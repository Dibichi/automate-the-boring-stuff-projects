#! python3
#randomChoreEmailer - randomly selects an email from a list and send an email with a chore
#FOR GMAIL
'''
High Level:
1. Have a list of emails and chores to choose from
2. Randomly assign a chore to each email
2.5. Check if the email has done the chore last week
3. Write a custom message for the email
4. Log into the email - possibly on another thread
5. Send the email containing the message to the recipient
'''

'''
Low Level:
1. Write a list of emails and chores
2. Use a loop to assign each member a chore
2.5. Use a shelve file to check if email has done chore last week
3. Write variables for a custom message and different email for each iteration
4. Follow the SMTP login process and send the email
'''

import smtplib, shelve, os, threading, random, sys
userDirectory = input('Choose a directory to place your shelve file...\n')
os.chdir(userDirectory)
shelfFile = shelve.open('choreEmails')
emails = ['example@gmail.com','example1@gmail.com','example2@gmail.com'] #change example emails to recipients' email
chores = ['wash the dishes','mow the lawn', 'feed the cat', 'clean the living room', 'vacuum the floor'] # some chores - can be changed

def smtpLogin(email,password):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email,password)
    myEmail = email
    return smtpObj, myEmail

smtpObj, myEmail = smtpLogin(sys.argv[1], sys.argv[2]) #email and password for gmail account

for email in emails:

    #The chore choosing part for the email
    randomChore = random.choice(chores)
    if email in list(shelfFile):
        while shelfFile[email] == randomChore: #makes sure the chore is not the same as last time
            randomChore = random.choice(chores)
    shelfFile[email] = randomChore # stores the chore as the value to the email
    chores.remove(randomChore)    # this chore is now taken, so remove it

    #The custom email message
    choreText = 'Subject: %s\nYour chore this week is to %s.' % (randomChore,randomChore)

    #Sending the email
    print('Sending an email to %s from %s' % (email,myEmail))
    emailStatus = smtpObj.sendmail(myEmail, email, choreText)
    if emailStatus != {}:
        print('There was a problem sending email to %s: %s' % (email,emailStatus))

smtpObj.close()
shelfFile.close()
print('All emails have been sent!')


