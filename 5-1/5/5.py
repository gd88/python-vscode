import random

def getRandomString(leng):
    string=''
    for i in range(1,int(leng)+1):
        a=random.randint(0,25)
        b=english[a]
        string=string+b

    return string

def joinList(l, space=''):
    string=''
    for i, c in enumerate(l):
        if i > 0:
            string=string+space+c
        else:
            string=string+c
    return string

english='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

n = int(input('Input the length of the string : '))
cheese = list(getRandomString(n))
original = joinList(cheese)
cnt, check = 0, []
eaten = 0

print(f"Generated Cheese is '{original}'")
print('Mouse starts eating!')
while cnt < 10:
    cnt += 1
    eat = None

    while True:
        if eat is None or eat in check:
            eat = getRandomString(1)
        else:
            check.append(eat)
            break

    cheese = ['_' if x == eat else x for x in cheese]

    print(f"Start eating '{eat}'")
    print(f'Eaten alphabet of cheese : {joinList(check, space=" ")}')
    print(f'Original cheese : {original}')
    print(f'Current cheese status : {joinList(cheese)}')
    print()

for x in cheese:
    if x == '_':
        eaten += 1
if eaten == n:
    print('Out of cheese!')
else:
    print('Finally remained Cheese Status :')
    print(f'Eaten alphabet of cheese : {joinList(check, space=" ")}')
    print(f'Original cheese : {original}')
    print(f'Current cheese status : {joinList(cheese)}')

