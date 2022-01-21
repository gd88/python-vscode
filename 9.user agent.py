# user agent는 requests를 통해 웹으로 접근할 때 웹에서 막을 경우, 크롬 사용자로 위장해 접근하는 방법이다.

import requests
url="https://nadocoding.tistory.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

res=requests.get(url, headers=headers)
res.raise_for_status() # 정상인지 확인하는 거 비정상이면 밑에 실행 안 된다

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)




