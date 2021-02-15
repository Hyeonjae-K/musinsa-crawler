from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def crawl_now_ranking():
    with open("now_ranking.txt", "w", encoding="utf-8") as f:
        for pageNum in range(1, 101):
            driver.get(
                "https://search.musinsa.com/ranking/best?period=now&mainCategory=&subCategory=&leafCategory=&price=&golf=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=%d&viewType=small&device=&priceMin=&priceMax=" % pageNum)
            titles = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a")
            prices = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.article_info > p.price")
            images = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.list_img > a > img")
            brands = driver.find_elements_by_css_selector("#goodsRankList > li > div.li_inner > div.article_info > p.item_title > a")
            for i in range(len(titles)):
                titleStr = str(titles[i].get_attribute("title")).strip()
                priceStr = str(prices[i].text)
                imageStr = str(images[i].get_attribute("data-original")).strip()
                brandStr = str(brands[i].text).strip()
                if priceStr.count("원") == 2:
                    priceStr = priceStr.replace(priceStr[:priceStr.find("원") + 1], "").strip()
                f.write(brandStr + "`" + titleStr + "`" + priceStr + "`" + imageStr + "\n")


driver = webdriver.Chrome()

driver.close()