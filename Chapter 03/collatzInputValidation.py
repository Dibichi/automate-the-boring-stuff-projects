#! python3
#collatzInputValidation.py - collatz.py but with try and except for user input

def collatz(number):
    if number % 2 == 0:
        new= number//2
        print(str(new))
        return new
    elif number %2 ==1:
        newone = number * 3 + 1
        print(str(newone))
        return newone

while True:
    try:
        userNum = input('Enter a number\n')
        numCollatz = collatz(int(userNum))
        break
    except ValueError:
        print('Input must be a number')

while numCollatz != 1:
    numCollatz = collatz(numCollatz)
