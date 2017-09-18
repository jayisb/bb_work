import pyautogui
import time
from PIL import Image
import pyscreenshot as ImageGrab
import datetime
import os
import pyperclip

pyautogui.click(1850, 390)
time.sleep(3)

pyautogui.keyDown('pgdn')
time.sleep(1)
pyautogui.keyUp('pgdn')


pyautogui.press("pagedown")
pyautogui.press("pgdn")
