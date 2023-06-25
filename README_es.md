# PyRooter

PyRooter es una aplicación Python que genera la estructura de carpetas de un directorio seleccionado y la guarda como un archivo JSON.

## Instalación

1. Clona el repositorio: `git clone https://github.com/tunombredeusuario/pyrooter.git`
2. Instala las dependencias requeridas: `pip install -r requirements.txt`

## Uso

Ejecuta el archivo `main.py` para iniciar la aplicación. Se abrirá la ventana de la interfaz gráfica (GUI).

### Selección de la Carpeta

Haz clic en el botón "Seleccionar Carpeta" para elegir la carpeta objetivo de la cual deseas generar la estructura de carpetas.

### Generación de la Estructura

Después de seleccionar la carpeta, haz clic en el botón "Generar Estructura". La aplicación generará la estructura de carpetas y la guardará como un archivo JSON.

### Resultado

La estructura de carpetas generada se guardará como `estructura_carpeta.json` en el mismo directorio que el archivo `main.py`.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos:

- `main.py`: El script principal que inicia la aplicación y configura la GUI.
- `mainwindow.py`: Contiene la clase `MainWindow` que define la ventana principal de la interfaz gráfica y maneja los clics de los botones.
- `ui_mainwindow.py`: Archivo generado a partir del archivo de diseño de la interfaz `mainwindow.ui` utilizando el generador de código de interfaz de usuario de PyQt5.
- `folder_structure.py`: Contiene las funciones para generar y guardar la estructura de carpetas.
- `requirements.txt`: Lista de dependencias requeridas.
- `readme.md`: Archivo de documentación (lo estás leyendo en este momento).

## Contribuciones

Se aceptan solicitudes de extracción. Para cambios importantes, abre un problema primero para discutir qué te gustaría cambiar.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).
