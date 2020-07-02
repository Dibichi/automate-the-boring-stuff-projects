#! python3
#gapFiller - fills in gaps in in naming of files in folder
# May have to refresh file explorer to see correct results
import re
from pathlib import Path
import shutil
import os

#Matches the stem of files
fileNameRegex = re.compile(r'(([a-zA-z]+)0*)(\d+)')

userFolder = input('What folder do you want to walk through?\n') #input folder path
os.chdir(userFolder)
#os.makedirs('filledGap', exist_ok = True)
#absCWD = os.path.abspath('.')

# Loops until all discrepancies are fixed
while True:
    fileSeries = {} # dictionary for series of files
    fileList = os.listdir(userFolder) # files in directory
    changes = 0 # for checking if any discrepancy were fixed

    # Finds files with numbers
    for file in fileList:
        fileStem = Path(file).stem
        if fileNameRegex.search(fileStem) is None:
            continue

        # Puts stem of file as key and list of files with same stem as key as value
        noNumberStem = fileNameRegex.search(fileStem).group(2)
        if noNumberStem in fileSeries.keys():
            fileSeries[noNumberStem].append(file)
        else:
            fileSeries.setdefault(noNumberStem, [file])

    # Loops through all series of files
    for series in fileSeries.values(): # eliminates keys with only one value
        if len(series) == 1:
            continue

        print(series) #removeable - keeps track of what file series looks like

        for file in series: # for each file in a series of files
            # All the needed components for the current file
            currentIndex = series.index(file)
            currentNumber = int(fileNameRegex.search(file).group(3))
            newStemName = fileNameRegex.search(file).group(1)
            
            # Gets the number of the next file and its stem
            try:
                nextFileStem = Path(series[currentIndex + 1]).stem
                nextNumber = int(fileNameRegex.search(nextFileStem).group(3))
               
            # Handles Index Error when it reaches last file in series
            except IndexError: 
                continue
                
            # Checks if numbered correctly
            if (currentNumber + 1 == nextNumber):
                continue
            
            # Naming and fixing of file name
            else:
                correctedFileName =  newStemName + str(currentNumber + 1) + Path(file).suffix
                print('Renaming %s to %s...' % (nextFileStem, correctedFileName))
                shutil.move(series[currentIndex + 1], correctedFileName)
                changes += 1
                #os.path.join(absCWD, 'filledgap', correctedFileName))

    if changes == 0: # No changes were made = everything was renamed properly
        break
    
print('Renamed all files')
