import requests
import json
import pandas as pd
# 要抓取的網址
url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&hl=zh-TW&ns=15'

# 請求網站
response = requests.get(url)
gettext = response.content
# print(gettext)
# 將整個程式碼爬取下來
getdata = json.loads(gettext[6:])
data = getdata['default']['trendingSearchesDays']
# print(getdata['default']['trendingSearchesDays'])

result = pd.json_normalize(data)
date = result['date']
# print(result)
#針對不同日期列出趨勢關鍵字
for i in range(len(date)):
    content = pd.DataFrame.from_dict(result['trendingSearches'][i])
    # print(len(result))
    for j in range(len(content)):
        title = content.iloc[j]['title']['query']
        print(title)
        print(content.iloc[j])


    

