from selenium import webdriver
from selenium.webdriver.common.keys import Keys


productUrl = input("Enter the product url: ")
# productSize = input("Enter the product size: ")
openTime = int(input("Enter the open time by 24 hour system(hhmm): "))
loginTime = int(input("Enter the number of minutes to login(<60): "))

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
    print(getTime)
    if getTime >= loginTime:
        break

# timeDriver.close()