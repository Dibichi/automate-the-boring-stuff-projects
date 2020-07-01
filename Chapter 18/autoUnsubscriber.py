#! python3
# autoUnsubscriber - automatically unsubscribes from emails
'''
High Level
1. Access all my emails using IMAP
2. Look through all my emails to for emails with an unsubscribe link
3. Opens the browser to the unsubscribe URL

Low Level
1. Login into IMAP with imapclient
2. Loop through each email and get the html part of every email
3. Use bs4 to look parse and look for <a> tags to add to a  list
3.5. Loop through the <a> tags in the list and find the one with 'unsubscribe' in the innerhtml
4. Take the 'href' link from that <a> tag and add it to a list
5. Loop through the list with links and open them using webbrowser.open()
'''

import bs4
import imapclient
import pyzmail
import webbrowser
import threading
import sys

unsubLinks = []

#Logs into IMAP and gets the UIDs of all emails
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
imapObj.login(sys.argv[1], sys.argv[2]) #email and password for email account
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])

# Loops through all email and stores the html parts
rawMessages = imapObj.fetch(UIDs, ['BODY[]']) #creates a nested dictionary with uids as keys
for uid, body in rawMessages.items():

    #creates a unique message object
    message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])

    if message.html_part == None: #checks if there is a HTML part of the message
        continue

    #takes the htmlPart
    htmlPart = message.html_part.get_payload().decode(message.html_part.charset)


    #The parsing of the HTML part and adding of all <a> tags to a list
    soup = bs4.BeautifulSoup(htmlPart, 'html.parser')
    linkElems = soup.select('a')

    #Checks the inner html of all <a> tags and takes its link if its for unsubscribing
    for elems in linkElems:
        innerHtml = elems.getText()
        if 'unsubscribe' == innerHtml.lower():
            unsubLinks.append(elems.get('href'))

#Loops through all unsubscribe links and opens them
for links in unsubLinks:
    webbrowser.open(links)

imapObj.logout()
print('All unsubscribe links have been opened...')



