#! python3
#mouseMove.py - moves mouse slightly to prevent from being set to idle
import pyautogui

print('Anti idle has been turned on')

while True:
    try:
        pyautogui.sleep(10)
        print('Moving mouse one pixel to the right')
        pyautogui.move(1, 0, duration = 0.2)
        pyautogui.sleep(10)
        print('Moving mouse one pixel to the left')
        pyautogui.move(-1, 0, duration = 0.2)
    except:
        break

print('Anti idle has been turned off')
