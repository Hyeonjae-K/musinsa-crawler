from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://store.musinsa.com/app/")


def login():
    with open('./info.txt', 'r', encoding='UTF-8') as f:
        my_id = f.readline().strip()
        my_pw = f.readline().strip()

    driver.find_element_by_css_selector("#default_top > div.header-member > button").click()

    id_input = driver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.id > input")
    id_input.click()
    id_input.send_keys(my_id)

    pw_input = driver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.pass > input")
    pw_input.click()
    pw_input.send_keys(my_pw)

    driver.find_element_by_css_selector("body > div.bottom-column.column.clearfix.n-member-area > div > div.loginBoxV3 > form > span.submit.submitWBOX > input[type=submit]").click()


login()

driver.close()