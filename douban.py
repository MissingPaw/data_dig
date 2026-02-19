# %%
import requests as rq
import csv

lists = []
for i in range(0,1061,20):
    url = f"https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={i}&limit=20"
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    res = rq.get(url, headers = my_headers)
    res.encoding = 'utf-8'

    data = res.json()



    for m in data:
        title = m["title"]
        region = ",".join(m["regions"])
        type = ",".join(m["types"])
        rating = m["rating"][0]
        rank = m["rank"]
        item = {
            "Title": title,
            "Region": region,
            "Type": type,
            "Rating": rating,
            "Rank": rank
        }
        lists.append(item)



# 1. 定义表头，必须和字典里的 Key 完全一致
keys = ["Title", "Region", "Type", "Rating", "Rank"]

# 2. 打开（或创建）一个文件
# 'w' 代表写入模式，newline='' 是为了防止 Windows 系统出现多余空行
with open("douban.csv", "w", encoding="utf-8-sig", newline="") as f:
    # 3. 创建一个字典写入器
    writer = csv.DictWriter(f, fieldnames=keys)
    
    # 4. 写入表头
    writer.writeheader()
    
    # 5. 写入所有数据
    writer.writerows(lists)

print("文件已保存为 douban.csv！")