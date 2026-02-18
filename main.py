
# %%
import requests as rq  #用于得到网页的数据
import bs4 #用于解析得到的数据


# %%
url = "https://www.scrapethissite.com/pages/simple/"
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
res = rq.get(url, headers = my_headers)
res.encoding = 'utf-8'


# %%
if res.status_code == 200:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # print(f"网页标题是 {soup.title.text}") #严格情况下还是要用 soup.find("title").text


countries = soup.find_all("div", class_ = "col-md-4 country")
all_countries = []
for country in countries:
    name = country.find("h3", class_ = "country-name").text.strip()
    capital = country.find("span", class_ = "country-capital").text.strip()
    population = country.find("span", class_ = "country-population").text.strip()
    area = country.find("span", class_ = "country-area").text.strip()
    item = {"country": name, "capital": capital,
    "population": population, "area": area}
    all_countries.append(item)

# print(f"一共有{len(all_countries)}个国家")
# print(all_countries[:10])



import csv

# 1. 定义表头，必须和字典里的 Key 完全一致
keys = ["country", "capital", "population", "area"]

# 2. 打开（或创建）一个文件
# 'w' 代表写入模式，newline='' 是为了防止 Windows 系统出现多余空行
with open("countries_data.csv", "w", encoding="utf-8-sig", newline="") as f:
    # 3. 创建一个字典写入器
    writer = csv.DictWriter(f, fieldnames=keys)
    
    # 4. 写入表头
    writer.writeheader()
    
    # 5. 写入所有数据
    writer.writerows(all_countries)

print("文件已保存为 countries_data.csv！")

websites = []
for i in range(1,11):
    a = f"https://example.com/news?page={i}"
    websites.append(a)