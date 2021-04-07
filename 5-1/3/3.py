words = input().split(' ')
dic = {}
for word in words:
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1

for word in dic.keys():
    print(f'{word} : {dic[word]}')

    
