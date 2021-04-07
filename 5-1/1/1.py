a,b=input().split()
c,d=input().split()
e,f=input().split()
hard={a:b,c:d,e:f}
print('Which student\'s score?')
guess=input()
if guess in hard.keys():
      print(guess + '\'s score: ' + hard[guess])
else:
    print(guess+ ' is not in the database.')
