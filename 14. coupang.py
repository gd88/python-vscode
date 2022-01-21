# 쿠팡에서 컴퓨터를 구할 떄, 조건에 맞는 목록들을 긁어오고 제품명, 가격, 평점, 평점수를 수집하는 프로젝트

import requests
from bs4 import BeautifulSoup

headers={"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

for i in range(1, 25):
    print("페이지", i)
    url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")


    items=soup.find_all("li", attrs={"class":"search-product"}) #이게 사실상 제일 중요, 밑에 속성들을 다 가지고 있는 태그를 잡아서 꼬리로 내리는 것
    for item in items:
        # 무료배송 제외
        free_del=item.find("span", attrs={"class":"badge badge-delivery"})
        if free_del:
            print("무료배송제외")
            continue

        name=item.find("div", attrs={"class":"name"}).get_text() #제품명
        # apple 제품 제외
        if "apple" in name:
            print("사과제품입니다")
            continue

        price=item.find("strong", attrs={"class":"price-value"}).get_text() #가격
        

        #리뷰 100개이상, 평점 4.5이상 되는 것만 조회
        rating=item.find("em", attrs={"class":"rating"}) # 평점
        if rating:
            rating=rating.get_text()

        else:
            print("평점 없는 상품")
            continue

        rating_count=item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
        if rating_count:
            rating_count=rating_count.get_text()[1:-1] # (28)이런 식으로 돼 있기 떄문에
        else:
            print("평점수 없음")
            continue

        if float(rating) >= 4.5 and float(rating_count) >=100:
             #print(name, price, rating, rating_count)
            print(f"제품명: {name}")
            print(f"가격: {price}") 
            print(f"평점: {rating}")
            print(f"평점수: {rating_count}") 


   
