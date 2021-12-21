from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile 1 position = X: 516 Y:  350 RGB: (  0,  34,  64)
#tile 2 position = X: 619 Y:  350 RGB: (  0,  34,  64)
#tile 3 position = X: 732 Y:  350 RGB: (  0,  34,  64)
#tile 4 position = X: 835 Y:  350 RGB: (  0,  34,  64)

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.09)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def clicked():
    print("Click!")


while keyboard.is_pressed("s") == False:
    if pyautogui.pixel(516, 400) [0] == 0:
            click(516,400)
            clicked()
    if pyautogui.pixel(619, 400) [0] == 0:
            click(619,400)
            clicked()
    if pyautogui.pixel(732, 400) [0] == 0:
            click(732,400)
            clicked()
    if pyautogui.pixel(835, 400) [0] == 0:
            click(835,400)
            clicked()
