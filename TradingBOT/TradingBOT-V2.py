from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
import requests
import schedule

#登入
def trade() :
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(chrome_options=options, executable_path='C:\\Users\\**')
    url = "*"
    
    driver.get(url)
    time.sleep(1)
    for n in range (1,16):
        i=str(n)
        s= str("*")
        if n>=10 :
            s =('*')
        driver.find_element_by_id("Email").send_keys(s+i)
        driver.find_element_by_name("Password").send_keys("**")
        driver.find_element_by_xpath('/html/body/div/form/div[3]/div/button').click()
        time.sleep(1)
        #取值
        point = int(driver.find_element_by_id('UnProfit').text.replace(',',''))
        print(s+i,point)
        if point>0:
            count = int(driver.find_element_by_id("UnBanance").text)
            if count<0 :
                driver.find_element_by_xpath('//*[@id="buy"]').click()
                print("已買入")
                driver.close()
                break
            elif count>0:
                driver.find_element_by_xpath('//*[@id="sell"]').click()
                print("已賣出")
                driver.close()
                break
        driver.find_element_by_xpath('/html/body/nav[1]/div/div/div[2]/div/a').click()


# 定義需要執行的方法
schedule.every().day.at("22:58").do(trade())
while True:
    schedule.run_pending()
    break

