#! python3
#passwordBreaker - tries every single english word to decrypt a PDF
import os, PyPDF2

dictionaryLocation = '' #input path to dictionary text file here
dicFile = open(dictionaryLocation)
allWords = dicFile.readlines()

while True:
    try:
        userDir = input('What directory?\n')
        userInput = input("What PDF file would you like to brute force?\n")
        pdfFile = open(os.path.join(userDir, userInput),'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        break
    except:
        continue

for word in allWords:
    word = word.strip()
    lowerCase = word.lower()
    upperCase = word.upper()
    if pdfReader.decrypt(lowerCase) == 1:
        print('%s is the password' % lowerCase)
        break
    elif pdfReader.decrypt(upperCase) == 1:
        print('%s is the password' % upperCase)
        break
print('Done')


