from random import randint
answer=int(input('guess a number from 1 to 100'))
number=randint(1,100)
while answer != number:
    if answer<number:
        print('the number is bigger')
        answer=int(input('guess a number from 1 to 100'))
    if answer>number:
        print('the number is smaller')
        answer=int(input('guess a number from 1 to 100'))
print('that is correct!')