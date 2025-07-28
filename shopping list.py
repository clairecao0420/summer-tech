list=[]
repeat='yes'
while repeat=='yes':
    add=input('do you want to add something?')
    if add=='yes':
        item=input('what would you like to add?')
        list.append(item)
    remove=input('do you want to remove something?')
    if remove=='yes':
        item2=input('what would you like to remove?')
        list.remove(item2)
    repeat=input('do you want to keep going')
    print(list)