#! python3
#tableprinter.py - displays list of lists of strings in a well - organized table

def printTable(lists):
    colWidths = [0] * len(lists)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for nestList in range(len(lists)):
	    for value in range(len(lists[nestList])):
		    if len(lists[nestList][value]) > colWidths[nestList]:
			    colWidths[nestList] = len(lists[nestList][value])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for value in range(len(lists[0])):
	    for nestList in range(len(lists)):
		    print(lists[nestList][value].rjust(colWidths[nestList]), end = ' ')
	    print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
