class color:
    reset = '\033[0m'
    class type:
        Black = '\033[1m'
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
class text:
    from getpass import getuser as user
    from os import getcwd, getenv, path

    # Define user / hostname / local path
    user = user()
    hostname = getenv("COMPUTERNAME")
    local_path = getcwd()
    user_home = path.expanduser('~')
    # If is in user path
    if local_path.startswith(user_home):
        local_path = local_path.replace(user_home, "~")

    # Variaveis
    user_text = f"{color.fg.green}({color.fg.blue}{user}@{hostname}{color.reset}{color.fg.green})-[{color.reset}{color.type.Black}{local_path}{color.fg.green}]{color.reset}"
    games_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:Minecraft{color.reset}\n{color.type.Black}>{color.fg.lightgrey} 1:Roblox{color.reset}\n{color.type.Black}>{color.fg.lightcyan} 2:Among Us{color.reset}\n{color.type.Black}>{color.fg.green} 3:Cs 1.6{color.reset}\n{color.type.Black}>{color.fg.lightgreen} 4:Terraria{color.reset}\n{color.type.Black}>{color.fg.orange} 5:Stardew Valley{color.reset}"
    app_options = f"{color.fg.orange}Options:{color.reset}\n\n{color.type.Black}>{color.fg.green} 0:PyCharm{color.reset}"
    shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
    wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"
    which_app = f"{color.fg.yellow}Installer{color.reset}{color.fg.cyan}[{color.fg.blue}0{color.fg.cyan}]{color.reset} {color.type.Black},{color.reset} {color.fg.purple}Sound Virus{color.reset}{color.fg.cyan}[{color.fg.blue}1{color.fg.cyan}]{color.reset}{color.type.Black} or {color.reset}{color.fg.red}KeyLogger{color.reset}{color.fg.cyan}[{color.fg.blue}2{color.fg.cyan}]"
    version = f"{color.type.Black}0.0.1 {color.reset}{color.fg.cyan}Beta{color.reset}"
    options = f"{color.fg.orange}Install{color.reset} {color.fg.cyan}[{color.fg.blue}0{color.fg.cyan}]{color.type.Black} or {color.fg.red}Remove {color.fg.cyan}[{color.fg.blue}1{color.fg.cyan}]{color.reset}"
