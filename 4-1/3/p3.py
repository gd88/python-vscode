
def addTotal(a):
    b=0
    c=0
    while b<a:
        b=b+1
        c=c+b
        
    return c


def mulTotal(a):
    b=1
    c=1
    global gMul
    gMul=1
    while b<a:
        b=b+1
        c=c*b
    gMul = c


    

a=int(input())
d=addTotal(a)
print('addTotal(): ' + str(d))
mulTotal(a)
print('gMul: ' + str(gMul))
