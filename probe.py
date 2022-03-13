import pyautogui as pt

position = pt.locateOnScreen('img.png', confidence=.7)
pt.moveTo(position[0:2], duration=.7)
pt.moveRel(100, 10, duration=.5)
pt.moveRel(10, -50, duration=.5)