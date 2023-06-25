import os
import json
from PIL import Image
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

def obtener_informacion_imagen(ruta_archivo):
    imagen = Image.open(ruta_archivo)
    return imagen.size

def obtener_calidad_audio(ruta_archivo):
    audio = AudioSegment.from_file(ruta_archivo)
    return audio.frame_rate

def obtener_calidad_video(ruta_archivo):
    video = VideoFileClip(ruta_archivo)
    return video.size

def generar_estructura_carpeta(carpeta_path):
    estructura = {}

    # Obtener el nombre de la carpeta
    nombre_carpeta = os.path.basename(carpeta_path)
    
    # Obtener la lista de archivos y carpetas en la carpeta actual
    archivos = []
    carpetas = []
    
    for elemento in os.listdir(carpeta_path):
        ruta_elemento = os.path.join(carpeta_path, elemento)
        if os.path.isfile(ruta_elemento):
            archivos.append(elemento)
        elif os.path.isdir(ruta_elemento):
            carpetas.append(elemento)
    
    # Agregar los archivos y carpetas a la estructura
    estructura['nombre'] = nombre_carpeta
    estructura['archivos'] = []
    estructura['carpetas'] = []
    
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_path, archivo)
        
        # Obtener información adicional según el tipo de archivo
        tipo_archivo = archivo.split('.')[-1].lower()
        informacion_adicional = {}
        
        if tipo_archivo in ['jpg', 'jpeg', 'png', 'gif']:
            informacion_adicional['tipo'] = 'imagen'
            informacion_adicional['resolucion'] = obtener_informacion_imagen(ruta_archivo)
        elif tipo_archivo in ['mp3', 'flac', 'wav', 'alac']:
            informacion_adicional['tipo'] = 'audio'
            informacion_adicional['calidad_audio'] = obtener_calidad_audio(ruta_archivo)
        elif tipo_archivo in ['mp4', 'mkv', 'avi']:
            informacion_adicional['tipo'] = 'video'
            informacion_adicional['calidad_video'] = obtener_calidad_video(ruta_archivo)
        
        archivo_info = {
            'nombre': archivo,
            'informacion_adicional': informacion_adicional
        }
        
        estructura['archivos'].append(archivo_info)
    
    for subcarpeta in carpetas:
        ruta_subcarpeta = os.path.join(carpeta_path, subcarpeta)
        estructura['carpetas'].append(generar_estructura_carpeta(ruta_subcarpeta))
    
    return estructura

def guardar_estructura_carpeta_en_json(carpeta_path, nombre_archivo):
    estructura = generar_estructura_carpeta(carpeta_path)
    
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(estructura, archivo_json, indent=4)

def guardar_estructura_carpeta_en_txt(carpeta_path, nombre_archivo):
    estructura = generar_estructura_carpeta(carpeta_path)
    
    with open(nombre_archivo, 'w') as archivo_txt:
        archivo_txt.write(json.dumps(estructura, indent=4))