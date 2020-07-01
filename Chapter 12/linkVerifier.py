#! python3
#linkVerifier.py - downloads every linked page on a page - 404 will be marked not found
import requests, webbrowser, bs4, os
#Downloads original page
url = input('What website links do you want to verify?\n')
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')

#Finds link elements
linkElems = soup.select('a[href]')
#Check if link exists
for i in range(len(linkElems)):
    link = linkElems[i].get('href')
    if link.startswith('http'):
        try:
            linkRes = requests.get(link)
            if linkRes.status_code == 503:
                print('%s found with 503 error (most likely Amazon)' % link)
                continue
            linkRes.raise_for_status()
            print('%s found' % link)

        except Exception as err:
            print('%s not found due to %s' % (link,err))

print('Finished')

