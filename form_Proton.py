from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from names import first_names, last_names, mail_usernames
from mail_verification import get_code
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

sleep(5)
driver.switch_to.frame(0)

username = get_username(first_names[randint(0, len(first_names) - 1)],
                        last_names[randint(0, len(last_names) - 1)])
driver.find_element_by_id('username').send_keys(username)

driver.switch_to.default_content()

password = get_password()
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('passwordc').send_keys(password)

driver.switch_to.frame(1)

driver.find_element_by_id('notificationEmail').send_keys('generalmarkin@yahoo.com')  # email de notificações

driver.find_element_by_name('submitBtn').click()

sleep(5)

driver.find_element_by_id('id-signup-radio-email').click()

email_verification = driver.find_element_by_id('emailVerification')
mail_username = mail_usernames[randint(0, len(mail_usernames) - 1)]


email_verification.send_keys('{}@yahoo.com'.format(mail_username))  # email para receber código de verificação
email_verification.send_keys(Keys.RETURN)

sleep(0.5)

while driver.find_element_by_xpath('//*[@id="verification-panel"]/form[1]/div[2]/p/strong').text != 'Verification code sent':
    email_verification.clear()
    mail_username = mail_usernames[randint(0, len(mail_usernames) - 1)]
    email_verification.send_keys('{}@yahoo.com'.format(mail_username))  # email para receber código de verificação
    email_verification.send_keys(Keys.RETURN)

    sleep(0.5)

sleep(15)

driver.find_element_by_xpath('//*[@id="codeValue"]').send_keys(get_code(mail_username))
driver.find_element_by_xpath('//*[@id="verification-panel"]/p[3]/button').click()
