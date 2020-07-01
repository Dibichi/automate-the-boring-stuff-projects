#! python3
#madLibs.py - reads text files and lets user adjust text 
'''
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:
'''

def madLibs(file):
    fileString = file.read_text() #reads the text file that contains the string
    partSpeech = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB') #regex that looks for part of speech

    while True: #loops through to find every instance of the regex
        result = partSpeech.search(filestring)  #result is equal to adj,noun,verb,or adv that is found in the string

        if result == '':  #if .search didn't find anything loop is broken and a blank file is created
            break

        if result.group() == 'ADJECTIVE' or result.group() == 'ADVERB': #if the string returned from .group is adj or adv
            print('Pls enter a %s: ' % (result.group().lower()) #prompts user to enter an adj or adv

        elif result.group() == 'Noun' or result.group() == 'Verb': #if the string returned from .group is noun or verb
            print('Pls enter a %s: ' % (resultgroup().lower()) #prompts user to enter a verb or noun

        i = input() #gets user input for what to replace the detected  part of speech is

        fileString = partSpeech.sub(i,fileString,1) #i = replacement, fileString = string where the regex will replace partrs of, 1 = searches for one word at once
                  

print(fileString) #prints the new fileString

print('Name file') #prompts user to name file

nameFile = input()

newFile = open("..\\%s.txt" % (nameFile),'w') #creates a new file with that name and writes the new string
newFile.write(fileString)
                  
        
    
    
    
