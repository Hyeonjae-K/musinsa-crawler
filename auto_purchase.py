from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = open("info.txt", "r", encoding="utf-8")
productUrl = f.readline().strip()
productSize = f.readline().strip()
openTime = int(f.readline().strip())
loginTime = int(f.readline().strip())
loginId = f.readline().strip()
loginPw = f.readline().strip()
f.close()

if openTime % 100 < loginTime:
    loginTime = openTime - 40 - loginTime
else:
    loginTime = openTime - loginTime

timeDriver = webdriver.Chrome()
timeDriver.get("https://time.navyism.com/")

inputBar = timeDriver.find_element_by_css_selector("#inputhere")
inputBar.click()
inputBar.send_keys(productUrl)
inputBar.send_keys(Keys.ENTER)

while True:
    getTime = timeDriver.find_element_by_css_selector("#time_area").text
    getTime = int(getTime[getTime.find("일") + 2:getTime.find("분")].replace("시 ", ""))
    if getTime >= loginTime:
        break

mainDriver = webdriver.Chrome()
mainDriver.get(productUrl)
mainDriver.find_element_by_css_selector("#default_top > div.header-member > button").click()
inputId = mainDriver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.id > input")
inputId.send_keys(loginId)
inputPw = mainDriver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.pass > input")
inputPw.send_keys(loginPw)
inputPw.send_keys(Keys.ENTER)

mainDriver.find_element_by_css_selector(productSize).click()

while True:
    getTime = timeDriver.find_element_by_css_selector("#time_area").text
    getTime = int(getTime[getTime.find("일") + 2:getTime.find("분")].replace("시 ", ""))
    if getTime >= openTime:
        break

mainDriver.find_element_by_css_selector("#product_order_info > div.explan_product.option_select_section.opt-select-box > div.box-btn-buy.wrap-btn-buy > div.btn_buy > a").send_keys(Keys.ENTER)
time.sleep(0.1)
mainDriver.find_element_by_css_selector("#payment_info_area > ul:nth-child(9) > li.cell_discount_detail.last > p:nth-child(1) > label > input[type=checkbox]").click()
mainDriver.find_element_by_css_selector("#btn_pay").send_keys(Keys.ENTER)