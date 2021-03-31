
def printLine(n):
    for i in range(1,n+1):
        print(i, end=' ')
    print()


a=int(input())



for j in range(1,a+1):
    printLine(j)
for k in range(a,0,-1):
    printLine(k)
