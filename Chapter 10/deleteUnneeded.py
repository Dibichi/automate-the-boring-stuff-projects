#! python3
#deleteUnneeded - walks through folder and prints files larger than 100MB
import re,os,shutil
from pathlib import Path

'''walks through a folder tree and searches for exceptionally large files or folders—say,
ones that have a file size of more than 100MB.
 from the os module.) Print these files with their absolute path to the screen.'''

userFolder = input('What folder do you want to walk through?\n')

for folderName, subfolders, filenames in os.walk(userFolder):

    for filename in filenames:
        filesize = os.path.getsize(os.path.join(folderName,filename))
        if filesize > 100000000:
            print(os.path.abspath(os.path.join(folderName,filename)))
