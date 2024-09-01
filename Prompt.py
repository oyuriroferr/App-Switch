from Download import download
from Colors import color
from getpass import getuser as user
from os import system as cmd
from os import getcwd, getenv
from time import sleep

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
games_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:Minecraft{color.reset}\n{color.type.Black}>{color.fg.lightgrey} 1:Roblox{color.reset}"
app_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:PyCharm{color.reset}"
shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"
version = f"{color.type.Black}0.0.1 {color.reset}{color.fg.cyan}Beta{color.reset}"

# Prompt
cmd("cls")
option = str(input(f"{color.fg.green}Games[0]{color.reset} or {color.fg.red}Apps[1]{color.reset}\n{color.type.Black}>{color.reset}"))
if option == '0':
    cmd("cls")
    print(games_options)
    option = str(input(f"{shell_simbol}"))
    if option == '0':
        download("minecraft")
    elif option == '1':
        download("roblox")
    else:
        print(f"{wrong_value}")
        sleep(10)
        exit(1)
        
elif option == '1':
    cmd("cls")
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


