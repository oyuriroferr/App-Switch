import os
from Colors import color
from getpass import getuser as user
from os import system as cmd
from os import getcwd, getenv
from time import sleep
from os import path
import shutil

#  Download Function
def download(file):
    # Games url
    minecraft = ['Minecraft',"https://tlauncher.org/installer"]
    roblox = ['Roblox',"https://www.roblox.com/pt/download/client?os=win"]
    among = ['Among Us', r"downloads\Among Us"]


    # Apps url
    pycharm = ['PyCharm',"https://download.jetbrains.com/python/pycharm-community-2024.2.0.1.exe"]


    if file == 'minecraft':
        file_name = path.join("downloads", file + ".exe")
        cmd(f'powershell Invoke-WebRequest "{minecraft[1]}" -OutFile "{file_name}"')
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {minecraft[0]}.exe"')
        print(file.capitalize())

    elif file == 'roblox':
        file_name = path.join("downloads", file + ".exe")
        cmd(f'powershell Invoke-WebRequest "{roblox[1]}" -OutFile "{file_name}"')
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {roblox[0]}.exe"')
        print(file.capitalize())

    elif file == 'among':
        appdata = getenv('APPDATA')
        #shutil.move(among[1], f"{appdata + r'\Among Us'}")
        shutil.copytree(among[1],f"{appdata + r'\Among Us'}" )
        file = appdata + r"\Among Us\Among Us.exe"
        os.startfile(file)
        print(file.capitalize())

    elif file == 'pycharm':
        file_name = path.join("downloads", file + ".exe")
        cmd(f'powershell Invoke-WebRequest "{pycharm[1]}" -OutFile "{file_name}"')
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {pycharm[0]}.exe"')
        print(file.capitalize())
    sleep(10)

# Define user / hostname / local path
user = user()
hostname = getenv("COMPUTERNAME")
local_path = getcwd()
# If is in User_Path
if user in local_path:
    local_path = "~" + local_path[local_path.find(user[-1:])+1:].replace("\\","/")

# Clear prompt
cmd("cls")

# Text Samples

user_text = f"{color.fg.green}({color.fg.blue}{user}@{hostname}{color.reset}{color.fg.green})-[{color.reset}{color.type.Black}{local_path}{color.fg.green}]{color.reset}"
games_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:Minecraft{color.reset}\n{color.type.Black}>{color.fg.lightgrey} 1:Roblox{color.reset}\n{color.type.Black}>{color.fg.lightcyan} 2:Among Us{color.reset}"
app_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:PyCharm{color.reset}"
shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"
version = f"{color.type.Black}0.0.1 {color.reset}{color.fg.cyan}Beta{color.reset}"

# Prompt
cmd("cls")
print(user_text)
option = str(input(f"{color.fg.green}Games[0]{color.reset} or {color.fg.red}Apps[1]{color.reset}\n{color.type.Black}>{color.reset}"))
if option == '0':
    cmd("cls")
    print(user_text)
    print(games_options)
    option = str(input(f"{shell_simbol}"))
    if option == '0':
        download("minecraft")
    elif option == '1':
        download("roblox")
    elif option == '2':
        download("among")
    else:
        print(f"{wrong_value}")
        sleep(10)
        exit(1)
        
elif option == '1':
    cmd("cls")
    print(user_text)
    print(app_options)
    option = str(input(f"{shell_simbol}"))
    if option == '0':
        download("pycharm")
    else:
        print(f"{wrong_value}")
        sleep(10)
        exit(1)
else:
    cmd("cls")
    print(f"{"\n"*35}{wrong_value}\n{version} By {color.type.Black}{color.fg.purple}EoRoferr{color.reset}")
    sleep(10)
    exit(1)


