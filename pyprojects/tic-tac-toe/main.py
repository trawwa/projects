board = [' ' for x in range(10)]


def printBoard(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3] + "| ")
    print("---------")
    print(" " + board[4] + "| " + board[5] + "| " + board[6] + "| ")
    print("---------")
    print(" " + board[7] + "| " + board[8] + "| " + board[9] + "| ")
    print("---------")


def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def isWinner(bo, le):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[1] == letter and board[4] == letter and board[7] == letter) or 
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == " "


def playerMove():
    run = True
    while run:
        move = input("Please insert position for 'X'(1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("x", move)
                else:
                    print("Sorry, this space is occupied.")
            else:
                 print("Plese type number whithin the range.")
        except:
            print("Please type a number.")