import json
import requests
from bs4 import BeautifulSoup
import time
from tools import currency_converter, headers


with open("products.json") as p:
    products = json.loads(p.read())

usd_amt = 551.59  # in usd

inr_amt = currency_converter(usd_amt, "USD", "INR")

for product in products:
    url = f"https://www.amazon.in/dp/{product}"

    req = requests.get(url, headers=headers, allow_redirects=True)

    soup = BeautifulSoup(req.text, 'html.parser')
    price = int(
        (soup.find(class_="a-price-whole").text).replace(",", "").replace(".", ""))

    if price <= inr_amt:
        print(f"found: {url}")
        break

    time.sleep(1)
