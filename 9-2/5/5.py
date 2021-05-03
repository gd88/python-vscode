def combi(n,r):
    if n==r:
        return 1
    elif r==0:
        return 1
    else:
        return combi(n-1,r-1)+combi(n-1,r)

a,b=input().split()
a=int(a)
b=int(b)
print(combi(a,b))