
# %%
import requests as rq
import bs4

url = "https://www.aeaweb.org/issues/835"
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
res = rq.get(url, headers = my_headers)
res.encoding = 'utf-8'


# %%
if res.status_code == 200:
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # print(f"网页标题是 {soup.title.text}") #严格情况下还是要用 soup.find("title").text




articles = soup.select("article.journal-article")
title_list = []
author_list = []
for article in articles:
    title_tag = article.find("h3")
    if title_tag:
        title = title_tag.get_text(strip = True)
        if title != "Front Matter":
            title_list.append(title)
    author_tag = article.select("div.article-item-authors span.vcard")
    authors = [author.get_text(separator = " ", strip = True) for author in author_tag]
    author_list.append(authors)





