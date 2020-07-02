#! python3
#imageDownloader - downloads images based on inputted term on Imgur
import requests, webbrowser, bs4, os
import pyinputplus as pyip
imagePage = 'https://imgur.com/search/score?q='
os.makedirs('searchImages',exist_ok =True) #exist_ok = True b/c if False will raise exception if duplicate folder

while True:
    #Take the user input and downloads the searched page
    userSearch = input('What do you wish to download?\n')
    searchTerm = '+'.join(userSearch.split())
    res = requests.get(imagePage + searchTerm)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #Checks if there are any matching images
    linkElems = soup.select('.post img')
    if linkElems ==[]:
        print('Could not find image matching search term')

    #Makes a new folder w/ user inputted search term and downloads images
    else:
        userFolder = os.path.join('searchImages', userSearch)
        os.makedirs(userFolder, exist_ok = True)

        #Determines how many images are downloaded
        userAmount = int(pyip.inputNum('How many images would you like to download?\n'))
        downloadImg = min(userAmount,len(linkElems))
        if len(linkElems) < userAmount:
            print('There were less than %s images found' % userAmount)

        print('Downloading %s images...' % downloadImg)

        #Writes downloaded images onto hard drive
        for i in range(downloadImg):
            imgUrl =  'https:' + linkElems[i].get('src')
            print('Downloading image %s   ' % imgUrl)
            res = requests.get(imgUrl)
            res.raise_for_status()
            imageFile = open(os.path.join(userFolder,os.path.basename(imgUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    #Asks if user wants to search for anything else
    response = pyip.inputYesNo('Do you want to search for something else?\n')
    if response == 'yes':
        continue
    else:
        break

print('Done')


