# Getting num. pokedex and pokemon names
import requests
from bs4 import BeautifulSoup

url = "https://www.pokemon.com/el/pokedex"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
tag = soup.find_all("a")

cleaning = [t.string for t in tag]
pokemon = []
for c in cleaning:
    if c == None: continue
    elif "\n" in c: continue
    else: pokemon.append(c)
pokemon = pokemon[:-8]

for i, x in enumerate(pokemon): pokemon[i] = x.replace(" -", "")

print(pokemon)