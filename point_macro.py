from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://store.musinsa.com/app/")
f = open('./info.txt', 'r', encoding='UTF-8')


def login():
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


def open_page():
    driver.get("https://magazine.musinsa.com/index.php?m=magazine&uid=15890")


def write_comment(comment, count):
    while True:
        try:
            comment_input = driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormTriger > span")
        except:
            continue
        else:
            comment_input.click()
            break

    comment_input = driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.cForm > textarea")
    comment_input.click()
    comment_input.send_keys(comment + str(count))

    driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.btnGroup > div > input.submit.mcmment-command-submit-comment").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.refresh()


def click_cool():
    time.sleep(1)
    driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > li:nth-child(5) > div.info > div.score.ui-require-all > a.ui-require-cool").click()
    time.sleep(1)
    driver.refresh()


def delete_comment():
    driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > li:nth-child(6) > div.info > label").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > li:nth-child(6) > div.info > label > div > a:nth-child(2)").click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.refresh()


def run_macro():
    comment = f.readline().strip()
    count = 0

    write_comment(comment, count)
    click_cool()
    time.sleep(4)

    while True:
        count += 1
        write_comment(comment, count)
        click_cool()
        delete_comment()


login()
open_page()
run_macro()

# driver.close()