import json
import requests
from bs4 import BeautifulSoup
import time

with open("products.json") as p:
    products = json.loads(p.read())

# usd_to_inr_amt =

for product in products:
    url = f"https://www.amazon.in/dp/{product}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-IN,en;q=0.9"
    }
    req = requests.get(url, headers=headers, allow_redirects=True)
    # with open(product,"w") as f:
    #     f.write(req.text)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(soup.find(id="nav-logo-sprites"))
    price = int((soup.find(class_="a-price-whole").text).replace(",","").replace(".",""))
    # print(url)
    time.sleep(1)
