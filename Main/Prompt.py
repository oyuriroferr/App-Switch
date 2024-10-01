import os
from Colors import color
from getpass import getuser as user
from os import system as cmd
from os import getcwd, getenv
from time import sleep
from os import path
import shutil
import win32com.client

#  Create Shortcut

def create_file_shortcut(file_path, shortcut_name=None):
    # Initialize the Windows Shell
    shell = win32com.client.Dispatch("WScript.Shell")
    # Get the path to the desktop
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")

    # Set the name of the shortcut and the full path where it will be created
    if not shortcut_name:
        shortcut_name = os.path.basename(file_path)  # Use the original file name if no name is provided
    shortcut_path = os.path.join(desktop, shortcut_name + ".lnk")

    shortcut = shell.CreateShortcut(shortcut_path)

    shortcut.TargetPath = file_path

    shortcut.WorkingDirectory = os.path.dirname(file_path)

    shortcut.save()
# \Microsoft\Windows\Start Menu\Programs

#  Download Function
def download(file):
    # Games url
    minecraft = ['Minecraft',"https://tlauncher.org/installer"]
    roblox = ['Roblox',"https://www.roblox.com/pt/download/client?os=win"]
    among = ['Among Us',"https://download1478.mediafire.com/r8iwm6uij49gD-5rw1xygwaEQMDIx082wJqvwR22VajYQTfNr-JDegmR_kzR0O-FPgWQUWT5u4_jOUoOtrGLVWmNFEvJQGWsaLpWiHdv3vG3IjbuyZS6qfJ2F4dDeR1GJdhLXbxcEX-bYUNw3ka7Z_8woS3gJMH548Wh3dQqHWtplN8/t9i81p300f7ay5c/Among+Us.zip" ,r"downloads\Among Us"]
    cs = ['Counter Strike 1.6',"https://download948.mediafire.com/us3zvebxtzpgBmgv-l0gSEzs7NYRXvJ2KWpEyqhFexD0nAU3rPBkSQhOd-tx8TvKWc5BRMSXdvwyRqWDZb4_dLXoRk87IyKY_X5Ks2ojlN1UUD5SXUbIXJ3xkc_7yw4lwk6Dr6lVuNYh0rr_EyE6a5XCNdHZOKVpNsYDIjG7rP5QCks/zs4ns5e52llytbj/Cs1.6.zip", r"downloads\cs1.6"]
    terraria = ['Terraria',  "https://download1500.mediafire.com/lpxzherbxk0gERHDsX8ElaRK3OMcLOjxWJdh4bJD9__rhXblqBvC1TsuZl5jXMYjNIzs6el0IqUZvxybv2U9qaiKFbhDdzWGuTfQwZdima0cgJhecYoySsXue9Oy2EILjq8vrZZPHwHiYrnnYw2y7TfyWiwYoRgUSNMo87hN7SZ0bTY/h8zdlsij5ovnler/Terraria.zip", r"downloads\Terraria"]
    stardew = ['Stardew Valley', "https://download1979.mediafire.com/v23cfabv25qguG9RwZ2eFWdghT4EaS_MlealWZX4Qg21hRq2R-fIp4Lp8-6duG3kCpOMPbR43nKTf0zzF1a7KWmIvyLVPuYdmMGQ9Q0M-8JpSpuwfow3WWEH-mPTk26GrYyyZUOH9pLhzqyl_UrUYaPbn5MxyTxZqtw4iV9QoNwz8J8/02pvdsjmaxx05an/Stardew+Valley.zip", r"downloads\Stardew"]

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
        name = r"AmongUs.zip"
        if not path.exists("AmongUs.zip"):
            cmd(f'powershell Invoke-WebRequest ""{among[1]}"" -OutFile "{among[0].replace(" ","")+ '.zip'}"')
        appdata = getenv('APPDATA')
        desktop = path.join(os.environ["USERPROFILE"], "Desktop")
        file = appdata + r"\Among Us\Among Us\Among Us.exe"
        if not path.exists(file):
            shutil.unpack_archive(name, appdata + r"\Among Us", 'zip')
        create_file_shortcut(file, f"{among[0].replace(" ","")}")
        os.startfile(desktop+rf"\{among[0].replace(" ","")+".lnk"}")
        print(file.capitalize())

    elif file == 'cs':
        name = "CounterStrike1.6.zip"
        if not path.exists("CounterStrike1.6.zip"):
            cmd(f'powershell Invoke-WebRequest ""{cs[1]}"" -OutFile "{cs[0].replace(" ","")+ '.zip'}"')
        appdata = getenv('APPDATA')
        desktop = path.join(os.environ["USERPROFILE"], "Desktop")
        file = appdata + r"\cs1.6\Cs1.6\Counter-Strike WaRzOnE\CS16Launcher.exe"
        if not path.exists(file):
            shutil.unpack_archive(name, rf"{appdata}\cs1.6", 'zip')
        create_file_shortcut(file, f"{cs[0]}")
        os.startfile(desktop+rf"\{cs[0]+".lnk"}")
        print(file.capitalize())

    elif file == 'terraria':
        name = "Terraria.zip"
        if not path.exists("Terraria.zip"):
            cmd(f'powershell Invoke-WebRequest ""{terraria[1]}"" -OutFile "{terraria[0].replace(" ", "") + '.zip'}"')
        appdata = getenv('APPDATA')
        desktop = path.join(os.environ["USERPROFILE"], "Desktop")
        file = appdata + r"\Terraria\Terraria\Terraria.exe"
        if not path.exists(file):
            shutil.unpack_archive(name, rf"{appdata}\Terraria", 'zip')
        create_file_shortcut(file, f"{terraria[0]}")
        os.startfile(desktop + rf"\{terraria[0] + ".lnk"}")
        print(file.capitalize())

    elif file == 'stardew':
        name = "StardewValley.zip"
        if not path.exists("StardewValley.zip"):
            cmd(f'powershell Invoke-WebRequest ""{stardew[1]}"" -OutFile "{stardew[0].replace(" ", "") + '.zip'}"')
        appdata = getenv('APPDATA')
        desktop = path.join(os.environ["USERPROFILE"], "Desktop")
        file = appdata + r"\StardewValley\Stardew Valley\Stardew Valley.exe"
        if not path.exists(file):
            shutil.unpack_archive(name, rf"{appdata}\StardewValley", 'zip')
        create_file_shortcut(file, f"{stardew[0]}")
        os.startfile(desktop + rf"\{stardew[0] + ".lnk"}")
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
games_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:Minecraft{color.reset}\n{color.type.Black}>{color.fg.lightgrey} 1:Roblox{color.reset}\n{color.type.Black}>{color.fg.lightcyan} 2:Among Us{color.reset}\n{color.type.Black}>{color.fg.pink} 3:Counter Strike 1.6{color.reset}\n{color.type.Black}>{color.fg.lightgreen} 4:Terraria{color.reset}\n{color.type.Black}>{color.fg.orange} 5:Stardew Valley{color.reset}"
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
    elif option == '3':
        download("cs")
    elif option == '4':
        download("terraria")
    elif option == '5':
        download("stardew")
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


