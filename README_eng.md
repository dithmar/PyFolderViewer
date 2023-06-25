# PyRooter

PyRooter is a Python application that generates the folder structure of a selected directory and saves it as a JSON file.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/pyrooter.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

Run the `main.py` file to launch the application. The GUI window will open.

### Selecting the Folder

Click on the "Seleccionar Carpeta" button to choose the target folder for which you want to generate the folder structure.

### Generating the Structure

After selecting the folder, click on the "Generar Estructura" button. The application will generate the folder structure and save it as a JSON file.

### Output

The generated folder structure will be saved as `estructura_carpeta.json` in the same directory as the `main.py` file.

## Project Structure

The project consists of the following files:

- `main.py`: The main script that launches the application and sets up the GUI.
- `mainwindow.py`: Contains the `MainWindow` class that defines the main GUI window and handles button clicks.
- `ui_mainwindow.py`: Generated file from the UI design file `mainwindow.ui` using PyQt5 UI code generator.
- `folder_structure.py`: Contains functions for generating and saving the folder structure.
- `requirements.txt`: List of required dependencies.
- `readme.md`: Documentation file (you're reading it right now).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
