# 무신사에서 쿠어 발마칸 코트 취소상품, 매크로 이용해 잡아오기 프로젝트

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


url="https://store.musinsa.com/app/goods/2144196"
driver.get(url)
driver.maximize_window()
time.sleep(2)


while True:

    box=driver.find_element_by_xpath('//*[@id="buy_option_area"]/div[1]')
    
    # 품절인지 확인하고 품절이면 새로고침
    if box.find_element_by_class_name('txt-default'):
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        continue
    
    # 사이즈 고르기
    driver.find_element_by_xpath('//*[@id="option1"]/option[2]').click()
    time.sleep(2)

    # 구매 버튼 클릭
    driver.find_element_by_class_name("btn_black").click()
    time.sleep(2)

    # 로그인,비번 입력
    login=driver.find_element_by_name("id")
    login.send_keys("dnjsry8377")
    pwd=driver.find_element_by_name("pw")
    pwd.send_keys("dnjsry23!")
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/button').click()

    # 개인정보 동의 + 무통장 입금 클릭+ 결제 버튼
    driver.find_element_by_xpath('//*[@id="payment_info_area"]/div[4]/ul/li[2]/div[1]/label[2]').click()
    driver.find_element_by_xpath('//*[@id="payment_info_area"]/ul[5]/li[2]/div/div[1]/label/input').click()
    driver.find_element_by_xpath('//*[@id="btn_pay"]').click()

    break
driver.quit()