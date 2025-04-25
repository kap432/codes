board = [" "] * 9
wins  = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]

def show():
    print(board[0],"|",board[1],"|",board[2])
    print("-"*5)
    print(board[3],"|",board[4],"|",board[5])
    print("-"*5)
    print(board[6],"|",board[7],"|",board[8])

def who_won():
    for a,b,c in wins:
        if board[a]==board[b]==board[c]!=" ": return board[a]
    return None

turn = "X"
while True:
    show()
    move = int(input(f"{turn} (0‑8): "))
    if board[move]!=" ": print("Busy!"); continue
    board[move]=turn
    if who_won() or " " not in board: break
    turn = "O" if turn=="X" else "X"

show()
print("Draw!" if not who_won() else who_won(),"wins!")