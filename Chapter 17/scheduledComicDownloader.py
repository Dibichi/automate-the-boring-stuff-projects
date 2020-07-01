#! python3
#scheduledComicDownloader - checks comic websites if there is a new comic
'''
Higher level
1. Download webpage and identify the comic image url
2. Take and store image url
3. If image url is not the same download otherwise skip and display message
'''

'''
Lower Level
1. Ask user to input website URL
2. Make a folder for comics
3. Download the webpage with request module and parse it with Beautiful Soup
4. Use the same element select parameters as xkcd (see downloadskcd.py) to get imageUrl
5. Check if imageUrl exists in shelf file - save it if doesnt exit or skip if it doesnt
6. If matches shelf url matches - skip it - otherwise download to folder
'''

import bs4, requests, os, shelve

userDirectory = input('Choose a directory to download the comics...\n')
os.chdir(userDirectory)
os.makedirs('comics', exist_ok = True)

#The checking and downloading of comic
def comicDownload(url):

    #Downloads webpage and identifies if comic image exists
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser') #turns into BeautifulSoup object
    comicElem = soup.select('#comic img') #element id is comic and img tag is within element
    if comicElem == []:
        print('Could not find comic image or comic image url could not be identified')

    else:
        comicUrl = comicElem[0].get('src')

        #Checks if comic has already been downloaded in shelf
        shelfFile = shelve.open('comicUrls')
        if comicUrl in shelfFile.values():
            print('The latest comic from the website has already been downloaded previously')

        else:

            #Saves comicUrl to shelfFile
            shelfFile[url] = comicUrl

            #Downloading image and writing to file
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()
            imageFile = open(os.path.join('comics',os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    print('Finished')

#Asks and checks web page url
while True:
    try:
        userUrl = input('What comic page do you want to go to? (enter URL)\n')
        res = requests.get(userUrl)
        res.raise_for_status()
        break
    except:
        print('The url %s is invalid. Try again.' % (userUrl))


comicDownload(userUrl)





