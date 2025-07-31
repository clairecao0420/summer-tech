board=[['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-']]
win=False
turn='o'
colums=[0,0,0,0,0,0,0]
while win==False:
    for i in range (6):
        print(board[i])
    colum=int(input('pick a colum.'))
    board[5-colums[colum]][colum]=turn
    colums[colum]+=1
    for i in range(3):
        for j in range(7):
            if board[i][j]==turn and board[i+1][j]==turn and board[i+2][j]==turn and board[i+3][j]==turn:
                win=True
                for i in range (6):
                    print(board[i])
                print(turn +' won')
    for i in range(4):
        if board[5][i]==turn and board[5][i]==turn and board[5][i]==turn and board[5][i]:            
            print(turn +' won')
    if colum>6:
        colum=6
    if turn=='o':
        turn='x'
    else:
        turn='o'
        