#! python3
#textFieldReader.py - reads the text field in a notepad window
import pyperclip
import pyautogui

# Selects notepad window
print('Making notepad window active window...')
notepad = pyautogui.getWindowsWithTitle('Notepad')[0]
try:
    notepad.activate()
except Exception as Err:
    print(Err)

# Selects text field and copies text
top, left = notepad.topleft
pyautogui.click((top + 200, left + 100))
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

pyautogui.sleep(1)

text = pyperclip.paste()
print(text)


