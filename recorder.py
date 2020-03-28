import subprocess
import keyboard
import pyautogui
import threading
from pynput.mouse import Listener

start = False
positions = []


def mouseDown(x, y):
    global start, positions
    positions.append(str(x) + "," + str(y))
    positions.append("click")
    start = True
    return True


def mouseUp(x, y):
    global start, positions
    positions.append(str(x) + "," + str(y))
    positions.append("end")
    start = False
    return True


def mouseMove(x, y):
    global positions
    if start:
        positions.append(str(x) + "," + str(y))
    return True


def save2file(positions):
    with open('positions.txt', 'w') as f:
        for item in positions:
            f.write("%s\n" % str(item))


def keydown(event):
    global positions
    if event.name == "q":
        save2file(positions)
        exit()
    return True


def on_click(x, y, button, pressed):
    if button.name == 'left':
        if pressed:
            mouseDown(x, y)
        else:
            mouseUp(x, y)


def hookKey():
    keyboard.on_press(keydown)
    keyboard.wait()


subprocess.call(["cmd", "/c", "start", "/max", "mspaint.exe"])
SIZE_X, SIZE_Y = pyautogui.size()
positions.append(str(SIZE_X) + "," + str(SIZE_Y))
threading.Thread(target=hookKey).start()
with Listener(
        on_move=mouseMove,
        on_click=on_click) as listener:
    listener.join()
