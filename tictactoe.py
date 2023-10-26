import main as m
import random

def main():

    mode = input("1 Player or 2 Player? (or quit) ").lower()

    if (mode == "1 player"):
        onePlayer()

    elif (mode == "2 player"):
        twoPlayer()
        
    elif (mode == "quit"):
        m.main()
        
    else:
        print("Not a valid choice please try again")
        main()

def onePlayer():
    board = [0,0,0,0,0,0,0,0,0]
    won = False
    translateBoard(board)
    
    while won == False:
        board = computerChoice(1,board)
        won = checkWin(board, 1)
        translateBoard(board)
        if (won):
            break
        
        board = translateChoice(2,board)
        won = checkWin(board,2)
        translateBoard(board)
        if (won):
            break
        
    again = input("Play again? ").lower()
    
    if (again == "yes" or again == "y" or again == "ye" or again == "yeah"):
        onePlayer()
        
    else:
        main()
        
def computerChoice(n, board):
    validMove = False
    
    while not validMove:
        move = random.randint(0,8)
        
        if (not checkTaken(board,move)):
            board[move] = n
            validMove = True
            return board

def twoPlayer():
    board = [0,0,0,0,0,0,0,0,0]
    won = False
    translateBoard(board)

    while won == False:
        board = translateChoice(1, board)
        won = checkWin(board, 1)
        translateBoard(board)
        if (won):
            break

        board = translateChoice(2, board)
        won = checkWin(board, 2)
        translateBoard(board)
        if (won):
            break

    again = input("Play again? ").lower()

    if (again == "yes" or again == "y" or again == "ye" or again == "yeah"):
        twoPlayer()

    else:
        main()
    
def translateBoard(board):
    i = 0
    translated = ""
    for space in board:
        if (space == 0):
            translated = translated + "/"

        elif (space == 1):
            translated = translated + "X"

        elif (space == 2):
            translated = translated + "O"

        i += 1
        if (i >= 3):
            translated = translated + "\n"
            i = 0

    print(translated)

def translateChoice(pNum, board):
    choice = input("Player " + str(pNum) + "'s move (tl,tm,tr,ml,mm,mr,bl,bm,br): ").lower()

    if (choice == "tl" and not checkTaken(board, 0)):
        board[0] = pNum
        return board

    elif (choice == "tm" and not checkTaken(board, 1)):
        board[1] = pNum
        return board

    elif (choice == "tr" and not checkTaken(board, 2)):
        board[2] = pNum
        return board

    elif (choice == "ml" and not checkTaken(board, 3)):
        board[3] = pNum
        return board

    elif (choice == "mm" and not checkTaken(board, 4)):
        board[4] = pNum
        return board

    elif (choice == "mr" and not checkTaken(board, 5)):
        board[5] = pNum
        return board

    elif (choice == "bl" and not checkTaken(board, 6)):
        board[6] = pNum
        return board

    elif (choice == "bm" and not checkTaken(board, 7)):
        board[7] = pNum
        return board

    elif (choice == "br" and not checkTaken(board, 8)):
        board[8] = pNum
        return board

    print("Not a valid space, please try again.")
    return translateChoice(pNum, board)

def checkTaken(board, num):
    if (board[num] == 0):
        return False
    else:
        return True

def checkWin(board, pNum):
    spNum = str(pNum)
    notTie = True
    for spot in board:
        if (spot == 0):
            notTie = True
            break
        else:
            notTie = False

    if (board[0] == pNum and board[1] == pNum and board[2] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[0] == pNum and board[3] == pNum and board[6] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[0] == pNum and board[4] == pNum and board[8] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[1] == pNum and board[4] == pNum and board[7] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[2] == pNum and board[5] == pNum and board[8] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[2] == pNum and board[4] == pNum and board[6] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[3] == pNum and board[4] == pNum and board[5] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (board[6] == pNum and board[7] == pNum and board[8] == pNum):
        print("Player " + spNum + " wins!")
        return True
    elif (notTie == False):
        print("It's a tie!")
        return True
    else:
        return False

if __name__ == "__main__":
    main()