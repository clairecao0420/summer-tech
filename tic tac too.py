board=[['-','-','-'],['-','-','-'],['-','-','-']]
for i in range(3):
    print(board[i])
row=int(input('choose a row'))
colum=int(input('choose a colum'))
board[row][colum]='x'
for i in range(3):
    print(board[i])