from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from phoneNumber import get_phone_number
driver = webdriver.Chrome(r'C:\Users\felip\PycharmProjects\python_projects\Twitter Bot\chromedriver.exe')
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=pt-BR&dsh=S1829548773%3A1595960178288392&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")


def get_random(digits):
    rdm = ''
    for i in range(0, digits):
        rdm += str(randint(0, 9))
    return rdm


inputFirstName = driver.find_element_by_name('firstName')
inputLastName = driver.find_element_by_name('lastName')
inputUsername = driver.find_element_by_name('Username')
inputPassword = driver.find_element_by_name('Passwd')
inputConfirmPassword = driver.find_element_by_name('ConfirmPasswd')

id = get_random(5)
firstName = 'Mark'
lastName = 'Zuckerberg'
username = firstName.lower() + lastName.lower() + id
password = '@Aa' + id

# preenchendo o formulário
inputFirstName.send_keys(firstName)
inputLastName.send_keys(lastName)
inputUsername.send_keys(username)
inputPassword.send_keys(password)
inputConfirmPassword.send_keys(password)
inputConfirmPassword.send_keys(Keys.RETURN)

sleep(4)  # esperando a página carregar

inputPhoneNumber = driver.find_element_by_id('phoneNumberId')
inputPhoneNumber.send_keys(get_phone_number())
inputPhoneNumber.send_keys(Keys.RETURN)
