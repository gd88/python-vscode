# 네이버웹툰에 접근해서 웹툰 제목들 긁어오기

import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


cartoons=soup.find_all("img")  # for문으로 안 하고 title하면 에러뜬다
for cartoon in cartoons:
    print(cartoon["title"]) 