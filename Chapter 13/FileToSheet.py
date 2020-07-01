#! python3
# FileToSheet - text in text file converted to excel sheets

import os, openpyxl, pyinputplus as pyip

wb = openpyxl.Workbook()
sheet = wb.active
columnValue = 1

while True:
    try:
        userDirectory = input('Where is the text file?\n')
        userInput = input("What text file would you like to covert?\n")
        txtFile = open(os.path.join(userDirectory, userInput))
    except:
        continue

    content = txtFile.readlines()

    counter = 0

    for lines in content:
        counter += 1
        sheet.cell(row=counter, column=columnValue).value = lines

    columnValue += 1

    keepGoing = pyip.inputYesNo('Do you want to keep converting\n')
    if keepGoing == 'no':
        break

wb.save('filetosheet.xlsx')
print('Finished')
