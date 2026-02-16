
# %%
# 导入必要的packages
import requests as rq
import bs4
url = "https://yss.mof.gov.cn/2024zyjs/202509/t20250904_3971479.htm"

# 伪装服务器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 获取内容
response = rq.get(url, headers = headers)
response.encoding = 'utf-8'

# 解析内容
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# 提取标题相关内容
title = soup.find("h2", class_ = "title_con")

# 打印英文标题
title_tag = title.get_text(separator= "|")
 
parts = title_tag.split("|")

english_title = parts[1]