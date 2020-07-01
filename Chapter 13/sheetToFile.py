#! python3
#sheetToFile.py - FileTosheet but reversed

import os, openpyxl

userPath = input('Choose the absolute path where your workbooks reside.\n')
userwb = input('Which workbooks do you choose?\n')

wbList = userwb.split()

try:
    for wb in wbList:
        currentwb = openpyxl.load_workbook(os.path.join(userPath, wb))
        sheet = currentwb.active

        for activeColumn in range(1, sheet.max_column + 1):
            #creates a new txt file for every column
            textFile = open(wb + str(activeColumn) + '.txt', 'w')

            #Takes the value of each cell in the column and writes to text file
            for cell in range(1, sheet.max_row + 1):
                cellValue = str(sheet.cell(row=cell, column = activeColumn).value)
                if cellValue == 'None':
                    textFile.write('\n')
                    continue
                else:
                    textFile.write(cellValue + '\n')

            textFile.close()
    print('All text files have been created')

except:
     print('No such files exist at directory %s' % userPath)



