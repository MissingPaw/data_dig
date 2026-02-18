# %%
import requests as rq
import bs4
import csv

book_info = []
for i in range(1,51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    res = rq.get(url, headers = my_headers)
    res.encoding = 'utf-8'

    if res.status_code == 200:
        soup = bs4.BeautifulSoup(res.text, "html.parser")

    books = soup.select("article.product_pod")


    for book in books:
        title = book.select_one("h3 a")["title"]
        price = book.find("p", class_ = "price_color").get_text(strip = True).replace('£', '')
        avail = book.find("p", class_ = "instock").get_text(strip = True)
        rate = book.find("p", class_ = "star-rating")["class"][1]
        book_dict = {
            "Title": title,
            "Price": price,
            "Rating": rate,
            "Availbility": avail
        }
        book_info.append(book_dict)

keys = ["Title", "Price", "Rating", "Availbility"]

# 2. 打开（或创建）一个文件
# 'w' 代表写入模式，newline='' 是为了防止 Windows 系统出现多余空行
with open("book_info.csv", "w", encoding="utf-8-sig", newline="") as f:
    # 3. 创建一个字典写入器
    writer = csv.DictWriter(f, fieldnames=keys)
    
    # 4. 写入表头
    writer.writeheader()
    
    # 5. 写入所有数据
    writer.writerows(book_info)

print("文件已保存为 book_info.csv！")