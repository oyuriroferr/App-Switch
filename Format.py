import ctypes
from ctypes import wintypes
from Colors import color
from getpass import getuser as user
from os import system as cmd
from os import getcwd, getenv
from time import sleep
from string import ascii_lowercase

# Define user / hostname / local path / ascii_letters
alphabet = list(ascii_lowercase)
user = user()
hostname = getenv("COMPUTERNAME")
local_path = getcwd()
# If is in User_Path
if user in local_path:
    local_path = "~" + local_path[local_path.find(user[-1:])+1:].replace("\\","/")

# Text Samples
shell_simbol = f"{color.type.Black}{color.fg.blue}\n$ {color.reset}"
wrong_value = f"{color.fg.red}{color.type.Black}%ERROR%{color.reset} WRONG VALUE"
version = f"{color.type.Black}0.0.1 {color.reset}{color.fg.cyan}Beta{color.reset}"
user_text = f"{color.fg.green}({color.fg.blue}{user}@{hostname}{color.reset}{color.fg.green})-[{color.reset}{color.type.Black}{local_path}{color.fg.green}]{color.reset}"
folder_path_sample = f"{color.fg.lightred}{color.type.Black}Specify your directory{color.reset} [{color.fg.cyan}Like{color.reset}: '{color.fg.red}C:{color.reset}']"

# Constantes para manipulação de permissões
READ_CONTROL = 0x00020000
FILE_GENERIC_READ = 0x120089  # Permissões de leitura e execução
FILE_GENERIC_EXECUTE = 0x1200A0  # Permissões de execução

# Objeto de segurança (Security Descriptor)
SECURITY_DESCRIPTOR_REVISION = 1


def set_read_execute_permissions(folder_path):
    # Cria um objeto de segurança (security descriptor)
    sd = ctypes.windll.advapi32.InitializeSecurityDescriptor(None, SECURITY_DESCRIPTOR_REVISION)

    # Define as permissões de segurança para o diretório
    if not ctypes.windll.advapi32.SetSecurityDescriptorDacl(
            ctypes.byref(sd),
            True,
            None,  # ACL nula (padrão)
            False  # Não é ACL padrão
    ):
        raise ctypes.WinError()

    # Define permissões de "Ler" e "Executar" no diretório especificado
    permissions = FILE_GENERIC_READ | FILE_GENERIC_EXECUTE
    if not ctypes.windll.kernel32.SetFileSecurityW(
            ctypes.c_wchar_p(folder_path),
            ctypes.wintypes.DWORD(permissions),
            sd
    ):
        raise ctypes.WinError()


# Exemplo de uso
cmd("cls")
folder_path = str(input(f"{folder_path_sample}\n{shell_simbol}")).strip(" :;,./?'[]{}\|*+-")
if folder_path[0].lower() in alphabet :
    set_read_execute_permissions(folder_path[0])
else :
    cmd("cls")
    print(f"{"\n" * 35}{wrong_value}\n{version} By {color.type.Black}{color.fg.purple}EoRoferr{color.reset}")
    sleep(10)
    exit(1)