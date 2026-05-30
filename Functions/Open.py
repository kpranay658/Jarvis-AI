import pyautogui
from time import sleep
def Opener(Name):
    pyautogui.press('win')
    sleep(0.5)
    pyautogui.write(Name)
    pyautogui.press('enter')
