import random
hard=[]
for i in range(1,101):
    hard.append(random.randint(1,1000))
for j in hard:
    print(j, end=' ')
    
print('\n')
king = hard[0]
for i in range(1, 100):
    if king < hard[i]:
        king=hard[i]

print('max value: '+str(king))
