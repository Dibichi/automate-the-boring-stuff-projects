#! python3
#umbrellaReminder - reminds someone to bring an umbrella if its raining via email
#will try to use SMS in the future

import smtplib
import bs4
import requests
import os
import sys

#location of weather
locationUrl = 'url'

#The parsing and identifying of weather
res = requests.get(locationUrl)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
weatherElem = soup.select('div.row-odd:nth-child(1) > div:nth-child(2)')[0]
weather = weatherElem.getText()
dayElem = soup.select('div.row-odd:nth-child(1) > div:nth-child(1)')[0]
day = dayElem.getText()

def smtpLogin(email,password):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email,password)
    myEmail = email
    return smtpObj, myEmail

if 'showers' in weather.lower():
    bodyText = 'Subject:Bring an umbrella\nThe weather for %s is\n%s' % (day.lower(), weather)
else:
    bodyText = 'Subject:Weather for %s\nThe weather for %s is\n%s' % (day.lower(), day.lower(), weather)

smtpObj, myEmail = smtpLogin(sys.argv[1], sys.argv[2])

print('Sending an email to %s from %s' % (myEmail, myEmail))
emailStatus = smtpObj.sendmail(myEmail, myEmail, bodyText)
if emailStatus != {}:
    print('There was a problem sending email to %s: %s' % (myEmail,emailStatus))
smtpObj.close()

print('Done')
