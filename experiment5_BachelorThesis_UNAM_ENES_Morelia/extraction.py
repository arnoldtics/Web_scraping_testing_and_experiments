from time import sleep
import random as r
from selenium import webdriver
from selenium.webdriver.common.by import By

def extraction():
    program = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[9]/td/a").text
    year = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[3]/td").text
    title = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[2]/td").text
    print(program, year, title)
    return (program, year, title)

def next_thesis():
    button = driver.find_element(by=By.XPATH, value="//img[@title='Registro siguiente']")
    button.click()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

link = input("Write the link to the most recent thesis:\n")
number_of_thesis = int(input("Write the total number of thesis to process:\n")) - 1

driver = webdriver.Chrome(options=options)
driver.get(link)

thesis = []

for _ in range(number_of_thesis):
    sleep(r.uniform(1, 2))
    thesis.append(extraction())
    try: next_thesis()
    except: break

print(thesis)

data = open("data1.txt", "w", encoding="utf-8")
for program, year, title in thesis: data.write(f"{program}. {year}. {title}\n")
data.close()