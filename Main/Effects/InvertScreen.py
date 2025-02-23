import win32api
import win32con
from time import sleep
from random import choice, randint
import pywintypes
import threading

def rotate_screen(rotation):
    device = win32api.EnumDisplayDevices(None, 0)
    devmode = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)

    if rotation == 0:
        devmode.DisplayOrientation = win32con.DMDO_DEFAULT
    elif rotation == 90:
        devmode.DisplayOrientation = win32con.DMDO_90
    elif rotation == 180:
        devmode.DisplayOrientation = win32con.DMDO_180
    elif rotation == 270:
        devmode.DisplayOrientation = win32con.DMDO_270

    try:
        win32api.ChangeDisplaySettingsEx(device.DeviceName, devmode)
    except pywintypes.error as e:
        print(e)

def mouse_click_listener():
    on_off = 0
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):  # Detecta clique esquerdo do mouse
            if on_off == 0:
                rotate_screen(180)
                on_off += 1
            elif on_off == 1:
                rotate_screen(0)
                on_off = 0

            sleep(0.5)  # Pequeno delay para evitar múltiplas rotações seguidas

def main():
    threading.Thread(target=mouse_click_listener, daemon=True).start()

    while True:
        rand = randint(6, 9)
        rotate_choice = choice([0, 90, 180, 270])
        rotate_screen(rotate_choice)
        sleep(rand)

if __name__ == "__main__":
    main()




"""
import win32gui
import win32api
import win32con
from time import sleep
from random import choice, randint
import pywintypes

# Rotacionar Tela
def rotate_screen(rotation):
    device = win32api.EnumDisplayDevices(None,0)
    devmode = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
    if rotation == 0:
        devmode.DisplayOrientation = win32con.DMDO_DEFAULT
    elif rotation == 90:
        devmode.DisplayOrientation = win32con.DMDO_90
    elif rotation == 180:
        devmode.DisplayOrientation = win32con.DMDO_180
    elif rotation == 270:
        devmode.DisplayOrientation = win32con.DMDO_270
    try:
        win32api.ChangeDisplaySettingsEx(device.DeviceName, devmode)
    except pywintypes.error as e:
        print(e)
count = 0
while True:
    rand = randint(3,6)
    rand = f"{rand}"
    rotate_choice = choice([0,90,180,270])
    count += 1 and rotate_choice == 180 if count == 0 else False
    rotate_screen(int(rotate_choice))
    sleep(int(rand))

"""
