#! python 3
# convertSheet.py - converts google sheet into any format that is available

import ezsheets, os, time
from pathlib import Path
import pyinputplus as pyip

#gets user directory and file name
userDirect = input('What directory is the file in?\n')
userInput = input('What file do you want to upload to Google Sheets?\n')

#sets absolute path of file
file = os.path.join(userDirect,userInput)

#Matches naming of uploaded spreadsheet names in google sheets
ssName = userDirect + '\\' + (Path(file).stem) 

#Tests if file can be uploaded
try:
    ezsheets.upload(file)
    print('Uploaded')
except:
    print('Invalid file format')

#Searches list of spreadsheets to match name with an ID
ssDict = ezsheets.listSpreadsheets()
for ids,names in ssDict.items():
    if names == ssName:
        ssId = ids

#Gets Spreadsheet object based off ID
ss = ezsheets.Spreadsheet(ssId)

#Asks users for what format to convert to - will default to whats typed in list if typed differently - ie 'excel' will equal 'Excel'
userFormat = pyip.inputChoice(['Excel','ODS','CSV', 'TSV', 'PDF', 'HTML'] ,prompt = 'What format do you want to convert it to?\n')

#Formats based on what is typed in
if userFormat == 'Excel':
    ss.downloadAsExcel()
elif userFormat == 'ODS':
    ss.downloadAsODS()
elif userFormat == 'CSV':
    ss.downloadAsCSV()
elif userFormat == 'TSV':
    ss.downloadAsTSV()
elif userFormat == 'PDF':
    ss.downloadAsPDF()
elif userFormat == 'HTML':
    ss.downloadAsHTML()

#Deletes from google drive to focus program on only converting
ss.delete(permanent = True)

print('File has been converted')

