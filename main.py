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

for asin in products:
    url = f"https://www.amazon.in/dp/{asin}"

    payload = {
        'api_key': os.getenv("SCAPERAPI_KEY"),
        'asin': asin,
        'tld': 'in'
    }
    r = requests.get('https://api.scraperapi.com/structured/amazon/product',params=payload)
    price = int((json.loads(r.text)["pricing"]).replace("₹","").replace(",",""))

    if price <= inr_amt:
        send_email(os.getenv("SEND_EMAIL"), [os.getenv("USER_EMAIL")], "Laptop price dropped below your card's balance!",f"Hey Sak!\n\nFinally the price of your favourite laptop had dropped below your card's amount.\n\nHere's the link: {url}")
        # print("found")
        break

    time.sleep(1)
