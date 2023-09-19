from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')
# ------ 等待頁面加載完畢 ------
time.sleep(10)
try:
    cards = driver.find_elements(By.CSS_SELECTOR,"div[class='Qnex0a']")
    print(cards)
    items = []
    for card in cards:
        title = card.find_element(By.CSS_SELECTOR,"div[class='WF8zKZ XNhH9V vy4NFA']").text #商品名稱
        price = card.find_element(By.CSS_SELECTOR,"div[class='CCRieW _7BzXXp']").text#商品價格
        link = card.find_element(By.TAG_NAME,"a").get_attribute('href')##求出<a>內的gref屬性質
        items.append((title,price,link))

    print(items)
except (TimeoutException, NoSuchElementException) as e:
    print("Table not found:", e)
        