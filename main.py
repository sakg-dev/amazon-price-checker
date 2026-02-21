import json
import requests
from bs4 import BeautifulSoup
import time
from tools import currency_converter, headers, send_email
import os
from dotenv import load_dotenv

if os.getenv("GITHUB_ACTIONS") != True:
    load_dotenv()

with open("products.json") as p:
    products = json.loads(p.read())

usd_amt = os.getenv("USD_AMT")  # in usd

inr_amt = currency_converter(usd_amt, "USD", "INR")

for product in products:
    url = f"https://www.amazon.in/dp/{product}"

    req = requests.get(url, headers=headers, allow_redirects=True)

    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup)
    price = int(
        (soup.find(class_="a-price-whole").text).replace(",", "").replace(".", ""))

    if price <= inr_amt:
        send_email(os.getenv("SEND_EMAIL"), [os.getenv("USER_EMAIL")], "Laptop price dropped below your card's balance!",f"Hey Sak!\n\nFinally the price of your favourite laptop had dropped below your card's amount.\n\n Here's the link: {url}")
        print("found")
        break

    time.sleep(1)
