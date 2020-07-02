#! python3
#gmailer.py - sends gmails with the first argument being the gmail to send to and second is the msg
import sys, re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
email = sys.argv[1]
password = sys.argv[2]
subject = sys.argv[3]
msg = ' '.join(sys.argv[4:])

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4}))''',re.VERBOSE)

emailSearcher = emailRegex.search(email)

if emailSearcher:

    browser = webdriver.Firefox()
    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')
    emailElem = browser.find_element_by_name('identifier')
    emailElem.send_keys(email)
    emailElem.send_keys(Keys.ENTER)
    time.sleep(3)

    passElem = browser.find_element_by_name('password')
    passElem.send_keys(password)
    passElem = passElem.send_keys(Keys.ENTER)
    time.sleep(5)

    compose = browser.find_element_by_class_name('z0')
    compose.click()
    time.sleep(5)

    recipient = browser.find_element_by_name('to')
    recipient.send_keys(email)

    subjectBox = browser.find_element_by_name('subjectbox')
    subjectBox.send_keys(subject)

    subjectBox.send_keys(Keys.TAB + msg + Keys.TAB)
    time.sleep(5)

    #browser.quit()
else:
    print('No valid email provided.')

