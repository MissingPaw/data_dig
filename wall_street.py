import requests as rq
import csv
from datetime import datetime

url = "https://api-one-wscn.awtmt.com/apiv1/content/information-flow"

params = {
    "channel": "global",
    "accept": "article",
    "limit": "20",
    "action": "upglide",
    "cursor": ""  
}

my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

news_list = []

for i in range(1,11):

    res = rq.get(url, headers = my_headers, params=params)
    res.encoding = 'utf-8'

    data = res.json()
    items = data["data"]["items"]

    # 使用列表推导式，在这一步就把 20 条原始数据转化成 20 个“干净的小字典”
    cleaned_page_news = [
        {
            "Title": i["resource"].get("title", "无标题"),
            "Author": i["resource"].get("author", {}).get("display_name", "佚名"),
            "Date": datetime.fromtimestamp(i["resource"].get("display_time", 0)).strftime("%Y-%m-%d"),
            "Abstract": i["resource"].get("content_short", "无摘要")
        } 
        for i in items if "resource" in i # 确保这条数据里确实有内容
    ]

    # 现在的 cleaned_page_news 是一个整洁的列表，直接 extend 进去！
    news_list.extend(cleaned_page_news)
    
    # 更新游标
    params['cursor'] = data["data"]["next_cursor"]


# 1. 定义表头，必须和字典里的 Key 完全一致
keys = ["Title", "Author", "Date", "Abstract"]

# 2. 打开（或创建）一个文件
# 'w' 代表写入模式，newline='' 是为了防止 Windows 系统出现多余空行
with open("wall_street.csv", "w", encoding="utf-8-sig", newline="") as f:
    # 3. 创建一个字典写入器
    writer = csv.DictWriter(f, fieldnames=keys)
    
    # 4. 写入表头
    writer.writeheader()
    
    # 5. 写入所有数据
    writer.writerows(news_list)

print("文件已保存为 wall_street.csv！")