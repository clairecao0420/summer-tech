board=[['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-']]
win=False
while win==False:
    for i in range (6):
        print(board[i])
    colum=int(input('pick a colum.'))
    turn='o'
    colums=[0,0,0,0,0,0,0]
    board[5-colums[colum]][colum]='o'
    colums[colum]+=1