import os
import winreg
from Colors import color
from time import sleep
from getpass import getuser as user
from os import getcwd, getenv

# Define user / hostname / local path
user = user()
hostname = getenv("COMPUTERNAME")
local_path = getcwd()
# If is in User_Path
if user in local_path:
    local_path = "~" + local_path[local_path.find(user[-1:])+1:].replace("\\","/")

# Text Samples
options = f"{color.fg.orange}Install{color.reset} {color.fg.cyan}[{color.fg.blue}0{color.fg.cyan}]{color.type.Black} or {color.fg.red}Remove {color.fg.cyan}[{color.fg.blue}1{color.fg.cyan}]{color.reset}"
shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"
user_text = f"{color.fg.green}({color.fg.blue}{user}@{hostname}{color.reset}{color.fg.green})-[{color.reset}{color.type.Black}{local_path}{color.fg.green}]{color.reset}"
shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"

# Sounds Function
def listar_sons_disponiveis(diretorio):
    """
    Lista todos os arquivos .wav em um diretório especificado que começam com 'a'.
    """
    sons = [f for f in os.listdir(diretorio) if f.lower().endswith('.wav') and f.lower().startswith('a')]
    return sons


def modificar_sons_do_windows(diretorio):
    """
    Modifica os sons do sistema do Windows para usar arquivos .wav que começam com 'a'.
    """
    chave_registro = r"AppEvents\Schemes\Apps\.Default"
    try:
        # Abre o registro para ler os sons configurados
        chave = winreg.OpenKey(winreg.HKEY_CURRENT_USER, chave_registro, 0, winreg.KEY_READ)
        sons = listar_sons_disponiveis(diretorio)

        for i in range(0, winreg.QueryInfoKey(chave)[0]):
            subchave_nome = winreg.EnumKey(chave, i)
            subchave_caminho = f"{chave_registro}\\{subchave_nome}\\.Current"
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, subchave_caminho, 0, winreg.KEY_SET_VALUE) as subchave:
                    caminho_som = os.path.join(diretorio, sons[i % len(sons)])  # Escolhe um som aleatoriamente
                    winreg.SetValueEx(subchave, "", 0, winreg.REG_SZ, caminho_som)
                    print(f"Substituído: {subchave_caminho} -> {caminho_som}")
            except FileNotFoundError:
                print(f"Subchave não encontrada: {subchave_caminho}")
    except Exception as e:
        print(f"Erro ao modificar sons: {e}")


# Remove Function
def restaurar_sons_do_windows():
        """
        Restaura os sons do sistema do Windows para seus valores padrão (geralmente sem som).
        """
        chave_registro = r"AppEvents\Schemes\Apps\.Default"
        try:
            chave = winreg.OpenKey(winreg.HKEY_CURRENT_USER, chave_registro, 0, winreg.KEY_READ)

            for i in range(0, winreg.QueryInfoKey(chave)[0]):
                subchave_nome = winreg.EnumKey(chave, i)
                subchave_caminho = f"{chave_registro}\\{subchave_nome}\\.Current"
                try:
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, subchave_caminho, 0,
                                        winreg.KEY_SET_VALUE) as subchave:
                        winreg.SetValueEx(subchave, "", 0, winreg.REG_SZ, "")  # Restaurar para sem som
                        print(f"Som restaurado para padrão: {subchave_caminho}")
                except FileNotFoundError:
                    print(f"Subchave não encontrada: {subchave_caminho}")
        except Exception as e:
            print(f"Erro ao restaurar sons: {e}")
# Choosing

option = str(input(f"{options}\n{shell_simbol}"))
print(user_text)
if option == "1":
    restaurar_sons_do_windows()
elif option == "0":
    path = os.getcwd() + "\\downloads\\audios\\"
    diretorio_dos_sons = path
    modificar_sons_do_windows(diretorio_dos_sons)
else:
    print(f"{wrong_value}")
    sleep(10)
    exit(1)
