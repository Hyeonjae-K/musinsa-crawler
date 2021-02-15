from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

productUrl = input("Enter the product url: ")
# productSize = input("Enter the product size: ")
openTime = int(input("Enter the open time by 24 hour system(hhmm): "))
loginTime = int(input("Enter the number of minutes to login(<=60): "))

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
with open("info.txt", "r", encoding="utf-8") as f:
    mainDriver.find_element_by_css_selector("#default_top > div.header-member > button").click()
    id = f.readline().strip()
    pw = f.readline().strip()
    inputId = mainDriver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.id > input")
    inputId.send_keys(id)
    inputPw = mainDriver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.pass > input")
    inputPw.send_keys(pw)
    inputPw.send_keys(Keys.ENTER)


# timeDriver.close()