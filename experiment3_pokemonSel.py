# Interacción con la página oficial de la pokedex

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import random as r

def nombre(nombres):
    n = driver.find_element(by=By.XPATH, value="//div[@class='pokedex-pokemon-pagination-title']").text
    nombres.append(n.split()[0])

def tipo(tipos):
    etiqueta = driver.find_element(by=By.XPATH, value="//div[@class='dtm-type']")
    t = etiqueta.find_element(by=By.XPATH, value=".//ul")
    tipos.append(t.text.replace("\n", " ").strip())

def altura_peso(alturas, pesos):
    etiquetas = driver.find_elements(by=By.XPATH, value="//span[@class='attribute-value']")
    altura, peso = etiquetas[0].text, etiquetas[1].text
    altura = altura.replace(",", ".")
    altura = altura.replace(" ", "")
    altura = altura.replace("m", "")
    peso = peso.replace(",", ".")
    peso = peso.replace(" ", "")
    peso = peso.replace("kg", "")
    alturas.append(float(altura))
    pesos.append(float(peso))

def siguiente():
    boton = driver.find_element(by=By.XPATH, value="//a[@class='next']")
    boton.click()

def aceptarCookie():
    boton = driver.find_element(by=By.XPATH, value="/html/body/div[14]/div[2]/div/div/div[2]/div/div/button[2]")
    boton.click()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
driver.get("https://www.pokemon.com/el/pokedex/bulbasaur")

nombres, tipos, pesos, alturas = [], [], [], []

sleep(r.uniform(1.0, 3.0))
try: aceptarCookie()
except: pass

for i in range(1010):
    sleep(r.uniform(1.0, 3.0))
    nombre(nombres)
    tipo(tipos)
    altura_peso(alturas, pesos)
    siguiente()

salida = open("salida.txt", "w", encoding="utf-8")
for i in range(1010): salida.write(f"{i+1} {nombres[i]} {tipos[i]} {alturas[i]} {pesos[i]}\n")
salida.close()

