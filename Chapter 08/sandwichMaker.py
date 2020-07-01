#! python3
#sandwichMaker.py - creates a custom sandwich using pyinputplus module

import pyinputplus as pyip
'''
    Using inputMenu() for a bread type: wheat, white, or sourdough.
    Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
    Using inputYesNo() to ask if they want cheese.
    If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
    Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
    Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.'''
cost = 0
breadTypePrices = {'wheat':1,'white':1,'sourdough':1}
proteinTypePrices = {'chicken':2,'turkey':2,'ham':1.5,'tofu':1.5}
cheeseTypePrices = {'cheddar':.5,'Swiss':1,'mozzarella':.5}

breadType = pyip.inputMenu(['wheat','white','sourdough'], prompt = 'What type of bread you want?\n')
cost += breadTypePrices.get(breadType,0)

proteinType = pyip.inputMenu(['chicken','turkey','ham','tofu'], prompt = 'Protein?\n')
cost += proteinTypePrices.get(proteinType,0)

cheeseYesNo = pyip.inputYesNo('You want cheese?\n')
if cheeseYesNo == 'yes':
    cheeseType = pyip.inputMenu(['cheddar','Swiss','mozzarella'], "What type of cheese?\n")
    cost += cheeseTypePrices.get(cheeseType,0)

mayoYesNo = pyip.inputYesNo('You want mayo?\n')
if mayoYesNo == 'yes':
    cost += .25

mustardYesNo = pyip.inputYesNo('You want mustard?\n')
if mustardYesNo == 'yes':
    cost += .25

lettuceYesNo = pyip.inputYesNo('You want lettuce?\n')
if lettuceYesNo == 'yes':
    cost += .25

tomatoYesNo = pyip.inputYesNo('You want tomato?\n')
if tomatoYesNo == 'yes':
    cost += .25

sandwichCount = pyip.inputInt(min = 1, prompt = 'How many sandwiches do you want?\n')

totalCost = sandwichCount * cost
print('Your total is : $' + str(totalCost))
