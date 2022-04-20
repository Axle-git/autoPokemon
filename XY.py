from re import A
import pyautogui

ACTIVE = (725,469)
ATTACK = (959,456)
BENCH = (492,665)
BENCH_SEPERATION = 110
HAND_LEFT = (324,806)
HAND_RIGHT = (1120,806)
DONE_DEFAULT = (1117,700)
HEADS = (600,700)
YES =(820,700)
YES_2 = (625,430)

def find_XY():
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

