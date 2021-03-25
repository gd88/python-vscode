
def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c

def mod(a,b):
    c=a%b
    return c

def printMsg():
    print('completed')

a=int(input())
b=int(input())

d=add(a,b)
e=sub(a,b)
f=mul(a,b)
g=div(a,b)
h=mod(a,b)

print('sum: ' + str(d))
print('difference: ' + str(e))
print('product: ' + str(f))
print('division: ' + str(g))
print('remainder: ' + str(h))
printMsg()

