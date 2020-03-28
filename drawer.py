import subprocess
import threading
import time
import os
import webbrowser
import pyautogui
from pynput.mouse import Button, Controller

mouse = Controller()


def clickeDown():
    mouse.press(Button.left)


def clickup():
    mouse.release(Button.left)


def move(x, y):
    mouse.position = (x, y)


def draw():
    with open("positions.txt") as f:
        line = f.readline()
        line = line.strip()
        position = line.split(",")
        width = int(position[0].strip())
        height = int(position[1].strip())
        SIZE_X, SIZE_Y = pyautogui.size()
        wco = SIZE_X / width
        hco = SIZE_Y / height
        for line in f:
            time.sleep(0.003)
            line = line.strip()
            if line == "click":
                clickeDown()
            elif line == "end":
                clickup()
            else:
                position = line.split(",")
                x = int(position[0].strip()) * wco
                y = int(position[1].strip()) * hco
                move(x, y)


html_str = "<html><head></head><body><h1>dont touch the computer!!!</h1></body></html>"
f = open("yourpage.html","w")
f.write(html_str)
f.close()
filename = os.getcwd()+'/' + 'yourpage.html'
webbrowser.open_new_tab(filename)
time.sleep(3)
subprocess.call(["cmd", "/c", "start", "/max", "mspaint.exe"])
time.sleep(1)
draw()
