# Getting data from an online store
import requests
from bs4 import BeautifulSoup

def extract(url, names, prices):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    n = soup.find_all("div", class_="h4 grid-view-item__title product-card__title")
    for name in n: names.append(name.text)
    p = soup.find_all("span", class_="price-item price-item--regular")
    for price in p: prices.append(price.text.strip())
    return names, prices

names, prices = [], []
url = ["https://amigoscool.casa/collections/cool?page=1", "https://amigoscool.casa/collections/cool?page=2", "https://amigoscool.casa/collections/cool?page=3", "https://amigoscool.casa/collections/cool?page=4"]
for i in range(4): names, prices = extract(url[i], names, prices)

pricesCleaned = []
for p in prices:
    p = p.replace(" ", "")
    p = p.replace("$", "")
    if p == "Agotado": p = 350.0
    else: p = float(p)
    pricesCleaned.append(p)

d = {names[i]:pricesCleaned[i] for i in range(len(names))}
d = sorted(d.items(), key=lambda x: x[1], reverse=True)

output = open("output.txt", "w", encoding="utf-8")
for x in d: output.write(f"{x[0]}: {x[1]}\n")
output.close()