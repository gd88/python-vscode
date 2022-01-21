# 정규식 모듈 re

import re #정규식
# abcd, book, desk
# ca?e > cafe, case, cave
# caae, cabe .....

p = re.compile('ca.e') # .은 하나의 문자를 의미>cafe이런 건 되는데 caffe같은 건 안 된다 
# ^은 문자열의 시작 > ^de은 desk, destination같은 것
# se$ 는 끝

def print_match(m):
    if m:
        print("m.group():", m.group()) #일치하는 문자열 반환
        print("m.string:", m.string) #입력받은 문자열 반환
        print("m.start():", m.start()) #일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
        
    else:
        print("매칭되지 않음")

m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

m = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는지 확인
print(m)
#print_match(m)


#list=p.findall("good care cafe")  # 일치하는 모든 것을 리스트로 반환
#print(list)

# 1. p = re.compile("원하는 형태")
# 2. m=p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m=p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
# 4. list = p.findall("비교할 문자열"): 일치하는 모든 것을 리스트 형태로 반환
