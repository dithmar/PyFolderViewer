import re
import os
from pathlib import Path

def convert_to_postgresql(sql):
    # Reemplazar las palabras clave y sintaxis específicas de MySQL por las correspondientes de PostgreSQL
    converted_sql = re.sub(r"\bAUTO_INCREMENT\b", "", sql, flags=re.IGNORECASE)
    converted_sql = re.sub(r"\bUNSIGNED\b", "", converted_sql, flags=re.IGNORECASE)
    converted_sql = re.sub(r"\bON UPDATE CURRENT_TIMESTAMP\b", "", converted_sql, flags=re.IGNORECASE)

    # Reemplazar el motor de almacenamiento por defecto en PostgreSQL (opcional)
    converted_sql = re.sub(r"\bENGINE\s*=\s*InnoDB\b", "", converted_sql, flags=re.IGNORECASE)

    # Convertir tipos de datos específicos de MySQL a sus equivalentes en PostgreSQL
    converted_sql = re.sub(r"\bINT\b", "SERIAL", converted_sql, flags=re.IGNORECASE)
    converted_sql = re.sub(r"\bVARCHAR\b", "TEXT", converted_sql, flags=re.IGNORECASE)

    # Agregar el prefijo "public." a las tablas para evitar problemas de esquema en PostgreSQL
    converted_sql = re.sub(r"\bCREATE TABLE (\w+)", r"CREATE TABLE \1", converted_sql, flags=re.IGNORECASE)

    # Reemplazar el comando USE de MySQL por el comando \c de PostgreSQL
    converted_sql = re.sub(r"\bUSE (\w+);", r"\\c \1;", converted_sql, flags=re.IGNORECASE)

    # Convertir sintaxis de valores literales de MySQL a PostgreSQL
    converted_sql = re.sub(r'(?<!")("NULL"|NULL)', 'NULL', converted_sql)
    converted_sql = re.sub(r'"', "'", converted_sql)

    return converted_sql

# Obtener la ruta del script actual
script_path = Path(os.path.abspath(__file__))

# Obtener la ruta del directorio padre del script
script_directory = script_path.parent

# Construir la ruta completa del archivo
input_file = script_directory / "Archivos_variados_sqlcode.sql"
output_file = script_directory / "postgresql_script.sql"

if input_file.exists():
    # Leer el contenido del archivo
    with input_file.open("r") as file:
        mysql_sql = file.read()

    # Convertir el código SQL
    postgresql_sql = convert_to_postgresql(mysql_sql)

    # Escribir el código convertido en el archivo de salida
    with open(output_file, "w") as file:
        file.write(postgresql_sql)

    print("Conversión completada. El código convertido se ha guardado en", output_file)
else:
    print("El archivo", input_file, "no existe.")
