from selenium import webdriver
import re
from time import sleep


def get_code():
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://login.yahoo.com/')

    driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('coronelmusk')
    driver.find_element_by_xpath('//*[@id="login-signin"]').click()

    sleep(2)

    driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('G3n3r@l')
    driver.find_element_by_xpath('//*[@id="login-signin"]').click()

    sleep(3)

    driver.find_element_by_xpath('//*[@id="header-nav-bar"]/li[1]/a').click()

    sleep(3)

    element = driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/a/div/div[2]/div[1]/div[2]/div')
    code = re.findall(r'[0-9]+', element.text)[0]
    return code
