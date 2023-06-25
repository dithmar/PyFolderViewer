import os
import json

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
    estructura['archivos'] = archivos
    estructura['carpetas'] = []
    
    for subcarpeta in carpetas:
        ruta_subcarpeta = os.path.join(carpeta_path, subcarpeta)
        estructura['carpetas'].append(generar_estructura_carpeta(ruta_subcarpeta))
    
    return estructura

def guardar_estructura_carpeta_en_json(carpeta_path, nombre_archivo):
    estructura = generar_estructura_carpeta(carpeta_path)
    
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(estructura, archivo_json, indent=4)
