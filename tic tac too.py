turn = 'x'
board=[['-','-','-'],['-','-','-'],['-','-','-']]
for i in range(3):
    print(board[i])
while True:
    row=int(input('choose a row'))
    colum=int(input('choose a colum'))
    if not board [row][colum]=='-':
        print('that spot is already taken')
        continue
    board[row][colum]=turn
    for i in range(3):
        print(board[i])
    if board [0][0]==turn and board [0][1]==turn and board [0][2]==turn:
        break
    elif board [0][0]==turn and board [1][0]==turn and board [2][0]==turn:
        break
    elif board [2][0]==turn and board [2][1]==turn and board [2][2]==turn:
        break
    elif board [0][1]==turn and board [1][1]==turn and board [2][1]==turn:
        break
    elif board [0][0]==turn and board [1][1]==turn and board [2][2]==turn:
        break
    elif board [2][0]==turn and board [2][1]==turn and board[2][2]==turn:
        break
    elif board [0][2]==turn and board [1][2]==turn and board[2][2]==turn:
        break
    elif board [2][0]==turn and board [1][1]==turn and board[0][2]==turn:
        break
    a=False
    for i in range(3):
        for j in range(3):
            if board [i] [j]=='-':
                a=True
                break
        if a==True:
            break
    if a==False:
        break
    if turn=='x':
        turn='o'
    elif turn=='o':
        turn='x'
if a==False:
    print('tie')
else:
    print('player ' + turn + ' won!')