from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from names import first_names, last_names
from time import sleep
from random import randint


def get_random(digits):
    rdm = ''
    for i in range(0, digits):
        rdm += str(randint(0, 9))
    return rdm


def get_username(name, surname):
    nm = name.lower().replace(' ', '')
    sn = surname.lower().replace(' ', '')
    return nm + sn + id_


def get_password():
    return 'G3n3r@l' + id_


driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
driver.get('https://mail.protonmail.com/create/new?language=en')

id_ = get_random(5)

sleep(3)
driver.switch_to.frame(0)

username = get_username(first_names[randint(0, len(first_names) - 1)],
                        last_names[randint(0, len(last_names) - 1)])
driver.find_element_by_id('username').send_keys(username)

driver.switch_to.default_content()

password = get_password()
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('passwordc').send_keys(password)

driver.switch_to.frame(1)

driver.find_element_by_id('notificationEmail').send_keys('generalmarkin@yahoo.com')

driver.find_element_by_name('submitBtn').click()

sleep(2)

driver.find_element_by_id('id-signup-radio-email').click()

driver.find_element_by_id('emailVerification').send_keys('coronelmusk@yahoo.com')
driver.find_element_by_id('emailVerification').send_keys(Keys.RETURN)
