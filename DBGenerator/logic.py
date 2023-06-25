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
    columnas_varchar = [
        "nombre_musica", "nombre_video", "nombre_imagen", "nombre_archivo", "formato_archivo", "resolucion_imagen"
    ]  # Columnas que serán del tipo VARCHAR(255)

    for carpeta in data["carpetas"]:
        archivos = carpeta["archivos"]
        for archivo in archivos:
            nombre_archivo, formato_archivo = archivo["nombre"].split(".")
            informacion_adicional = archivo["informacion_adicional"]
            tipo_archivo = informacion_adicional.get("tipo", "documento")
            
            if tipo_archivo in formatos:
                formatos_extensiones = formatos[tipo_archivo]
                if formato_archivo.lower() in formatos_extensiones:
                    if tipo_archivo == "audio":
                        table_name = "archivos_audio"
                        columns = "nombre_musica, formato_archivo, calidad_audio VARCHAR(255)"
                        additional_info = str(informacion_adicional.get("calidad_audio", "NULL"))
                    elif tipo_archivo == "video":
                        table_name = "archivos_video"
                        columns = "nombre_video, formato_archivo, calidad_video VARCHAR(255)"
                        additional_info = str(informacion_adicional.get("calidad_video", "NULL"))
                    elif tipo_archivo == "imagen":
                        table_name = "archivos_imagen"
                        columns = "nombre_imagen, formato_archivo, resolucion_imagen VARCHAR(255)"
                        additional_info = str(informacion_adicional.get("resolucion", "NULL"))
                    
                    if table_name not in table_statements:
                        table_statements.add(table_name)
                        
                        create_table_columns = ", ".join(
                            [f"{column} VARCHAR(255)" if column in columnas_varchar else column for column in columns.split(", ")]
                        )
                        create_table_statement = f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {create_table_columns});\n"
                        sql_code += create_table_statement
                    
                    if table_name not in insert_statements:
                        insert_statements[table_name] = []
                    
                    values = f'("{nombre_archivo}", "{formato_archivo}", "{additional_info}")'
                    insert_statements[table_name].append(values)
            
            else:
                table_name = "archivos_documentos"
                columns = "nombre_archivo, formato_archivo"
                
                if table_name not in table_statements:
                    table_statements.add(table_name)
                    
                    create_table_columns = ", ".join(
                        [f"{column} VARCHAR(255)" if column in columnas_varchar else column for column in columns.split(", ")]
                    )
                    create_table_statement = f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {create_table_columns});\n"
                    sql_code += create_table_statement
                
                if table_name not in insert_statements:
                    insert_statements[table_name] = []
                
                insert_statements[table_name].append(f'("{nombre_archivo}", "{formato_archivo}")')
    
    # Generar sentencias INSERT INTO
    for table_name, values in insert_statements.items():
        columns = table_name.replace("archivos_", "nombre_")
        values_str = ",\n".join(values)
        insert_statement = f"\nINSERT INTO {table_name} ({columns}, formato_archivo, resolucion_imagen) VALUES {values_str};\n"
        sql_code += insert_statement
    
    return sql_code

def import_json(json_file_path):
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        nombre_db = data["nombre"]
        sql_code = generate_sql_code(data)
        nombre_archivo = f"{nombre_db}_sqlcode.sql"
        with open(nombre_archivo, "w") as sql_file:
            sql_file.write(sql_code)
        print(f"Código SQL generado y guardado en '{nombre_archivo}'")
