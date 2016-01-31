        ########################################################
        # This function displays the game board on the screen. #
        ########################################################

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#


    #########################################################################
    # This function checks the tic-tac-toe board to determine if the player #
    # stored in variable 'player' currently has a winning position on the   #
    # board.                                                                #
    # This function returns True if the player specified in variable        #
    # 'player' has won. The function should return False if the player in   #       
    # the variable 'player' has not won.                                    #
    #########################################################################    

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...(not sure why you should know this)')
    if board['top-L'] == player and board['top-M'] == player and board['top-R'] == player:
        return True
    elif board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player:
        return True
    elif board['low-L'] == player and board['low-M'] == player and board['low-R'] == player:
        return True
    elif board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player:
        return True
    elif board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player:
        return True
    elif board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player:
        return True
    elif board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player:
        return True
    elif board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player:
        return True
    else:
        return False


#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#


    
    ########################################################################
    # This is the main (game) function. It is called by the runner.py file #
    ########################################################################   

    
def startGame(startingPlayer, board):

    turn = startingPlayer
    #This assignes the choice for the first player 'X' or 'Y' (which is entered when the function
    #is called in the runner.py file) to the variable 'turn'.
    for i in range(9):
    #Loop will run 10 times. First time to display starting-empty board + 9 times for all
    #possible turns (spaces to mark) in game
        printBoard(board)
        #Calls printBoard() function so to visually display board with current
        #items for each key in 'board' dictionary (displays X and O positions)
        print('Turn for ' + turn + '. Move on which space?')
        #Displays message requesting current player to select a space to mark 
        move = input()
        #Assignes player's choice to the variable 'move'
        
        while board[move] != ' ':
        #This loops will be entered if player selects a spot that had already been marked
        #This loop will be exited once player selects a valid spot (one that had not already
        #been selected.)
            print('This spot is already marked. Please select a different move.')
            #Displays a message notifying the player that he'd selected a spot that's already
            #marked and asks player to re-select
            move = input()
            #Assignes player's new choice to the variable 'move'

        board[move] = turn
        #Assignes the current player's letter ('X' or 'O') as the item for the key in the 'board'
        #dictionary that matches the player's selection.
        if( checkWinner(board, 'X') ):
        #Calls and uses checkWinner function to identify if dictionary currently has
        #three keys that have the item 'X' that are in one row
        #(horizinal, vertical or diagonal)
            print('X wins!')
            #If above condition is true, displays message that X won.
            break
            #With an announced winner, the checking function is exited.
        elif ( checkWinner(board, 'O') ):
        #Calls and uses checkWinner function to identify if dictionary currently has
        #three keys that have the item  'O' that are in one row
        #(horizinal, vertical or diagonal)
            print('O wins!')
            #If above condition is true, displays message that O won.
            break
            #With an announced winner, the checking function is exited.
               
        if turn == 'X':
        #Checks if the current value for 'turn' is 'X' (if the current player is 'X')
            turn = 'O'
            #If so, re-assignes the value for 'turn' to 'O' to switch between the two players.
        else:
        #If current player wasn't 'X' then he must be 'O'
            turn = 'X'
            #If so, this re-assignes the value for 'turn' to 'X' to switch between the two players.
        
    printBoard(board)
    #Displays the board as it appears after the last assignment, showing the winning row.

