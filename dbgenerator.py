import json

def generate_sql_code(data):
    sql_code = ""
    
    # Obtener el nombre de la carpeta principal
    nombre_db = data["nombre"]
    
    # Crear la sentencia CREATE DATABASE
    create_db_statement = f"CREATE DATABASE {nombre_db};\n"
    sql_code += create_db_statement
    
    # Generar sentencia USE DATABASE
    use_db_statement = f"USE {nombre_db};\n\n"
    sql_code += use_db_statement
    
    # Definir formatos y tablas por formato
    formatos = {
        "audio": {
            "mp3", "flac", "alac", "aac", "wav", "aiff"
        },
        "imagen": {
            "bmp", "gif", "jpg", "tif", "png"
        },
        "video": {
            "mp4", "mkv", "wmv", "avi", "flv"
        }
    }
    
    table_statements = set()
    insert_statements = {}
    
    for carpeta in data["carpetas"]:
        archivos = carpeta["archivos"]
        for archivo in archivos:
            nombre_archivo, formato_archivo = archivo.split(".")
            
            for tipo_formato, formatos_extensiones in formatos.items():
                if formato_archivo.lower() in formatos_extensiones:
                    if tipo_formato == "audio":
                        table_name = "archivos_audio"
                        columns = "nombre_musica, formato_archivo"
                    elif tipo_formato == "video":
                        table_name = "archivos_video"
                        columns = "nombre_video, formato_archivo"
                    elif tipo_formato == "imagen":
                        table_name = "archivos_imagen"
                        columns = "nombre_imagen, formato_archivo, resolucion_imagen"
                    
                    if table_name not in table_statements:
                        table_statements.add(table_name)
                        
                        create_table_statement = f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {columns});\n"
                        sql_code += create_table_statement
                    
                    if table_name not in insert_statements:
                        insert_statements[table_name] = []
                    
                    # Modificar las comillas en los valores de inserción
                    if tipo_formato == "imagen":
                        values = f'("{nombre_archivo}", "{formato_archivo}", NULL)'
                    else:
                        values = f'("{nombre_archivo}", "{formato_archivo}")'
                    insert_statements[table_name].append(values)
                    break
            
            # Si el formato no coincide con ninguno, se asume archivos_documentos
            else:
                table_name = "archivos_documentos"
                columns = "nombre_archivo, formato_archivo"
                
                if table_name not in table_statements:
                    table_statements.add(table_name)
                    
                    create_table_statement = f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {columns});\n"
                    sql_code += create_table_statement
                
                if table_name not in insert_statements:
                    insert_statements[table_name] = []
                
                # Modificar las comillas en los valores de inserción
                insert_statements[table_name].append(f'("{nombre_archivo}", "{formato_archivo}")')
    
    # Generar sentencias INSERT INTO
    for table_name, values in insert_statements.items():
        columns = table_name.replace("archivos_", "nombre_")
        values_str = ",\n".join(values)
        insert_statement = f"\nINSERT INTO {table_name} ({columns}, formato_archivo, resolucion_imagen) VALUES {values_str};\n"
        sql_code += insert_statement
        
    return sql_code


# Cargar los datos desde el archivo JSON
with open("E&Y_estructura.json") as json_file:
    data = json.load(json_file)

# Obtener el nombre de la base de datos
nombre_db = data["nombre"]

# Generar el código SQL
sql_code = generate_sql_code(data)

# Definir el nombre del archivo SQL
nombre_archivo = f"{nombre_db}_sqlcode.sql"

# Guardar el código SQL en el archivo
with open(nombre_archivo, "w") as sql_file:
    sql_file.write(sql_code)

print(f"Código SQL generado y guardado en '{nombre_archivo}'")
