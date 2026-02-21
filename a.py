# import os
# from dotenv import load_dotenv
# load_dotenv()

# from tools import send_email
# send_email(os.getenv("SEND_EMAIL"), [os.getenv("USER_EMAIL")], "Laptop price dropped below your card's balance!",f"Hey Sak!\n\nFinally the price of your favourite laptop had dropped below your card's amount.\n\nHere's the link: https://a.com")
# send_email(os.getenv("SEND_EMAIL"),[os.getenv("USER_EMAIL")],"Test subject","This is how message will be shown\n\nThanks")

# import requests
# import json
# payload = {
#     'api_key': os.getenv("SCAPERAPI_KEY"),
#     'asin': 'B0CR8XY6MG',
#     'tld': 'in'
# }
# r = requests.get('https://api.scraperapi.com/structured/amazon/product',params=payload)
# price = int((json.loads(r.text)["pricing"]).replace("₹","").replace(",",""))
# print(price)