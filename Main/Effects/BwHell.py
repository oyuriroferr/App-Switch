import win32gui
import win32con
import ctypes
import random
from time import sleep

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
hdc = win32gui.GetDC(0)

while True:
    rand = random.randint(1,5)
    rand = f"0.0{rand}"
    win32gui.BitBlt(
        hdc,
        0,
        0,
        sw,
        sh,
        hdc,
        random.randrange(-3, 4),
        random.randrange(-3, 4),
        win32con.NOTSRCCOPY,
    )
    sleep(float(rand))