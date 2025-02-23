import win32gui
import ctypes
import time
from random import randint

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
while True:
    rand = randint(3,9)
    rand = f"0.0{rand}"
    win32gui.InvertRect(hdc, (0, 0, w, h))
    time.sleep(float(rand))  # Adjust delay to your liking
