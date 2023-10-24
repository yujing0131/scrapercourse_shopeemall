import requests
import json

# 要抓取的網址
url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&hl=zh-TW&ns=15'

# 請求網站
response = requests.get(url)
gettext = response.content
print(gettext)
# 將整個程式碼爬取下來
getdata = json.loads(gettext[6:])
print(getdata)
