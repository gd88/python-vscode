def printStarDia(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(0,i+1):
            print('* ', end='')

        print()

    for l in range(n):
        for p in range(l):
            print(' ', end='')
        for o in range(n-l):
            print('* ', end='')
        print()

        

a=int(input())
printStarDia(a)

    
