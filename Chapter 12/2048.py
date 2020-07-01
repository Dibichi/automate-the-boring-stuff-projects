#! python3
#2048.py - plays the game 2048 automatically via web browser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.UP + Keys.RIGHT + Keys.DOWN + Keys.LEFT)
    gameOver = browser.find_element_by_css_selector('.game-container p')
    try:
        if gameOver.is_displayed():
            gameScore = browser.find_element_by_class_name('score-container')
            print('Game Score: ' + gameScore.text)
            retry = browser.find_element_by_class_name('retry-button')
            retry.click()
        continue
    except:
        continue
print('Done')

