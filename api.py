
# %%
import requests as rq


url = "https://catfact.ninja/fact"
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
res = rq.get(url, headers = my_headers)
res.encoding = 'utf-8'

data = res.json()

print(data["fact"])