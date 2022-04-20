#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pyautogui
import XY
pyautogui.PAUSE = .4
import random





def playCards():

    X = XY.HAND_RIGHT # play cards on active spot 75%, first bench 25%
    i = 0 
    while i < 900:
        pyautogui.click(X[0]-i,X[1])
        if random.randint(0,4):
            pyautogui.click(XY.ACTIVE)
        else:
            pyautogui.click(XY.BENCH)

        # pyautogui.click(75,430) # click off to side to ready cards

        i += 100 # shift right

    return

def attack():
    pyautogui.click(75,430) # click off to side to ready attack

    pyautogui.click(XY.ACTIVE)
    time.sleep(.4)
    pyautogui.click(XY.ATTACK)

    pyautogui.click(75,430) # click off to side to ready for next action

    return

def Done():
    pyautogui.click(XY.DONE_DEFAULT)
    pyautogui.click(XY.YES_2)

    return

def autoBattle():

    while not pyautogui.locateOnScreen('Play!.png'): # wait for play to be available
        print("Waiting",end = '\r')
        pass
    pyautogui.click( 700 , 550) # click Play!

    # wait for initializer
    while not pyautogui.locateOnScreen('initializer.png'): # wait for match
        print("Waiting",end = '\r')
        pass

    time.sleep(3)

    pyautogui.click(XY.HEADS) # not always useful

    time.sleep(4)

    pyautogui.click(XY.YES) # this neither

    time.sleep(4)

    pyautogui.click(XY.YES) # just in case    

    i = 0
    while True: # main game loop

        playCards()
        attack()
        Done()
        i += 1
        if i % 2:
            if pyautogui.locateOnScreen('Play!.png'):
                return 1


def main():

    time.sleep(2) # time to stop between games

    startTime = time.time()

    print(startTime)

    battles = 0

    while autoBattle():
        battles += 1
        print("Battle #" + str(battles) + " Complete")

    print("\nDone\n")

    print(time.time())

    print("Average battles / time: " + str(battles / (time.time() - startTime)))

    return 0

if __name__ == "__main__":
    main()