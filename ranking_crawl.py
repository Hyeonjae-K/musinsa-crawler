from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
products = {}
f = open("test.txt", "w", encoding="utf-8")
for pagenum in range(1, 101):
    driver.get("https://search.musinsa.com/ranking/best?period=now&mainCategory=&subCategory=&leafCategory=&price=&golf=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=%d&viewType=small&device=&priceMin=&priceMax=" % pagenum)
    titles = driver.find_elements_by_css_selector("p.list_info > a")
    for i in range(len(titles)):
        f.write(str(titles[i].get_attribute("title")) + "\n")


#driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()