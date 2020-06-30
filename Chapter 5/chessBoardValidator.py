# Write your code here :-)
#chessBoardValidator.py - function for validating if a dictionary is a valid chess board

def isValidChessBoard(board):
    validPieces = {'wking':1,'bking':1,'wqueen':1,'bqueen':1,'wbishop':2,'wrook':2,'wknight':2,'bbishop':2,'brook':2,'bknight':2,'bpawn':8,'wpawn':8}
    validPositions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pieceCount={'wking':0,'bking':0,'wqueen':0,'bqueen':0,'wbishop':0,'wrook':0,'wknight':0,'bbishop':0,'brook':0,'bknight':0,'bpawn':0,'wpawn':0}

    # Checks if positions are valid on inputted board
    for position in board.keys():
        if ((int(position[0]) < 1) or (int(position[0]) > 8) or (position[1] not in validPositions)):
            print('%s is an invalid position' % position)
            return False


    for piece in board.values():

        #Checks if a piece is valid
        if piece not in validPieces.keys():
            print('%s is an invalid piece' % piece)
            return False

        pieceCount[piece] += 1

        #Checks if there are too many of one piece
        if pieceCount[piece] > validPieces[piece]:
            print('Too many %s on the board' % piece)
            return False

    return True

print(isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','9a':'bpawn'}))
print(isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','8a':'bpawn'}))
print(isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '6e': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','8a':'bpawn'}))
