#! python3
# hangoutBot.py - sends out a message to a select group of people on Google hangouts
import os
import pyautogui
import webbrowser
import threading

pyautogui.PAUSE = 0.5
people = ['Python Test Group', 'Example Person'] # groups or people you want to message
messages = input('What do you want to send to your groups?\n')
browserPath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # can be removed

# Folder for saving screenshots and with the images you need
userDirectory = ''
os.chdir(userDirectory)
newConvoImg = 'example.PNG' # screenshot of the green circle w/ a plus sign on the home page
messageImg= = 'message.PNG' # screenshot of 'Send a message' text in input box while in a chat

# Types to groups/conversations
def sendingMessages(groups, notification):
    pyautogui.sleep(5)
    pyautogui.screenshot().save('Active Window.png')

    if pyautogui.locateOnScreen(newConvoImg) is None:
        pyautogui.hotkey('ctrl', 'r')
        pyautogui.sleep(3)

    i = 0
    attempts = 3
    pyautogui.click(newConvoImg)
    for names in groups:
        while attempts > 0:
            pyautogui.write(names + '\n', 0.2)
            pyautogui.sleep(2)
            if pyautogui.locateOnScreen(messageImg) is None:
                pyautogui.click()
                continue
            break
        pyautogui.write(notification + '\n', 0.2)
        pyautogui.screenshot().save('group' + str(i) + '.png')
        i += 1
        pyautogui.click()


# Opens to site via chrome or select window with Google Hangouts open
# Can be removed if don't want to open with google chrome
if (pyautogui.getWindowsWithTitle('Google Chrome')) == []:
    threadObj = threading.Thread(target=sendingMessages, args=(people, messages))
    threadObj.start()
    webbrowser.get(browserPath).open('https://hangouts.google.com/')

else:
    # Select and maximize browser window
    print('Select window running Google Hangouts')
    pyautogui.sleep(5)
    browser = pyautogui.getActiveWindow()
    sendingMessages(people, messages)

#browser.maximize()

print('Notifications sent')
