# milesone 1 includes

def display_board(board):
    clear_output()
    print('     |     |     ')
    print('  '+ board[0][0] + '  |  ' + board[0][1] + '  |  ' + board[0][2] + '  ')
    print('     |     |     ')
    print('=================')
    print('     |     |     ')
    print('  '+ board[1][0] + '  |  ' + board[1][1] + '  |  ' + board[1][2] + '  ')
    print('     |     |     ')
    print('=================')
    print('     |     |     ')
    print('  '+ board[2][0] + '  |  ' + board[2][1] + '  |  ' + board[2][2] + '  ')
    print('     |     |     ')


def playerattributes():
    xoro = ''
    xoro2 = ''
    player1 = {"name": '', "assignment": ''}
    player2 = {"name": '', "assignment": ''}

    player1name = input(print("What is player 1's name?: "))
    while xoro not in ['X', 'O']:
        xoro = input(print("Will you be X or O?")).upper()
        if xoro not in ['X', 'O']:
            print("Invalid input, try again")
    xoro = xoro.upper()
    
    if xoro == 'X':
        xoro2 = 'O'
    else:
        xoro2 = 'X'

    player2name = input(print("What is player 2's name?: "))
    
    player1["name"], player1["assignment"], player2["name"], player2["assignment"] = player1name, xoro, player2name, xoro2
    print(player1)
    print(player2)

    whosefirst = int(input(print("Who is going first? Enter \"1\" or \"2\": ")))
    currentplayer = ''
    if whosefirst == 1:
        currentplayer = player1
    else:
        currentplayer = player2
    print(f'Alright {currentplayer["name"]}, you are assigned "{currentplayer["assignment"]}" and it\'s your turn!')
    print('enter the number correcponding with your move: ')
    print('1 | 2 | 3')
    print('---------')    
    print('4 | 5 | 6')
    print('---------')    
    print('7 | 8 | 9')
    return currentplayer, player1, player2