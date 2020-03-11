def draw_hori(size):
    print(" ---" * size)

def draw_vert(board, i):
    print("| " + str(board[i][0]) + " | " + str(board[i][1]) + " | " + str(board[i][2]) + " |") 

def draw_board(board):
    size = 3
    for i in range(0,size):
        draw_hori(size)
        draw_vert(board, i)
    draw_hori(size)

def diag_match(board):
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    else:
        return 0

def vert_match(board):
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][1]
            break
        else:
            return 0

def hori_match(board):
    for i in range(0,3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[1][i]
            break
        else:
            return 0

def check_winner(board):
    winner = 0
    hori = hori_match(board)
    vert = vert_match(board)
    diag = diag_match(board)
    winner = max(hori, vert, diag)
    if winner > 0:
        print("The winner is player " + str(winner))
        return True
    else:
        return False

def player_turn(player,board,coor):
    c = coor.split(",")
    x = int(c[0])
    y = int(c[1])
    if board[x][y] == 0:
        board[x][y] = player
    else:
        print("Invalid turn!\n")
    return board

def game_flow(p,board):
    draw_board(board)
    p_input = input("Player " + str(p) + "'s turn: ")
    board = player_turn(p,board,p_input)
    return check_winner(board)

def new_turn(p):
    if p == 1:
        p = 2
    else:
        p = 1
    return p

def main():
    print("Tic Tac Toe\n\n")
    board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    winner = False
    player = 1
    while winner == False:
        winner = game_flow(player,board)
        if winner == True:
            draw_board(board)
            break
        player = new_turn(player)

main()
