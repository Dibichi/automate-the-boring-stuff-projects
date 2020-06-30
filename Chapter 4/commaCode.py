#! python3
#commaCode.py - turns into a string separated by a comma and space with and at the end

def listToString(someList):
    converted = ' '
    for i in range(len(someList)-1):
        converted += someList[i] + ', '
    converted += 'and ' + someList[-1]
    return converted

spam = ['apples', 'bananas', 'tofu', 'cats', 'potatoes']
print(listToString(spam))
