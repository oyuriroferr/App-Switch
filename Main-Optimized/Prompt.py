# Prompt.py
import os
from Colors import color
from Colors import text
from os import system as cmd, path
from pathlib import Path
from time import sleep
import win32com.client


# Create Shortcut
def create_file_shortcut(file_path, shortcut_name=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    if not shortcut_name:
        shortcut_name = os.path.basename(file_path)
    shortcut_path = os.path.join(os.environ["USERPROFILE"], "Desktop", f"{shortcut_name}.lnk")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = file_path
    shortcut.WorkingDirectory = os.path.dirname(file_path)
    shortcut.save()


# Download Function
def download_game(file, url, file_name):
    file_path = Path(f"downloads/{file_name + ".exe"}")
    if file_path.is_file():
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {file}.exe"')
    elif not file_path.is_file():

        full_path = path.join("downloads", f"{file}.exe")
        cmd(f'powershell Invoke-WebRequest "{url}" -OutFile "{full_path}"')
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {file}.exe"')
        print(file.capitalize())
    else:
        print("Erro ao baixar/executar")


# Mapping games and their URLs
games = {
    'minecraft': ["Minecraft", "https://tlauncher.org/installer"],
    'roblox': ["Roblox", "https://www.roblox.com/pt/download/client?os=win"],
    'among': ["Among Us", "https://download1478.mediafire.com/..."],
    'cs': ["Counter Strike 1.6", "https://download948.mediafire.com/..."],
    'terraria': ["Terraria", "https://download1500.mediafire.com/..."],
    'stardew': ["Stardew Valley", "https://download1979.mediafire.com/..."],
    'pycharm': ["PyCharm", "https://download.jetbrains.com/python/pycharm-community-2024.2.0.1.exe"]
}

# Clear prompt
cmd("cls")
print(text.user_text)
option = input(
    f"{color.fg.green}Games[0]{color.reset} or {color.fg.red}Apps[1]{color.reset}\n{color.type.Black}>{color.reset}")

if option == '0':
    cmd("cls")
    print(text.user_text)
    print(text.games_options)
    game_option = input(f"{text.shell_simbol}")
    if game_option in map(str, range(len(games))):
        game_key = list(games.keys())[int(game_option)]
        download_game(game_key, games[game_key][1], f"{games[game_key][0]}.exe")
    else:
        print(f"{text.wrong_value}")
        sleep(10)
        exit(1)

elif option == '1':
    cmd("cls")
    print(text.user_text)
    print(text.app_options)
    app_option = input(f"{text.shell_simbol}")
    if app_option == '0':
        download_game('pycharm', games['pycharm'][1], 'PyCharm.exe')
    else:
        print(f"{text.wrong_value}")
        sleep(10)
        exit(1)
else:
    cmd("cls")
    print(f"{text.wrong_value}\n{'-' * 35}\n{text.version} By {color.type.Black}{color.fg.purple}EoRoferr{color.reset}")
    sleep(10)
    exit(1)
