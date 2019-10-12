#!/usr/bin/python3
import pyautogui, cv2
import os, time
from PIL import ImageGrab
import numpy as np
import img
from AppKit import NSWorkspace

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

# print(screenWidth, screenHeight)
# print(currentMouseX, currentMouseY)

# os.system("open /Applications/阴阳师.app")

# time.sleep(3)
# pyautogui.click(10, 300, 1, 0, 'left')

def getScreen ():
  pyautogui.screenshot('screen.png')
  screen = cv2.imread('screen.png')
  return screen

def detectScreenIsOk (screen, name):
  want = imgs[name]
  pts = img.locate(screen, want, 0)
  return pts
print(pyautogui.position())
# pyautogui.moveTo(874, 130)

# pyautogui.moveTo(1449, 319)

# imgs = img.load_imgs()

# # time.sleep(2)
# pyautogui.click(1296, 857, 1, 0, 'left')
# # time.sleep(6)
# pos = []
# screen = ''
# while (not pos):
#   print("not ok")
#   screen = getScreen()
#   pos = detectScreenIsOk(screen, 'index')
#   print('pos ', pos)
#   pyautogui.click(500, 600, 1, 0, 'left')
#   time.sleep(1)

# print("index ok, waiting for scaning qr code")
# pts = detectScreenIsOk(screen, 'close')
# print('close ', pts)
# while (pts):
#   print("waiting for scaning qr code")
#   screen = getScreen()
#   pts = detectScreenIsOk(screen, 'close')
#   print('close ', pts[0][0], pts[0][1])
#   pyautogui.click(pts[0][0], pts[0][1], 1, 0, 'left')
#   time.sleep(1)

# print('close ok')

# activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
# print(activeAppName)