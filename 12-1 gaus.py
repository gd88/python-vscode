# 네이버 웹툰 중 '가우스전자'라는 웹툰해 접근해서 각 화 제목, 링크, 평점 긁어오기

import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=675554"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 제목
cartoons=soup.find_all("td", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.a.get_text())
# 링크
for link in cartoons:
    print("https://comic.naver.com/webtoon/list?titleId=675554"+link.a["href"])
# 평점
total_rates=0
likes=soup.find_all("div", attrs={"class":"rating_type"})
for like in likes:
    total_rates+=float(like.strong.get_text())
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))