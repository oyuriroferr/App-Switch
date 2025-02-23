import win32gui
import win32con
import ctypes
from time import sleep
from random import randint

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


rand = randint(3,6)
rand = f"0.{rand}"
size = 100
while True:
    hdc = win32gui.GetDC(0)
    win32gui.StretchBlt(
        hdc,
        int(size / 2),
        int(size / 2),
        sw - size,
        sh - size,
        hdc,
        0,
        0,
        sw,
        sh,
        win32con.SRCCOPY,
    )
    sleep(float(rand))
