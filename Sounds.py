import os
import winreg
path = os.getcwd() + "\\downloads\\audios\\"

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

    except PermissionError:
        print("Erro: É necessário executar o script com permissões de administrador.")
    except Exception as e:
        print(f"Erro ao modificar sons: {e}")


if __name__ == "__main__":
    diretorio_dos_sons = path  # Defina o caminho para o diretório que contém os sons
    modificar_sons_do_windows(diretorio_dos_sons)
