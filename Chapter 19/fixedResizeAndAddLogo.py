#! python3
#fixedresizeAndAddLogo.py - resizes all images in cwd to fit
#in a 300x300 square and adds catlogo.png to lower-right corner with all the fixes

import os
from PIL import Image

#Changeable values
os.chdir('') #put logo image file path here
squareFitSize = 600 #change size of picture
logoName = 'image.png' #put logo image file here
logoImg = Image.open(logoName)
logoWidth, logoHeight = logoImg.size
os.makedirs('withLogo', exist_ok=True)

#Loop over all files in cwd
for filename in os.listdir('.'):
    filenameLower = filename.lower()
    if not (filenameLower.endswith('.png') or filenameLower.endswith('.jpg')\
    or filenameLower.endswith('.gif') or filenameLower.endswith('.jpeg'))\
    or filename == logoName: #checks if not .png, .jpg, or logo file
        continue

    img = Image.open(filename)
    width,height = img.size

    #Checks if image needs to be resized
    if width > squareFitSize and height > squareFitSize:

        #calculate th enew width and height to resize to
        if width > height:
            height = int((squareFitSize/width) * height) #square/width gets proportion or ratio
            width = squareFitSize

        else:
            width = int((squareFitSize/height) * width) #has to be int b/c of resize()
            height = squareFitSize

        print('Resizing %s...' % (filename))
        img = img.resize((width, height))

    #Resizes logo to be half the size of the image
    if (logoWidth * 2) > width and (logoHeight * 2) > height:
        print('%s is too small' % filename)
        continue

    # Add the logo
    print('Adding logo to %s...' % (filename))
    #calculates for top left of image
    img.paste(logoImg,(width - logoWidth, height - logoHeight), logoImg)
    img.save(os.path.join('withLogo',filename))
