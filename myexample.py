## TIC TAC TOE GAME IN PYTHON

board = ['' for x in range(10)]

def insertletter(letter, pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos]==' '

def printboard(pos):
    print('   |   | ')
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print('' + board[4] + '|' + board[5] + '|' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def iswinner(bo, le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le)or(bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)



def playermove():
    run = True
    while run:
        move = input('Please select a position to place an X --(1-9):')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                    run = False
                    insertletter('X', move)
                else: 
                    print('Sorry, this space is already taken, try another space.')
            else: print('Please type a number between 1 and 9 for your next move.')
        else: print('Please type a number between 1 and 9')

def compmove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possiblemoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if iswinner(boardCopy, letter):
                move = i
                return move

def selectrandom(board):
    pass

def isboardfull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False

def main():
    print('Welcome to Tic Tac Toe!')
    printboard()

    while not(isboardfull(board)):
        if not(iswinner(board, 'O')):
            playermove()
            printboard()
        else: 
            print('Sorry, O\'s won this time.')
            break

        if not(iswinner(board, 'X')):
            move = compmove()
            if move == 0:
                print('Tie Game!')
            else:
                insertletter('O', board)
                print('Computer placed an O in position: ', move,)
                printboard()
        else: 
            print('X\'s won this time! Good job!')
            break

    if isboardfull(board):
        print('Tie Game!')

    

main()
