from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

##利用驅動程式管理員在執行排重拾自動下載驅動程式
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#爬取多分業的資料在發送請求前指定頁碼範圍
for page in range(1,3):
    
    driver.get(f'https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925/popular?pageNumber={page}')#代表format string

    time.sleep(5)
    items = []
    ##將滑鼠移動到座標為(x,y)=(100,100)的位置上點擊左鍵關閉
    ActionChains(driver).move_by_offset(100,100).click().perform()
    #移動滑鼠至底部顯示所有列表商品
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    cards = driver.find_elements(By.CSS_SELECTOR,"div[class='Qnex0a']")
    # print(len(cards))
    #將彈跳視窗關閉
    for card in cards:
        # ActionChains(driver).move_to_element(card).perform()
        title = card.find_element(By.CSS_SELECTOR,"div[class='WF8zKZ _8ayTha _3I+cDt']").text #商品名稱
        price = card.find_element(By.CSS_SELECTOR,"div[class='CCRieW ZJwBnM']").text#商品價格
        link = card.find_element(By.TAG_NAME,"a").get_attribute('href')##求出<a>內的gref屬性質
        items.append((title,price,link))

    # print(items)
    result = []
    for item in items:

        driver.get(item[2])
        
        for i in range(5):##設定滾動滑鼠的次數
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
        comments = driver.find_elements(By.CSS_SELECTOR,"div[class='Rk6V+3']")
        for comment in comments:
            result.append((item[0],item[1],comment.text))
        break
    print(f"第{page}頁")
    print(result)