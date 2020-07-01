#! python3
#regexSearch.py - opens text files and searches for any lines that matches user regex

import re
import os
from pathlib import Path

inputRegex = input('What to search for?\n')
userRegex = re.compile(inputRegex)
# tester = userRegex.search('There is an apple right there') works

userDirectory = input('Where is the folder (input path)\n')
userFolder = input('What folder do you want to look through\n')
folderDirectory = os.path.join(userDirectory,userFolder)
textFolders = list(Path(folderDirectory).glob('*.txt'))

for files in os.listdir(folderDirectory):
    currentFile = Path(os.path.join(folderDirectory, files))
    
    if currentFile in textFolders:
        if userRegex.search(currentFile.read_text()):
            print(str(currentFile))

    
    

