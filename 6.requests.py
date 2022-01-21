# requests 라이브러리는 주로 크롤링 할 때 http 주소를 얻어오기 위에 쓰인다

import requests

res=requests.get("https://www.google.com")
res.raise_for_status() # 정상인지 확인하는 거 비정상이면 밑에 실행 안 된다



# print("응답코드 :", res.status_code) # 200이면 정상, 403이면 접근 권한 없다


# if res.status_code == requests.codes.ok: 이게 200이랑 같은 의미
#    print("정상입니다") 
# else:
#    print("문제가 생겼습니다. [에러코드", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoolge.html", "w", encoding="utf8") as f: # w가 write을 의미, res.text에 써진 것을 새로운 파일에 써서 만든다
    f.write(res.text)

