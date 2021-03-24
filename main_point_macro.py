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


def get_nick():
    return driver.find_element_by_css_selector("#default_top > div.header-member > div:nth-child(1) > a").text


def get_data(url_css, brand_css):
    urls = driver.find_elements_by_css_selector(url_css)
    brands = driver.find_elements_by_css_selector(brand_css)

    for i in range(len(urls)):
        urls[i] = urls[i].get_attribute('href')
        brands[i] = brands[i].text

    return urls, brands


def get_comment(word):
    if (ord(word[-1]) - 44032) % 28 == 0:
        return "{brand}가 {brand}했다".format(brand=word)
    return "{brand}이 {brand}했다".format(brand=word)


def write_comment(text_css, area_css, submit_css, comment):
    while True:
        try:
            driver.find_element_by_css_selector(text_css).click()
        except:
            time.sleep(0.1)
            continue
        else:
            break

    text_area = driver.find_element_by_css_selector(area_css)
    text_area.click()
    text_area.send_keys(comment)

    driver.find_element_by_css_selector(submit_css).send_keys(Keys.ENTER)
    driver.switch_to.alert.accept()
    time.sleep(1)


def click_cool(cool_css):
    try:
        driver.find_element_by_css_selector(cool_css).click()
    except:
        driver.switch_to.alert.accept()


def check_commented(comment_css):
    if nick in driver.find_element_by_css_selector(comment_css).text:
        time.sleep(10)
        return True
    return False


def check_time(write_time):
    while True:
        if time.time() - write_time > 10:
            return
        time.sleep(0.1)


def news():
    page_num = 1
    write_time = 0

    url_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.news > div > ul > li > div.articleImg > a"
    brand_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.news > div > ul > li > div.articleInfo.info > div.info > b > a > span"
    comment_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div"
    text_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormTriger > span"
    area_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.cForm > textarea"
    submit_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.btnGroup > div > input.submit.mcmment-command-submit-comment"
    cool_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div.content-wrapper.article.wrapper > div > div.replyBoard-box.box > div.postRight > div > div > ul > li > div.info > div.score.ui-require-all > a.ui-require-cool"

    while True:
        driver.get("https://magazine.musinsa.com/index.php?m=news&p=%d" % page_num)
        page_num += 1

        urls, brands = get_data(url_css, brand_css)

        for i in range(len(urls)):
            driver.get(urls[i])

            if check_commented(comment_css):
                return

            comment = get_comment(brands[i])

            check_time(write_time)

            write_comment(text_css, area_css, submit_css, comment)
            write_time = time.time()

            click_cool(cool_css)


def magazine():
    page_num = 1
    write_time = 0

    url_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div > div > ul > li > div.articleImg > a"
    brand_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.main-content > div > div > ul > li > div.articleInfo > div.info > b > a > span"
    comment_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div"
    text_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormTriger > span"
    area_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.cForm > textarea"
    submit_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.btnGroup > div > input.submit.mcmment-command-submit-comment"
    cool_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div:nth-child(3) > div > div > div.replyBoard-box.box > div.postRight > div > div > ul > li:nth-child(5) > div.info > div.score.ui-require-all > a.ui-require-cool"

    while True:
        driver.get("https://magazine.musinsa.com/?m=magazine&sort=dataDate&p=%d" % page_num)
        page_num += 1

        urls, brands = get_data(url_css, brand_css)

        for i in range(len(urls)):
            driver.get(urls[i])

            if check_commented(comment_css):
                return

            comment = get_comment(brands[i])

            check_time(write_time)

            write_comment(text_css, area_css, submit_css, comment)
            write_time = time.time()

            click_cool(cool_css)


def lookbook():
    page_num = 1
    write_time = 0

    url_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.wrapper > div > div.boxed-list-wrapper > div.list-box.box > ul > li > div.articleImg > a"
    brand_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.wrapper > div > div.boxed-list-wrapper > div.list-box.box > ul > li > div.articleInfo > div.category > span"
    comment_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.article.wrapper > div.replyBoard-box.box > div.postRight > div"
    text_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.article.wrapper > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormTriger > span"
    area_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.article.wrapper > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.cForm > textarea"
    submit_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.article.wrapper > div.replyBoard-box.box > div.postRight > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.btnGroup > div > input.submit.mcmment-command-submit-comment"
    cool_css = "#wrapper > div.bottom-column.column.clearfix > div.main-content-wrapper > div.content-wrapper.article.wrapper > div.replyBoard-box.box > div.postRight > div > div > ul > li > div.info > div.score.ui-require-all > a.ui-require-cool"

    while True:
        driver.get("https://magazine.musinsa.com/index.php?m=lookbook&sort=dataDate&p=%d" % page_num)
        page_num += 1

        urls, brands = get_data(url_css, brand_css)

        for i in range(len(urls)):
            driver.get(urls[i])

            if check_commented(comment_css):
                return

            comment = get_comment(brands[i])

            check_time(write_time)

            write_comment(text_css, area_css, submit_css, comment)
            write_time = time.time()

            click_cool(cool_css)


def update():
    page_num = 1
    write_time = 0

    while True:
        driver.get("https://store.musinsa.com/app/news/lists?page=%d" % page_num)
        page_num += 1

        contents = driver.find_elements_by_css_selector("body > div.wrap > div.right_area.news_list > div.news_contents")

        for content in contents:
            try:
                content.find_element_by_css_selector("#contentComment > p > a").click()
            except:
                continue

            content.find_element_by_css_selector("div > div > div > ul > div.gWarea > form > div.cFormTriger > span").click()

            if nick in content.find_element_by_css_selector("div.comment").text:
                return

            brand = content.find_element_by_css_selector("div.box_news > div.list-box.box > ul > li > div.li_inner > div.article_info > p.item_title > a").text
            comment = get_comment(brand)

            text_area = content.find_element_by_css_selector("div > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.cForm > textarea")
            text_area.click()
            text_area.send_keys(comment)

            while True:
                if time.time() - write_time > 10.1:
                    break
                time.sleep(0.1)

            content.find_element_by_css_selector("div > div > div > ul > div.gWarea > form > div.cFormBox.groupType-cForm > div.btnGroup > div > input.submit.mcmment-command-submit-comment").send_keys(Keys.ENTER)
            driver.switch_to.alert.accept()
            time.sleep(1)

            write_time = time.time()

            try:
                content.find_element_by_css_selector("div > div > div > ul > li > div.info > div.score.ui-require-all > a.ui-require-cool").click()
            except:
                continue


login()
nick = get_nick()
news()
magazine()
lookbook()
update()

driver.close()