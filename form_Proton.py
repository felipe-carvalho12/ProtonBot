from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lists import mail_usernames
from mail_verification import get_yahoo_code
from time import sleep
from random import randint


def get_email(username, password):
    driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
    driver.get('https://mail.protonmail.com/create/new?language=en')

    sleep(5)

    driver.switch_to.frame(0)

    driver.find_element_by_id('username').send_keys(username)

    driver.switch_to.default_content()

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

    sleep(10)

    driver.find_element_by_xpath('//*[@id="codeValue"]').send_keys(get_yahoo_code(mail_username))
    driver.find_element_by_xpath('//*[@id="verification-panel"]/p[3]/button').click()
