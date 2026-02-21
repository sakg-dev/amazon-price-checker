from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-IN,en;q=0.9"
}


def currency_converter(amt, from_, to):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amt}&From={from_}&To={to}"
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    amt = soup.find_all(class_="amount-input")
    val = amt[1].contents[1]["value"]
    return float(val)


def send_email(from_, to, subject, message):
    pass
