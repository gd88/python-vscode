import random

def getRandomString(leng):
    string=''
    for i in range(1,int(leng)+1):
        a=random.randint(0,25)
        b=english[a]
        string=string+b

    return string



english='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
leng=input()
rstring=getRandomString(leng)
print(rstring)
