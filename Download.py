from urllib.request import urlretrieve
from os import system as cmd
from time import sleep
from os import path

#  Download Function
def download(file):
    # Games url
    minecraft = ['Minecraft',"https://tlauncher.org/installer"]
    roblox = ['Roblox',"https://www.roblox.com/pt/download/client?os=win"]

    # Apps url
    pycharm = ['PyCharm',"https://download.jetbrains.com/python/pycharm-community-2024.2.0.1.exe"]


    if file == 'minecraft':
        file_name = path.join("downloads", file + ".exe")
        urlretrieve(minecraft[1],file_name)
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {minecraft[0]}.exe"')
        print(file.capitalize())

    elif file == 'roblox':
        file_name = path.join("downloads", file + ".exe")
        urlretrieve(roblox[1], file_name)
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {roblox[0]}.exe"')
        print(file.capitalize())

    elif file == 'pycharm':
        file_name = path.join("downloads", file + ".exe")
        urlretrieve(pycharm[1], file_name)
        cmd(f'cmd.exe /C "cd downloads && set __COMPAT_LAYER=RUNASINVOKER && {pycharm[0]}.exe"')
        print(file.capitalize())
    sleep(10)