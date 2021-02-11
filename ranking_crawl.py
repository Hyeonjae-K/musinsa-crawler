from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

driver = webdriver.Chrome()
Titles = []
Prices = []
Images = []

for pageNum in range(1, 3):
    driver.get("https://search.musinsa.com/ranking/best?period=now&mainCategory=&subCategory=&leafCategory=&price=&golf=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=%d&viewType=small&device=&priceMin=&priceMax=" % pageNum)
    titles = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a")
    prices = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.article_info > p.price")
    images = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.list_img > a > img")
    for i in range(len(titles)):
        titleStr = str(titles[i].get_attribute("title")).strip()
        priceStr = str(prices[i].text)
        imageStr = str(images[i].get_attribute("data-original")).strip()
        if priceStr.count("원") == 2:
            priceStr = priceStr.replace(priceStr[:priceStr.find("원") + 1], "").strip()
        Titles.append(titleStr)
        Prices.append(priceStr)
        Images.append(imageStr)
        print(imageStr)

with open("test.txt", "w", encoding="utf-8") as f:
    for i in range(len(Titles)):
        f.write(Titles[i] + "`" + Prices[i] + "`" + Images[i] + "\n")

driver.close()