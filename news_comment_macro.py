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


def open_news_page(page_num):
    driver.get("https://magazine.musinsa.com/index.php?m=news&p=%d" % page_num)


def get_data():
    data = {}
    urls = driver.find_elements_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.news > div > ul > li > div.articleImg > a")
    brands = driver.find_elements_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.news > div > ul > li > div.articleInfo.info > div.info > b > a > span")

    for i in range(len(urls)):
        data[urls[i].get_attribute('href')] = brands[i].text

    return data


def check_last_word(word):
    if (ord(word[-1]) - 44032) % 28 == 0:
        return False
    return True


def write_comment(comment):
    while True:
        try:
            driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormTriger > span").click()
        except:
            continue
        else:
            break

    comment_input = driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.cForm > textarea")
    comment_input.click()
    comment_input.send_keys(comment)

    driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.btnGroup > div > input.submit.mcmment-command-submit-comment").send_keys(Keys.ENTER)
    driver.switch_to.alert.accept()
    time.sleep(1)


def click_cool():
    driver.find_element_by_css_selector("#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > li > div.info > div.score.ui-require-all > a.ui-require-cool").click()


def run(data):
    write_time = 0

    for key in data:
        driver.get(key)

        if check_last_word(data[key]):
            comment = "{brand}".format(brand=data[key])
        else:
            comment = "{brand}".format(brand=data[key])

        while True:
            if time.time() - write_time > 10.1:
                break

        write_comment(comment)
        write_time = time.time()
        click_cool()


login()
for page in range(1, 101):
    open_news_page(page)
    data = get_data()
    run(data)
    time.sleep(10)

driver.close()