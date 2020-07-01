#! python3
#passwordDetection.py - detects if a password is strong or weak
import re

#Strong Password Protection
upCases = re.compile(r'[A-Z]');
lowCases = re.compile(r'[a-z]');
digit = re.compile(r'\d+');
def pwMatch(user):
    if len(user) > 7:
        if upCases.search(user) and lowCases.search(user) and digit.search(user):
            #can use 'if' to identify if variable contains object (in this case Match)
            print('Strong password')
        else:
            print('Weak password')
    else:
        print('Password too short')




userPw = input('What is the password\n')
pwMatch(userPw)


