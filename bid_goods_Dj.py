#python 나라장터 입찰정보수집_20220210(ver_01) 20220421(Renewal)
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By     #새롭게 추가
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, os
start = time.time()  #시작시간

try:
    driver = webdriver.Chrome()
    # driver.get('https://www.d2b.go.kr/psb/bid/serviceBidAnnounceList.do?key=32')
    driver.get('https://www.d2b.go.kr/pdb/bid/goodsBidAnnounceList.do?key=129')

    query1 = "대전"   #소프트웨어 검색시 사용
    area_name = driver.find_element(By.ID,'area_name')
    area_name.click()
    area_name.send_keys(query1)
    area_name.send_keys(Keys.ENTER)

    button = driver.find_element(By.ID, 'btn_search')
    button.click()

    xldown = driver.find_element(By.ID,'btn_excel_down')
    xldown.click()

    time.sleep(5)
    
    os.rename('C:/Users/USER/Downloads/입찰공고목록.xls','C:/Users/USER/Downloads/bid_def_goods.xls')

    print("time :", time.time() - start) #현재시각 - 시작시간

except Exception as e:
    print(e) 
    print("time :", time.time() - start) #현재시각 - 시작시간   
finally:
    
    # time.sleep(5)
    # os.replace('C:/Users/USER/Downloads/bid_def_goods.xls','D:/BID/bid_def_goods.xls')
    driver.close()
