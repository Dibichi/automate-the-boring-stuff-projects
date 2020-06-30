#! python3
#coinFlip.py - flips a coin 1000 times and prints the percent of streaks of 6
import random
numberOfStreaks = 0
flipList = []
lastCoin = ''
streak = 0

for experimentNumber in range(1000):
    coin = random.randint(0,1)
    if coin == 0:
        flipList.append('H')
    else :
        flipList.append('T')

    if coin == lastCoin:
        streak += 1
    else:
        streak = 0

    lastCoin = coin

    if streak == 6:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
