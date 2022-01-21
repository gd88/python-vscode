## beautifulsoup으로 댓글을 읽어오려 했으나 바로 댓글이 업로드되지 않고 밑으로 내려야만 댓글이 업로드 돼 html을 검사할 수 없다. >> 동적 크롤링 필요

import requests
from bs4 import BeautifulSoup



url="https://www.youtube.com/watch?v=-UZXEFzWXfc"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "Accpet-Language":"ko-KR,ko"}
res=requests.get(url, headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text, "lxml")
datas=soup.find_all("ytd-comment-thread-renderer", attrs={"class":"style-scope ytd-item-section-renderer"})
print(len(datas))


for data in datas:
    title=data.find("yt-formatted-string", attrs={"id":"text"}).get_text()
    print(title)