import time

import pyautogui

screenWidth , screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.moveTo(100, 150)
pyautogui.click()
time.sleep(3)
pyautogui.click(400, 700)
pyautogui.press('enter')
pyautogui.write('xin chao', interval=0.25)