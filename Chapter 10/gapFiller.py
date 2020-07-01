#! python3
#gapFiller - fills in gaps in in naming of files in folder
import re
from pathlib import Path
import shutil
import os

numberRegex = re.compile(r'\d+')
fileNameRegex = re.compile(r'[a-zA-z]+')
nameAndZeroRegex = re.compile(r'(\D+)(0)*')

userFolder = input('What folder do you want to walk through?\n') #input folder path
os.chdir(userFolder)
#os.makedirs('filledGap', exist_ok = True)
fileList = os.listdir(userFolder)
#absCWD = os.path.abspath('.')

for file in fileList:
    #Identify files that has numbers
    fileStem = Path(file).stem
    if numberRegex.search(fileStem) is None:
        continue

    # Checks for series of files
    currentIndex = fileList.index(file)
    try:
        previousFile = fileList[currentIndex - 1]
        previousFileStem = fileNameRegex.search(previousFile).group()

        nextFile = fileList[currentIndex + 1]
        nextFileStem = fileNameRegex.search(nextFile).group()

    except IndexError:
        continue

    noNumberStem = fileNameRegex.search(fileStem).group()
    if (noNumberStem != previousFileStem) or (noNumberStem != nextFileStem):
        continue

    # Find out whether there is a gap in the file series
    # Gets numbers in file stem and changes it to comparable integers
    previousFileStem = Path(previousFile).stem
    nextFileStem = Path(nextFile).stem
    currentNumber = int(numberRegex.search(fileStem).group())
    previousNumber = int(numberRegex.search(previousFileStem).group())
    nextNumber = int(numberRegex.search(nextFileStem).group())

    # Changes file name to fill gap if necessary
    if (currentNumber - 1 == previousNumber) and (currentNumber + 1 == nextNumber):
        continue

    else:
        newStemName = nameAndZeroRegex.search(fileStem).group()
        correctedFileName =  newStemName + str(nextNumber - 1) + Path(file).suffix
        print('Renaming %s to %s...' % (nextFileStem, correctedFileName))
        shutil.move(nextFile, correctedFileName)
        #os.path.join(absCWD, 'filledgap', correctedFileName))

print('Renamed all files')

