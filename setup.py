import venv
import os
import subprocess
import sys
import importlib.util

def create_virtual_environment(venv_dir):
    venv.create(venv_dir, with_pip=True)

def activate_virtual_environment(venv_dir):
    activate_script = os.path.join(venv_dir, 'Scripts', 'Activate.ps1')
    subprocess.check_call(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-Command', activate_script])

if __name__ == '__main__':
    # Obtener la ruta completa del directorio components/installer
    components_dir = os.path.join(os.getcwd(), 'components')
    installer_dir = os.path.join(components_dir, 'ScriptInstaller')

    # Agregar la ruta del directorio al sys.path para que pueda importar el módulo
    sys.path.append(components_dir)

    # Importar el módulo install_dependencies utilizando importlib
    module_name = 'ScriptInstaller.install_dependencies'
    module_path = os.path.join(installer_dir, 'install_dependencies.py')
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    venv_dir = 'myenv'  # Nombre del directorio del entorno virtual
    
    create_virtual_environment(venv_dir)
    activate_virtual_environment(venv_dir)

    module.install_requirements()
