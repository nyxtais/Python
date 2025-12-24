board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    print("   0   1   2")
    print("0 "+board[0][0]+ "  | " + board[0][1] + "  | " + board[0][2])
    print("  ---+---+---")
    print("1 "+board[1][0]+ "  | " + board[1][1] + "  | " + board[1][2])
    print("  ---+----+---")
    print("2 "+board[2][0]+ "  | " + board[2][1] + "  | " + board[2][2])

def check_winner(player):
    for i in range(3):
        if board[i][0] == player and board[i][0] == player and board[i][2] == player:
            return True
        
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

def check_full():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

players = ["X", "O"]
current_player = 0

while True:
    print_board()

    move = input("Player "+players[current_player]+", enter your move (row column): ")
    move = move.split()
    row = int(move[0])
    col = int(move[1])

    if board[row][col] != " ":
        print("Invalid move. Try again :) ")
        continue

    board[row][col] = players[current_player]

    if check_winner(players[current_player]):
        print_board()
        print("Player "+players[current_player]+" wins!")
        break

    if check_full():
        print_board()
        print("Tie!")
        break

    current_player = (current_player + 1) % 2