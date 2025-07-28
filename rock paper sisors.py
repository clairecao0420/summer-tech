from random import randint
answer2=input('do you want to play again?')
while answer2=='yes':
    x=randint(0,2)
    answer=input('pick rock,paper or sisors')
    if x==0:
        x='rock'
    if x==1:
        x='paper'
    if x==2:
        x='sisors'
    print (x)
    if answer=='rock' and x=='paper':
        print('you lost')
    if answer=='rock' and x=='sisors':
        print('you won')
    if answer=='paper' and x=='rock':
        print('you won')
    if answer=='paper' and x=='sisors':
        print('you lost')
    if answer=='sisors' and x=='rock':
        print('you lost')
    if answer=='sisors' and x=='paper':
        print('you win')
    if answer=='sisors' and x=='sisors':
        print('tie')
    if answer=='rock' and x=='rock':
        print('tie')
    if answer=='paper' and x=='paper':
        print('tie')
    answer2=input('do you want to play again?')