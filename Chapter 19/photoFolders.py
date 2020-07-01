#! python3
#photoFolders - searches through folders in drive to look for
#leftover digital photos

from PIL import Image
from pathlib import Path
import os

userDirectory = '' #choose a directory you want to search for leftover photos in

for foldername, subfolders, filenames in os.walk(userDirectory): 
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        filenameLower = filename.lower()

        # Check if file extension isn't .png or .jpg.
        if not ((filenameLower.endswith('.png')) or (filenameLower.endswith('.jpg'))):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        #print(os.path.join(foldername, filename))
        img = Image.open(os.path.join(foldername, filename))
        width,height = img.size

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))
