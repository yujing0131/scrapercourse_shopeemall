import requests
from bs4 import BeautifulSoup

stock='2330'
##要抓取的網址
url = 'https://tw.stock.yahoo.com/q/q?s='+stock
##請求網站
list_req = requests.get(url)
##將網站的所有程式碼爬取下來
soup = BeautifulSoup(list_req.content,"html.parser")


