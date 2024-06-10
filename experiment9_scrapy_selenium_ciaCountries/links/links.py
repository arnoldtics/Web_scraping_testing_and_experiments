from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--incognito')

url = "https://www.cia.gov/the-world-factbook/countries/"
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

with open("links.txt", "w") as file:
    for i in range(22):
        browser.maximize_window()
        links = browser.find_elements(by=By.XPATH, value="//a[@class='inline-link']")
        for link in links: file.write("\"" + link.get_attribute('href') + "\"," + "\n")
        sleep(5)
        browser.minimize_window()
browser.close()