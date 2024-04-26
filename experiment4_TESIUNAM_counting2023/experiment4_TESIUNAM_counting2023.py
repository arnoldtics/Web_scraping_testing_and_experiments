# Extraction and counting data from bachelor's degree thesis from UNAM ENES Morelia 2023

from time import sleep
import random as r
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def extraction():
    carrera = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[9]/td/a").text
    return carrera

def next_thesis(): 
    button = driver.find_element(by=By.XPATH, value="//img[@title='Registro siguiente']")
    button.click()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
driver.get("https://tesiunam.dgb.unam.mx/F/TNLQBC5QILDFKS5IIHSLVGPBBJDJSE3QDULVB97199LQYPSI97-05430?func=full-set-set&set_number=078919&set_entry=000001&format=999")

counting = {}

for _ in range(83):
    sleep(r.uniform(1.10, 3.31))
    program = extraction()
    try: counting[program] += 1
    except: counting[program] = 1
    try: next_thesis()
    except: break

print(counting)

output= open("output.txt", "w", encoding="utf-8")
for program, number in counting.items(): output.write(f"{program}: {number}")
output.close()