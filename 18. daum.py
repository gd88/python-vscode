# 2015년부터 2020년까지 다음인기영화 연간 5위 이미지로 추출하는 프로젝트

import requests
from bs4 import BeautifulSoup

for year in range(2015,2021):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res=requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    imgs=soup.find_all("img", attrs={"class":"thumb_img"})

    for i, img in enumerate(imgs):
        img_url=img["src"]
        img_res=requests.get(img_url)
        img_res.raise_for_status()

        with open("movie{}-{}.jpg".format(year, i+1), "wb") as f:
            f.write(img_res.content)

        if i >= 4:
            break