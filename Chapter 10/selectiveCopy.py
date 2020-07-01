#! python3
#selectiveCopy - walks through a folder  and searches for certain extension files

from pathlib import Path
import os, shutil
def copier(folder, fileType):
    
    for foldername, subfolders, filename in os.walk(folder):
        
        foldername = Path(foldername)
        
        for file in foldername.glob('*' + fileType):
            shutil.copy(file, 'Copied')
        for file in subfolders:
            fullFile = Path(os.path.join(foldername,file))
            for filePath in fullFile.glob('*' + fileType):
                shutil.copy(filePath, 'Copied')

userDirectory = input('What directory is the folder in?\n')
os.chdir(userDirectory)
os.makedirs('Copied', exist_ok = True)
userFolder = input('What folder do you want to walk through?\n')
copyFile = input('What type of files do you want to copy? (.txt)\n')
copier(userFolder, copyFile)
