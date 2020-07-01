#! python3
#collatz.py - keeps running until user integer equals one - Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        new= number//2
        print(str(new))
        return new
    elif number %2 ==1:
        newone = number * 3 + 1
        print(str(newone))
        return newone

userNum = input('Enter a number\n')
numCollatz = collatz(int(userNum))

while numCollatz != 1:
    numCollatz = collatz(numCollatz)

