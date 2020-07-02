#! python3
import time, pyperclip
#improvedStopwatch.py
#Display prrogram's instructions
print('Press ENTER to begin. Afterward press ENTER to "click the stopwatch. Press CTRL-C to quit.')

input() #press enter to begin

print('Started.')

#Setting up
startTime = time.time()
lastTime = startTime
lapNum = 1

#Start tracking the lap times
try: #handles in event of CTRL - C
    while True:
        input()
        lapTime = round(time.time() - lastTime,2) #subtracts from lastTime for laps
        totalTime = round(time.time() - startTime,2) #subtracts from startTime for total
        lapPrint =  'Lap #' + str(lapNum) + ':'
        timePrint = str(totalTime) + ' (' + str(lapTime) + ')'
        fullPrint = lapPrint.ljust(8) + timePrint
        print(fullPrint,end = '')
        pyperclip.copy(fullPrint)
        #prints lap number, total time, and lap time - end = '' keeps from double spacing since default is \n
        lapNum += 1
        lastTime = time.time() #resets lap time - new lap

except:
    #Handles the CTRL-C to keep error message from displaying - not working with mu
    print('\nDone.')
