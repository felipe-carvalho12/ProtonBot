from selenium import webdriver
from selenium.webdriver.support.ui import Select
from mail_verification import get_proton_code
from time import sleep


def get_twitter_accounts(username, email, password):
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://twitter.com/i/flow/signup')

    sleep(2)

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

    sleep(2)

    driver.find_element_by_tag_name('span').click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[1].click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[13].click()

    sleep(2)

    driver.find_element_by_name('verfication_code').send_keys(get_proton_code(username, password))

    driver.find_elements_by_tag_name('span')[1].click()

    sleep(2)

    driver.find_element_by_name('password').send_keys(password)

    driver.find_element_by_tag_name('span').click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[2].click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[2].click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[2].click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[2].click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[8].click()

    sleep(2)

    driver.find_elements_by_tag_name('span')[8].click()
