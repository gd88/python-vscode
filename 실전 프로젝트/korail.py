# 1월 29일 용산 -> 순천: KTX 일반석, 14시 12분 기차 취소표 매크로 실제 프로젝트
# 경고문과 주의사항이 뜨는 창은 html이 표시되지 않아 pyautogui를 공부해서 사용했다.


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

url="https://www.letskorail.com/ebizprd/prdMain.do"

driver.get(url)
driver.maximize_window()

# 로그인하기 클릭
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/ul/li[2]/a').click()
time.sleep(1)

# 휴대전화로 입력 클릭
driver.find_element_by_xpath('//*[@id="radInputFlg2"]').click()
time.sleep(1)

# 휴대전화랑 비밀번호 입력
driver.find_element_by_id('txtCpNo2').send_keys('8386')
driver.find_element_by_id('txtCpNo3').send_keys('8377')
driver.find_element_by_id('txtPwd1').send_keys('dnjsry23!')
driver.find_element_by_id('txtPwd1').send_keys(Keys.ENTER)

# 출발역 설정
driver.find_elements_by_class_name("btn_sch_r")[0].click()
print(driver.window_handles) #활성 탭 목록을 보여준다
driver.switch_to.window(driver.window_handles[1]) # 2번째 활성창 고르기
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
time.sleep(2)

#driver.close()

# 도착역 설정
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.find_elements_by_class_name('btn_sch_r')[1].click() # s 안 붙이면 첫번째만 찾는다는 의미
driver.switch_to.window(driver.window_handles[2])
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[7]/td[4]/a').click()
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

#출발일 설정
driver.find_elements_by_class_name("btn_sch_r")[2].click()
driver.switch_to.window(driver.window_handles[2])
time.sleep(1)
driver.find_element_by_xpath('//*[@id="d20220129"]').click()
driver.switch_to.window(driver.window_handles[0])

# 예매  버튼 클릭
driver.find_element_by_xpath('//*[@id="res_cont_tab01"]/form/div/fieldset/p/a/img').click()
time.sleep(2)

# ktx로 상세 검색
driver.find_element_by_xpath('//*[@id="selGoTrainRa00"]').click()
driver.find_element_by_xpath('//*[@id="center"]/div[3]/p/a/img').click()
time.sleep(1)

while True:
    # 매진 or 예매가 있는 테이블
    elem=driver.find_element_by_xpath('//*[@id="tableResult"]/tbody/tr[10]/td[6]')
    time.sleep(1)

    # 매진이면 다시 클릭
    if elem.find_element_by_tag_name('img').get_attribute("alt")=="좌석매진":
        driver.refresh()
        time.sleep(1)
        continue

    # 선택 가능하면 선택
    elem.find_element_by_tag_name('img').click()
    time.sleep(2)
    # 경고문이랑 주의사항 뜨는 거 해제, 이건 html 검사가 안 돼서 pyautogui 이용
    pyautogui.click(1188,207)
    time.sleep(2)
    pyautogui.click(1203,416)
    time.sleep(1)

    # 결제
    driver.find_element_by_xpath('//*[@id="btn_next"]').click()
    time.sleep(1)
    # 신용카드 선택
    driver.find_element_by_xpath('//*[@id="tabStl1"]').click()
    time.sleep(1)
    # 카드 번호 입력
    driver.find_element_by_xpath('//*[@id="Div_Card"]/table/tbody/tr[2]/td/input[1]').send_keys('4854790261577451')
    time.sleep(1)
    # 카드 유효기간 선택
    driver.find_element_by_xpath('//*[@id="month"]/option[11]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='year']/option[3]").click()
    time.sleep(1)
    # 카드 비번
    driver.find_element_by_xpath('//*[@id="Div_Card"]/table/tbody/tr[5]/td/input').send_keys("08")
    time.sleep(1)
    # 인증번호
    driver.find_element_by_xpath('//*[@id="Div_Card"]/table/tbody/tr[6]/td/input').send_keys("991106")
    time.sleep(1)
    # 개인정보동의
    driver.find_element_by_xpath('//*[@id="chkAgree"]').click()
    # 결제하기
    driver.find_element_by_xpath('//*[@id="fnIssuing"]').click()

    break

driver.quit()