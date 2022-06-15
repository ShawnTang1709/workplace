pip install selenium

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
    driver = webdriver.Chrome(chrome_options=options, executable_path='C:\\Users\\*')
    url = "*"
    
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_id("Email").send_keys("*")
    driver.find_element_by_name("Password").send_keys("*")
    driver.find_element_by_xpath('/html/body/div/form/div[3]/div/button').click()
    time.sleep(1)
    #取值
    point = int(driver.find_element_by_id('UnProfit').text.replace(',',''))
    print(point)
    if point>0:
        count = int(driver.find_element_by_id("UnBanance").text)
        if count<0 :
            driver.find_element_by_xpath('//*[@id="buy"]').click()
            print("已買入")
            driver.close()

        elif count>0:
            driver.find_element_by_xpath('//*[@id="sell"]').click()
            print("已賣出")
            driver.close()

    driver.find_element_by_xpath('/html/body/nav[1]/div/div/div[2]/div/a').click()

def average() :
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(chrome_options=options, executable_path='C:\\Users\\Shawn Tang\\Desktop\\線上遊戲測試報告\\BOT\\chromedriver')
    url = "http://superit.net/"
    
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_id("Email").send_keys("hhh111")
    driver.find_element_by_name("Password").send_keys("888888")
    driver.find_element_by_xpath('/html/body/div/form/div[3]/div/button').click()
    time.sleep(1)
    averagepoint = int(driver.find_element_by_xpath('//*[@id="LastPrice2"]'))
    # print(averagepoint)
    driver.close()
average()
    

# 定義需要執行的方法
schedule.every().day.at("22:58").do(trade())
while True:
    schedule.run_pending()
    break

