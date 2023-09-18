from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path = "chromedriver")
##利用驅動程式管理員在執行排重拾自動下載驅動程式
driver=  webdriver.Chrome()


driver.get('https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')
time.sleep(5)
items = []
cards = driver.find_elements(By.CSS_SELECTOR,"div[class='Qnex0a']")

for card in cards:
    title = card.find_element(By.CSS_SELECTOR,"div[class='WF8zKZ XNhH9V vy4NFA']").text #商品名稱
    price = card.find_element(By.CSS_SELECTOR,"div[class='CCRieW _7BzXXp']").text#商品價格
    link = card.find_element(By.TAG_NAME,"a").get_attribute('href')##求出<a>內的gref屬性質
    items.append((title,price,link))

print(items)
    