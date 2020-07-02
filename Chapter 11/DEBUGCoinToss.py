#! python3
#Fix with debugger
import random
'''guess = ''
while guess not in ('tails', 'heads'): #ask for heads or tails until entered
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess: #toss is in numbers (0 and 1) while guess is in string form (heads or tails)
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input() #misspelled guess
    if toss == guess: #same as last time
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')'''

#Fixed code

guess = ''
flip = ('tails','heads')
while guess not in flip:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if flip[toss] == guess: #toss is in numbers (0 and 1) while guess is in string form (heads or tails)
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input() #misspelled guess
    if flip[toss] == guess: #same as last time
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
