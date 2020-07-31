from selenium import webdriver
import re
from time import sleep


def get_code(username):
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://login.yahoo.com/')

    driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="login-signin"]').click()

    sleep(2)

    driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('G3n3r@l')
    driver.find_element_by_xpath('//*[@id="login-signin"]').click()

    sleep(3)

    driver.find_element_by_xpath('//*[@id="header-nav-bar"]/li[1]/a').click()

    sleep(3)

    code = re.findall(r'is: (.+?)<', driver.page_source)[0]

    return code
