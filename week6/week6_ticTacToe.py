theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])




turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input() # need to check if the move is valid. if not, ask again
    theBoard[move] = turn # updating position with X or O
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# 1. thing to do is decide who won the game
# 2. have larger board area
# 3. have a computer player
# 4. add board position validation
# 5. use while and break to make the game loop

s = """
practice project
- tic tac toe
- 2 players
- 3x3 board
- X and O
- X goes first
- X and O alternate turns
- X and O can only go on empty spaces
- if a player gets 3 in a row, they win
- if all spaces are filled and no player has 3 in a row, it's a tie
"""
print(s)