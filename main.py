from itertools import cycle

# First I make the board
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


# prints board
def printBoard(board):
    l = '|'
    print(board['7'] + l + board['8'] + l + board['9'])
    print('-+-+-')

    print(board['4'] + l + board['5'] + l + board['6'])
    print('-+-+-')

    print(board['1'] + l + board['2'] + l + board['3'])


def tictactoeGame():
    turn = 'X'
    count = 0
    players = 'Player 1'

    while count < 10:
        # print current board
        printBoard(theBoard)
        print(f'It\'s your turn, {players}. What is your move using the number pad?')

        move = input()

        # Check move validity
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Invalid move either position DNE or is taken")

        # Check for winner
        if count >= 5:

            # check for row victory
            if theBoard['7'] == theBoard['8'] == theBoard['9'] and theBoard['7'] != ' ':
                print(f'{players} has won')
                break

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] and theBoard['4'] != ' ':
                print(f'{players} has won')
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] and theBoard['1'] != ' ':
                print(f'{players} has won')
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] and theBoard['4'] != ' ':
                print(f'{players} has won')
                break
                # check for column victory
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] and theBoard['7'] != ' ':
                print(f'{players} has won')
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] and theBoard['8'] != ' ':
                print(f'{players} has won')
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] and theBoard['9'] != ' ':
                print(f'{players} has won')
                break
            # check for diagonal victory
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] and theBoard['7'] != ' ':
                print(f'{players} has won')
                break
            elif theBoard['9'] == theBoard['5'] == theBoard['1'] and theBoard['9'] != ' ' :
                print(f'{players} has won')
                break

        if count == 9:
            print('Tie Game !!!')

        if turn == 'X':
            turn = 'O'
            players = 'Player 2'
        else:
            turn = 'X'
            players = 'Player 1'


tictactoeGame()
