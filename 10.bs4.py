# beautifulsoup 라이브러리는 크롤링에 주로 쓰인다. requests를 이용해 접근하고자 하는 웹의 http 주소를 받은 다음 beatufiulsuop은 이를 html 또는 lxml으로 파싱해 객체로 만들어 원하는 동작을 수행하도록 한다.

import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) # soup 객체에서 처음으로 발견되는 a
#print(soup.a.attrs) # a element의 속성 정보를 출력
#print(soup.a["href"]) # a element의 href속성 '값' 정보를 출력


#print(soup.find('a', attrs={"class":"Nbtn_upload"})) #class="Nbtn_upload인 a element를 찾아줘
#print(soup.find(attrs={"class":"Nbtn_upload"})) # "class":"Nbtn_upload"를 찾아줘

rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
rank2=rank1.next_sibling.next_sibling
rank3=rank1.next_sibling.next_sibling.next_sibling.next_sibling
print(rank3.a.get_text())
print(rank3.previous_sibling.previous_sibling.a.get_text())

print(rank1.parent)
rank2=rank1.find_next_sibling("li")
print(rank2.a.get_text())
print(rank3.find_previous_sibling("li").a.get_text())

rank1.find_next_siblings("li")

webtoon = soup.find("a", text="싸움독학-113화 : 진짜 칼이네?!")
print(webtoon)
