import json

with open("products.json") as p:
    products = json.loads(p.read())

print(products)
