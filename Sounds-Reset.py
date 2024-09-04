import winreg


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
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, subchave_caminho, 0, winreg.KEY_SET_VALUE) as subchave:
                    winreg.SetValueEx(subchave, "", 0, winreg.REG_SZ, "")  # Restaurar para sem som
                    print(f"Som restaurado para padrão: {subchave_caminho}")
            except FileNotFoundError:
                print(f"Subchave não encontrada: {subchave_caminho}")

    except PermissionError:
        print("Erro: É necessário executar o script com permissões de administrador.")
    except Exception as e:
        print(f"Erro ao restaurar sons: {e}")


if __name__ == "__main__":
    restaurar_sons_do_windows()
