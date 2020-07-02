#! python3
#forms.py - stores the emails found in the Google Sheet created by Google Forms
import ezsheets
googleSheet = input('What is the id of the Google Sheet?\n')
ss = ezsheets.Spreadsheet(googleSheet)
sheet = ss[0]

emails = []
for rows in range(2, sheet.rowCount + 1):
    emails.append(sheet[3,rows])

textFile = open('emails.txt','w')
for email in emails:
    textFile.write(email + '\n')

textFile.close()
