from selenium import webdriver
import re
from time import sleep


def get_yahoo_code(username):
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://login.yahoo.com/')

    driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="login-signin"]').click()

    sleep(2)

    driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('G3n3r@l')
    driver.find_element_by_xpath('//*[@id="login-signin"]').click()

    sleep(3)

    driver.find_element_by_xpath('//*[@id="header-nav-bar"]/li[1]/a').click()  # indo para o yahoo mail

    sleep(3)

    code = re.findall(r'is: (.+?)<', driver.page_source)[0]  # selecionando o último código

    return code


def get_proton_code(username, password):
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://mail.protonmail.com/login')

    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_id('login_btn').click()

    sleep(6)

    code = re.findall(r'([0-9]+) é seu', driver.page_source)[0]

    return code
