# 파이썬 셀레니움 패키지
# 웹으로 접근한다, 자동화, 동적 데이터 크롤링을 위해 사용한다.

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys # 이 모듈을 import 해야지 바로 함수만으로 enter키를 누를 수 있다.

browser = webdriver.Chrome() # 크롬 웹 드라이버 객체
browser.get("http://naver.com") # 거기서 네이버로 이동
time.sleep(3)
elem=browser.find_element_by_id("query")
elem.click()
elem.send_keys('나도코딩')
elem.send_keys(Keys.ENTER)

# elem=browser.find_elements_by_tag_name("a")
# for e in elem:
#   e.get_attribute("href")