import random

def getRandomString(leng):
    string=''
    for i in range(1,int(leng)+1):
        a=random.randint(0,25)
        b=english[a]
        string=string+b

    return string


english='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

n = int(input('Input the length of the string : '))
cheese = getRandomString(n)
original = cheese
cnt, check = 0, ''
eaten = 0

print(f"Generated Cheese is '{original}'")
print('Mouse starts eating!')
while cnt < 10 and eaten < n:
    cnt += 1
    eat = None

    while True:
        if eat is None or eat in check:
            eat = getRandomString(1)
        else:
            check += (eat + ' ')
            break

    for c in cheese:
        if c == eat:
            cheese = cheese.replace(eat, '_', 1)
            eaten += 1

    print(f"Start eating '{eat}'")
    print(f'Eaten alphabet of cheese : {check}')
    print(f'Original cheese : {original}')
    print(f'Current cheese status : {cheese}')
    print()

if eaten == n:
    print('Out of cheese!')
else:
    print('Finally remained Cheese Status :')
    print(f'Eaten alphabet of cheese : {check}')
    print(f'Original cheese : {original}')
    print(f'Current cheese status : {cheese}')


