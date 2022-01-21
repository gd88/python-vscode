# 코스피 종목이랑 값들 긁어와서 csv파일로 저장하는 프로젝트

import csv
import requests
from bs4 import BeautifulSoup

filename="시가총액.csv"
f=open(filename, "w", encoding="utf-8-sig", newline="")    
writer=csv.writer(f)
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for i in range(1,36):
    url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(i)
    res=requests.get(url)
    soup=BeautifulSoup(res.text, "lxml")

    rows=soup.find_all("tr", attrs={"onmouseover":"mouseOver(this)"})
    for row in rows:
        columns=row.find_all("td")
        data=[column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)