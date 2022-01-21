# 셀레니움을 통해 제주도가는 비행기를 예매하는 프로젝트

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url="https://flight.naver.com/"
browser=webdriver.Chrome()
browser.get(url)
browser.maximize_window() #창 극대화

# 장소 제주로 선택
browser.find_elements_by_class_name("select_code__d6PLz")[1].click() # 오는 날 클릭, 가는 날이랑 클래스내임 같아서 인덱스 붙임
time.sleep(1)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[1]/div/input").send_keys("제주") # 제주 검색, xpath로 함
time.sleep(1)
browser.find_element_by_class_name("autocomplete_location__TDL6g").click() # 제주 검색한거 클릭

time.sleep(2)

# 가는 날, 오는 날 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button/b').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[6]/button/b').click()

time.sleep(3)
#항공권 검색
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()



try:
    elem=WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div[1]/div[1]/div/div[2]")))
    #print(elem.text)
    #elem=browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div[1]/div[1]')
    #for i in elem:
     #   print(i.text)
finally:
    browser.quit()