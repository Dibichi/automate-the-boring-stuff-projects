#! python3
#regexStrip.py - like strip() method - strips string of whitespaces unless specified

import re

def regexStripper(text, characters = ''):
    if characters == '':
        stripRegex = re.compile(r'\S.*\S')
        return stripRegex.search(text).group()

    else:
        #Matches the characters in the beginning and end of string
        startRegex = re.compile(r'^([%s]+)' % characters)
        endRegex = re.compile(r'([%s]+)$' % characters)
        start = startRegex.search(text)
        end = endRegex.search(text)

        # Uses indexing to subtract the text with matching characters
        try:
            return text[len(start.group()):len(text) - len(end.group())]
        except:
            print('No matching characters found')


userText = input('Write something to strip.\n')

print(userText.strip('space'))
print(regexStripper(userText, 'space'))
