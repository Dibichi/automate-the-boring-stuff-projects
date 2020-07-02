#! python3
#zombieDiceBots.py - play zombie dice
import zombiedice
import random

class randomAfterFirst:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # Bot decides if it wants to roll after the first roll
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            randNum = random.randint(0,1)
            if randNum == 0:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class stopTwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        
        # Stops rolling if it gets 2 brains
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains != 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class stopsTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll

        # Stops after rolling two shotguns - already included in example
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns != 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class randomRollsUnlessShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll

        # Rolls between 1 - 4 times unless there are two shotguns
        shotguns = 0
        rolls = random.randint(1, 4)

        while rolls > 1:
            if diceRollResults is not None:
                shotguns += diceRollResults['shotgun']
                if shotguns != 2:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
            else:
                break
            rolls = rolls - 1

class moreShotgunsThanBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll

        # Stops rolling after rolling more shotguns than brains
        # I can't tell if this one is really working or not
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            print('shotguns: %s brains: %s' % (shotguns, brains))
            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2\
Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1\
Shotgun', minShotguns=1),
    randomAfterFirst(name='Random after first'),
    # Add any other zombie players here.
    stopTwoBrains(name = 'Stop Two Brains'),
    randomRollsUnlessShotguns(name = 'Random until shotgun'),
    moreShotgunsThanBrains(name = 'More shotguns'),

)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
