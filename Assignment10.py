from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=  webdriver.Chrome()
driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')

time.sleep(5)
items=[]
cards = driver.find_elements(By.CSS_SELECTOR,'div[class="Qnex0a"]')
print(cards)

for card in cards :
    title = card.find_element(By.CSS_SELECTOR,"div[class='WF8zKZ XNhH9V vy4NFA']").text
    price = card.find_element(By.CSS_SELECTOR,"div[class='hs7RXe']").text
    link = card.find_element(By.TAG_NAME,"a").get_attribute('href')
    items.append((title,price,link))

print(items)
