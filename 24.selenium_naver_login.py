from selenium import webdriver
import time

browser = webdriver.Chrome()
#1 네이버로 이동
browser.get("http://naver.com")

#2 로그인 버튼 클릭
login=browser.find_element_by_class_name("link_login")
login.click()

#3 아이디, 비번 입력 + 클릭
browser.find_element_by_id("id").send_keys("dnjsry837")
browser.find_element_by_id("pw").send_keys("dnjsry123")

browser.find_element_by_class_name("btn_login").click()

# 4 id 틀려서 지우고 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("dnjsry8377")

#5 html 정보 툴력(로그인 잘 됐다 가정)
print(browser.page_source)

#7 브라우저 종료
browser.close() #현재 탭만 종료
browser.quit() #전체 브라우저 종료

# 로그인하면 보안문자 입력하라고 뜬다