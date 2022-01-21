# 동적 크롤링
# 유튜브 good boy 무대 댓글 긁어오기

# 셀레니움으로 동적인 페이지 (유튜브)에 접근
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


url="https://www.youtube.com/watch?v=-UZXEFzWXfc"
browser=webdriver.Chrome()
browser.get(url)

time.sleep(5)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 900)") # 1920*1080 # 주의할 점: 처음 댓글이 있는 곳으로 스크롤 내려야 한다. 아니면 댓글이 업로드 되지 않는다.
# time.sleep(5)
# browser.execute_script("window.scrollTo(900, 1800)") # 1920*1080 # 주의할 점: 처음 댓글이 있는 곳으로 스크롤 내려야 한다. 아니면 댓글이 업로드 되지 않는다.

# 화면 가장 아래로 스크롤 내리기(유튜브에서 이걸 했더니 스크롤이 위로 팅긴다)
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")



### 다른 끝이 보이는 페이지라면 밑에 코드를 사용하여 끝까지 스크롤을 내리면 된다.#####

# interval = 2 # 2초에 한번씩 스크롤 내림

# # 현재 문서 높이를 가져와서 저장
# prev_height = browser.execute_script("return document.body.scrollHeight")

# # 반복 수행
# while True:
#     # 스크롤을 가장 아래로 내림
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#     # 페이지 로딩 대기
#     time.sleep(interval)

#     # 현재 문서 높이를 가져와서 저장
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if curr_height == prev_height:
#         break

#     prev_height = curr_height

# print("스크롤 완료")



### 하지만 내가 가져온 유튜브 링크는 댓글이 매우 많아 끝까지 내리기가 현실적으로 불가능하므로 일정부분가지만 작업을 수행하겠다.

interval = 2 # 2초에 한번씩 스크롤 내림

# 반복 수행
number=0
i=0

while number<6:
     # 스크롤을 900으로 내림
     browser.execute_script("window.scrollTo(0, 900+{})".format(i))

     # 페이지 로딩 대기
     time.sleep(interval)

     # 현재 문서 높이를 가져와서 저장
     curr_height = browser.execute_script("return document.body.scrollHeight")


     
     number+=1
     i+=900

print("스크롤 완료")

## 셀레니움으로 댓글 접근한 후 beatifulsoup을 사용해서 댓글 크롤링
import requests
from bs4 import BeautifulSoup



soup=BeautifulSoup(browser.page_source, "lxml")
datas=soup.find_all("ytd-comment-thread-renderer", attrs={"class":"style-scope ytd-item-section-renderer"})

print(len(datas))


for data in datas:
    content=data.find("yt-formatted-string", attrs={"id":"content-text"}).get_text()
    print(content)

