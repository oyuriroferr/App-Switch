# Switch-App.py
import subprocess
from Colors import color
from os import getenv, path
from time import sleep
from pathlib import Path
import platform

# Verifica se o sistema operacional é Windows
if platform.system() != "Windows":
    print("Este script é compatível apenas com o Windows.")
    exit(1)

# Text Samples
from Colors import text
which_app = text.which_app
shell_symbol = text.shell_simbol
wrong_value = text.wrong_value
user_text = text.user_text

# Constants
APPDATA = getenv('APPDATA')
LOG_DIR = path.join(APPDATA, "MicrosoftWindowsAgent")
LOG_FILE = path.join(LOG_DIR, "log.txt")


def cls():
    subprocess.run("cls", shell=True, check=True)


def handle_option(option):
    cls()
    if option == '0':
        subprocess.run(["python", "Prompt.py"], check=True)
    elif option == '1':
        subprocess.run(["python", "Sounds.py"], check=True)
    elif option == '2':
        subprocess.run(["python", "agnsrvch.py"], check=True)
    else:
        print(f"Opção inválida: '{option}'. Por favor, escolha uma das opções: 0, 1 ou 2.")
        sleep(5)
        exit(1)


# Início do programa
cls()
print(user_text)

valid_options = ['0', '1', '2']
option = input(f"{which_app}\n{shell_symbol}")

handle_option(option)
