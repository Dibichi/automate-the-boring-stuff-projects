#! python3
#dateDetection.py - detects dates
import re

#Date Detection
dates = re.compile(r'''
    (((0|1|2)\d)|(3(0|1)))  #Day
    \/                      #separator
    (0\d|1(0|1|2))          #Month
    \/                      #separator
    (1|2)(\d){3}            #Year
    ''', re.VERBOSE);
date = dates.search(input())
print(date.group()) 


