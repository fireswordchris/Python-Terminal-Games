def main():

    mode = input("1 Player or 2 Player? ").lower()

    if (mode == "1 player"):
        onePlayer()

    elif (mode == "2 player"):
        twoPlayer()

def onePlayer():
    print("Not avaliable")
    main()

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

    if (again == "yes"):
        main()

    else:
        pass
    
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

def translateChoice(playerNum, board):
    choice = input("Player " + str(playerNum) + "'s move (tl,tm,tr,ml,mm,mr,bl,bm,br): ").lower()

    if (playerNum == 1):
        if (choice == "tl"):
            board[0] = 1
            return board

        elif (choice == "tm"):
            board[1] = 1
            return board

        elif (choice == "tr"):
            board[2] = 1
            return board

        elif (choice == "ml"):
            board[3] = 1
            return board

        elif (choice == "mm"):
            board[4] = 1
            return board

        elif (choice == "mr"):
            board[5] = 1
            return board

        elif (choice == "bl"):
            board[6] = 1
            return board

        elif (choice == "bm"):
            board[7] = 1
            return board

        elif (choice == "br"):
            board[8] = 1
            return board

    elif (playerNum == 2):
        if (choice == "tl"):
            board[0] = 2
            return board

        elif (choice == "tm"):
            board[1] = 2
            return board

        elif (choice == "tr"):
            board[2] = 2
            return board

        elif (choice == "ml"):
            board[3] = 2
            return board

        elif (choice == "mm"):
            board[4] = 2
            return board

        elif (choice == "mr"):
            board[5] = 2
            return board

        elif (choice == "bl"):
            board[6] = 2
            return board

        elif (choice == "bm"):
            board[7] = 2
            return board

        elif (choice == "br"):
            board[8] = 2
            return board

    print("Not a valid space, please try again.")
    return translateChoice(playerNum, board)

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