from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui as pag  
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
driver = webdriver.Chrome()
driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')
# ------ 等待頁面加載完畢 ------
time.sleep(5)

##將滑鼠移動到座標為(x,y)=(100,100)的位置上點擊左鍵關閉
ActionChains(driver).move_by_offset(100,100).click().perform()


##將滑鼠移動到最底部的新加坡商蝦皮娛樂電商有限公司台灣分公司
js = "window.scrollTo(0, document.body.scrollHeight);"
driver.execute_script(js)
time.sleep(5)
##元素定位
ele = driver.find_element(By.CSS_SELECTOR,'div[class="AF3TXt"]')
ActionChains(driver).move_to_element(ele).perform()
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
        