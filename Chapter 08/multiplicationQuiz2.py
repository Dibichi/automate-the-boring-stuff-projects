#! python3
#multiplicationQuiz.py - creates a multiplication quiz

import pyinputplus as pyip
import random,time

#Project 2: Multiplication Quiz
numberQuestions = 10
correctAnswers = 0
for questionNumber in range(numberQuestions): #questionNumber keeps track of what question we are on out of ten
    #picks 2 random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber,num1,num2) #does not have to be %s can be %d,%q, etc.
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], #%s is equal to the answer
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=8, limit=3)
        #if input != answer then it will say incorrect and prompt the user to enter another input

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    #Raises a timeout or retry limit Exception if input took more than 8 seconds or 3 tries
        
    else:
        #else can follow except just like if
        # This block runs if no exceptions were raised in the try block. - answer was correct
        print('Correct!')
        correctAnswers += 1
        time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberQuestions))
#%s is used as filler and requires % followed by the actual variables in paranthesis
