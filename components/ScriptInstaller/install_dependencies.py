import subprocess

def install_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

    for requirement in requirements:
        subprocess.check_call(['pip', 'install', requirement])

if __name__ == '__main__':
    install_requirements()
