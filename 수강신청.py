

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

url="https://portal.hanyang.ac.kr/sso/lgin.do"
browser=webdriver.Chrome()
browser.get(url)

time.sleep(3)

# 바로가기 클릭
browser.find_element_by_class_name("goPortal").click()
time.sleep(2)
# 로그인하기
login=browser.find_element_by_id("userId")
login.send_keys("rladnjsry837")
pwd=browser.find_element_by_id("password")
pwd.send_keys("rladnjsry23")
pwd.send_keys(Keys.ENTER)
time.sleep(2)
# 비밀번호 다음에 변경 클릭
browser.find_element_by_id("btn_cancel").click()
time.sleep(3)

# 교과목 포트폴리오로 들어가기
browser.find_element_by_link_text('학사행정').click()
time.sleep(2)
browser.find_element_by_link_text('교과목포트폴리오').click()
time.sleep(2)

# 서울로 선택
browser.find_element_by_id('cbCampus').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="cbCampus"]/option[2]').click() # 서울대학 선택
time.sleep(2)
browser.find_element_by_id('cbHakgwa').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="cbHakgwa"]/option[2]').click()
time.sleep(2)
# 조회 클릭
browser.find_element_by_id('btn_Find').click()
