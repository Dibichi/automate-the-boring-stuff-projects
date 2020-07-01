#! python3
#extendedClipboard.py - extended version of the same clipboard made this chapter

'''Here’s what the program does:

    The command line argument for the keyword is checked.
    If the argument is save, then the clipboard contents are saved to the keyword.
    If the argument is list, then all the keywords are copied to the clipboard.
    Otherwise, the text for the keyword is copied to the clipboard.

This means the code will need to do the following:

    Read the command line arguments from sys.argv.
    Read and write to the clipboard.
    Save and load to a shelf file.'''

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys #pyperclip for copy and paste, sys for command line arguments, shelve - where txt is saved  and loaded
mcbShelf = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
    else:
        pyperclip.copy(f'{sys.argv[2]} does not exist')

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list': #user inputs 'list' as second argument 
        pyperclip.copy(str(list(mcbShelf.keys())))  # A string representation of the list of shelf keys will be copied to the clipboard

    elif sys.argv[1] in mcbShelf:           #if users second argument is in the shelf 
        pyperclip.copy(mcbShelf[sys.argv[1]]) #Whatever value that equals to the key that the user inputted - the value will be copied to the user's clipboard
        
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()

        
        
