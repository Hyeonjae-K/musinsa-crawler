from selenium import webdriver
from selenium.webdriver.common.keys import Keys


productUrl = input("Enter the product url: ")
# productSize = input("Enter the product size: ")
# openTime = input("Enter the time by 24 hour system(hhmm): ")

timeDriver = webdriver.Chrome()
timeDriver.get("https://time.navyism.com/")

inputBar = timeDriver.find_element_by_css_selector("#inputhere")
inputBar.click()
inputBar.send_keys(productUrl)
inputBar.send_keys(Keys.ENTER)