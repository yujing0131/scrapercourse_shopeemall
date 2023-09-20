from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
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
    title = card.find_element(By.CSS_SELECTOR,"div[class='WF8zKZ XNhH9V vy4NFA']").text #商品名稱
    price = card.find_element(By.CSS_SELECTOR,"div[class='CCRieW _7BzXXp']").text#商品價格
    link = card.find_element(By.TAG_NAME,"a").get_attribute('href')##求出<a>內的gref屬性質
    items.append((title,price,link))

print(items)
    