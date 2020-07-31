from selenium import webdriver
from selenium.webdriver.support.ui import Select


def get_twitter_accounts(username, email):
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://twitter.com/i/flow/signup')

    driver.implicitly_wait(2)

    driver.find_element_by_name('name').send_keys(username)

    driver.find_elements_by_tag_name('span')[6].click()

    driver.find_element_by_name('email').send_keys(email)

    month = driver.find_elements_by_tag_name('select')[0]
    select1 = Select(month)
    select1.select_by_visible_text('Janeiro')

    day = driver.find_elements_by_tag_name('select')[1]
    select2 = Select(day)
    select2.select_by_visible_text('1')

    year = driver.find_elements_by_tag_name('select')[2]
    select3 = Select(year)
    select3.select_by_visible_text('2001')

    driver.implicitly_wait(3)

    driver.find_element_by_class_name('css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1vsu8ta r-aj3cln r-icoktb r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr').click()
