from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome()
products = {}
f = open("test.txt", "w", encoding="utf-8")
for pagenum in range(1, 101):
    driver.get("https://search.musinsa.com/ranking/best?period=now&mainCategory=&subCategory=&leafCategory=&price=&golf=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=%d&viewType=small&device=&priceMin=&priceMax=" % pagenum)
    titles = driver.find_elements_by_css_selector("p.list_info > a")
    prices = driver.find_elements_by_css_selector("p.price")
    for i in range(len(titles)):
        titleStr = str(titles[i].get_attribute("title")).strip()
        priceStr = str(prices[i].text)
        if priceStr.count("원") == 2:
            priceStr = priceStr.replace(priceStr[:priceStr.find("원") + 1], "").strip()
        if(titleStr != ''):
            f.write(titleStr + " " + priceStr + "\n")