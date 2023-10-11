from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains

##利用驅動程式管理員在執行排重拾自動下載驅動程式
driver=  webdriver.Chrome()

driver.get('https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')
time.sleep(5)
items = []
##將滑鼠移動到座標為(x,y)=(100,100)的位置上點擊左鍵關閉
ActionChains(driver).move_by_offset(100,100).click().perform()
cards = driver.find_elements(By.CSS_SELECTOR,"div[class='Qnex0a']")
#將彈跳視窗關閉
for card in cards:
    # ActionChains(driver).move_to_element(card).perform()
    title = card.find_element(By.CSS_SELECTOR,"div[class='WF8zKZ _8ayTha _3I+cDt']").text #商品名稱
    price = card.find_element(By.CSS_SELECTOR,"div[class='CCRieW ZJwBnM']").text#商品價格
    link = card.find_element(By.TAG_NAME,"a").get_attribute('href')##求出<a>內的gref屬性質
    items.append((title,price,link))


result = []
for item in items:

    driver.get(item[2])
    # time.sleep(5)
    for i in range(5):##設定滾動滑鼠的次數
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
    comments = driver.find_elements(By.CSS_SELECTOR,"div[class='Rk6V+3']")
    for comment in comments:
        result.append((item[0],item[1],comment.text))
    break

print(result)