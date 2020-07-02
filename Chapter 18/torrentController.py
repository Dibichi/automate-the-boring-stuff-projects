#! python3
#torrentController - downloads torrents through emails and sends email when finished

#Will download any torrent link as long as email subject is 'torrents'
#and torrents are seperated by a new line

#There may be issues for emailing when torrent program is closes

'''
High Level
1. Check email for files with torrents
2. Open the torrents in qBittorent
3. Wait for all torrents to finish and send an email when finished

Low Level
1. Check emails with attachments with IMAPClient module
2. Check if email is from me and is a .tor file
3. Download the file and open with Popen in qBittorent
4. Wait for torrent to download and wait 15 min
'''

import threading
import imapclient
import smtplib
import pyzmail
import logging
import traceback
import subprocess
import time
import re
import os
import sys

logging.basicConfig(filename='torrentStarterLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

email = 'example@ex.com' #your email that you want to send a notification to
imapServer = 'imap.gmail.com' #your imap server
torRegex = re.compile(r'magnet:\?\S*') #regex for identifying magnet links
torrentProgram = 'C:\Program Files\qBittorrent\qbittorrent.exe' #location of torrent program

# Logins into SMTP
def smtpLogin(email,password):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email,password)
    myEmail = email
    return smtpObj, myEmail

#Looks for torrent files in email
def emailSearch(password):
    downloadTorrents = []
    deleteUIDs = []
    #Finds all emails sent by me
    logging.debug('Logging into IMAP server: %s' % imapServer)
    print('Logging into IMAP server: %s' % imapServer)
    imapObj = imapclient.IMAPClient(imapServer, ssl = True)
    imapObj.login(email, password)
    logging.debug('Connected')
    imapObj.select_folder('INBOX', readonly = False)
    uids = imapObj.search(['FROM', email])


    for uid in uids:
        rawMessage = imapObj.fetch(uid, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY[]'])
        try:
            if message.text_part == None: #checks if there is a HTML part of the message
                emailText = message.html_part.get_payload().decode(message.html_part.charset)
            else:
                emailText = message.text_part.get_payload().decode(message.text_part.charset)
        except:
            continue
        #Checks if there is torrent in email and adds them to download list
        torrents = torRegex.findall(emailText)

        #Checks if the subject is 'torrents' to include more torrent formats
        if 'torrents' == (message.get_subject()).lower():
            lines = emailText.split('\n') #splits text into lines
            for magnet in lines:

                #skips subject line and adds magnet links separated by new lines
                if magnet.startswith('Subject:') is False :
                    torrents.append(magnet)

        if torrents == []:
            continue

        #Adds all found torrents into 'downloadTorrents'
        for match in torrents:
            print('%s added to download list' % match)
            logging.debug('%s added to download list' % match)
            downloadTorrents.append(match)

        deleteUIDs.append(uid)

    #Logs out and deletes messages
    imapObj.delete_messages(deleteUIDs)
    imapObj.logout()

    return downloadTorrents


# Sends email with SMTP about torrents
def torrentEmailer(torrentsDownloaded, finish):
    #Creates the actual text - body will be each torrent link followed by a new line
    if finish == 'downloading':
        bodyText = 'Subject: Torrents are downloading\nThe following torrents are being downloaded\n'
    elif finish == 'done':
        bodyText = 'Subject: Torrents have finished\nThe following torrents are done downloading\n'

    for torrent in torrentsDownloaded:
        bodyText = bodyText + torrent + '\n'

    #The logging in and sending of email
    smtpObj, myEmail = smtpLogin(email, sys.argv[1])
    print('Sending an email to %s from %s' % (myEmail, myEmail))
    logging.debug('Sending an email to %s from %s' % (myEmail, myEmail))
    emailStatus = smtpObj.sendmail(myEmail, myEmail, bodyText)
    if emailStatus != {}:
        logging.debug('There was a problem sending email to %s: %s' % (myEmail,emailStatus))

    smtpObj.close()

def torrentDone(torrentsDownloaded, status):
    whenClosed = status.wait()
    if whenClosed == 0:
        torrentEmailer(torrentsDownloaded, 'done')
        print('Torrents have finished downloading')
        logging.debug('Torrents have finished downloading')

#The continous checking of emails
print('Starting torrent email program')
logging.debug('Starting torrent email program')
while True:
    try:
        allTorrents = emailSearch(sys.argv[1])
        if allTorrents != []:
            torrentStatus = subprocess.Popen(torrentProgram)
            threadObj = threading.Thread(target=torrentDone, args = (allTorrents, torrentStatus))
            threadObj.start()
            for torrent in allTorrents:
                torrentStatus = subprocess.Popen(torrentProgram + ' ' + torrent)
            torrentEmailer(allTorrents, 'downloading')
    except Exception as err:
        logging.error(traceback.format_exc())
        print(traceback.format_exc())

    # Wait 15 minutes before checking again
    logging.debug('Refreshing in 15 minutes.')
    print('Refreshing in 15 minutes...')
    time.sleep(900)


