import ctypes
import win32gui
from win32con import HORZRES, VERTRES
from pyautogui import moveTo
from random import randint

screen_dc = win32gui.GetDC(0)
screen_width = ctypes.windll.gdi32.GetDeviceCaps(screen_dc, HORZRES)
screen_height = ctypes.windll.gdi32.GetDeviceCaps(screen_dc, VERTRES)

while True:
    moveTo(randint(10,screen_width),randint(10,screen_height), duration=float(f"0.{randint(2, 9)}"))
