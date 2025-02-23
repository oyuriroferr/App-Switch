import win32api
import win32gui
import win32con
from win32con import HORZRES, VERTRES
import ctypes
from time import sleep

hdc = win32gui.GetDC(0)

while True:
    x, y = win32api.GetCursorPos()
    win32gui.DrawIcon(
        hdc,
        x,
        y,
        win32gui.LoadIcon(None, win32con.IDI_ERROR),
    )
    sleep(0.009)
    # Change IDI_ERROR to something else to change the icon being displayed
