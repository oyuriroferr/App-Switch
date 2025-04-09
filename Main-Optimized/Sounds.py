# Sounds.py
import os
import winreg
from Colors import color
from time import sleep
from getpass import getuser
from os import getcwd

user = getuser()
local_path = getcwd()

options = f"{color.fg.orange}Install{color.reset} {color.fg.cyan}[0]{color.reset} or {color.fg.red}Remove {color.fg.cyan}[1]{color.reset}"
shell_symbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"


def listar_sons(diretorio):
    if not os.path.exists(diretorio):
        print(f"Diretório não encontrado: {diretorio}")
        return []
    return [f for f in os.listdir(diretorio) if f.lower().endswith('.wav')]


def modificar_sons(diretorio):
    chave_registro = r"AppEvents\Schemes\Apps\.Default"
    try:
        chave = winreg.OpenKey(winreg.HKEY_CURRENT_USER, chave_registro, 0, winreg.KEY_READ)
        sons = listar_sons(diretorio)
        if not sons:
            print("Nenhum arquivo de som encontrado.")
            return
        for i in range(winreg.QueryInfoKey(chave)[0]):
            subchave_nome = winreg.EnumKey(chave, i)
            subchave_caminho = f"{chave_registro}\\{subchave_nome}\\.Current"
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, subchave_caminho, 0, winreg.KEY_SET_VALUE) as subchave:
                    caminho_som = os.path.join(diretorio, sons[i % len(sons)])
                    winreg.SetValueEx(subchave, "", 0, winreg.REG_SZ, caminho_som)
                    print(f"Substituído: {subchave_caminho} -> {caminho_som}")
            except Exception as e:
                print(f"Erro ao modificar {subchave_caminho}: {e}")
        winreg.CloseKey(chave)
    except Exception as e:
        print(f"Erro ao abrir chave de registro: {e}")


def restaurar_sons():
    chave_registro = r"AppEvents\Schemes\Apps\.Default"
    try:
        chave = winreg.OpenKey(winreg.HKEY_CURRENT_USER, chave_registro, 0, winreg.KEY_READ)
        for i in range(winreg.QueryInfoKey(chave)[0]):
            subchave_nome = winreg.EnumKey(chave, i)
            subchave_caminho = f"{chave_registro}\\{subchave_nome}\\.Current"
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, subchave_caminho, 0, winreg.KEY_SET_VALUE) as subchave:
                    winreg.SetValueEx(subchave, "", 0, winreg.REG_SZ, "")
                    print(f"Restaurado: {subchave_caminho}")
            except Exception as e:
                print(f"Erro ao restaurar {subchave_caminho}: {e}")
        winreg.CloseKey(chave)
    except Exception as e:
        print(f"Erro ao abrir chave de registro: {e}")


def main():
    print(options)
    opt = input(shell_symbol)
    if opt == '0':
        modificar_sons(local_path)
    elif opt == '1':
        restaurar_sons()
    else:
        print(wrong_value)
        sleep(10)
        exit(1)


if __name__ == "__main__":
    main()
