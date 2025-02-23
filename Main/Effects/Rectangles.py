import win32gui
import ctypes
import win32api
from random import randint
from time import sleep
from win32con import HORZRES, VERTRES

# Define o DC
screen_dc = win32gui.GetDC(0)
# Lê a largura e altura da tela
screen_width = ctypes.windll.gdi32.GetDeviceCaps(screen_dc, HORZRES)
screen_height = ctypes.windll.gdi32.GetDeviceCaps(screen_dc, VERTRES)



"""# Define o retângulo
win32gui.Rectangle(screen_dc,50,200,500,400) # Esquerda Topo Direita Baixo"""

while True:
    # Define brush e suas cores do brush
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    brush = win32gui.CreateSolidBrush(win32api.RGB(red, green, blue))

    # Torna o brush utilizavel
    win32gui.SelectObject(screen_dc, brush)

    # Define o retângulo
    x1 = randint(0, screen_width)
    y1 = randint(0, screen_height)
    x2 = x1 + randint(10, 300)
    y2 = y1 + randint(10, 300)
    win32gui.Rectangle(screen_dc, x1, y1, x2, y2)  # Esquerda Topo Direita Baixo
    sleep(0.1)
