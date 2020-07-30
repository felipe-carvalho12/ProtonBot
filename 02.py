driver = webdriver.Chrome(executable_path='./driver/chromedriver', chrome_options=options)

    url = 'http://protonmail.com/signup'

    def randomStringDigits(stringLength=13):
        # Generate a random string of letters and digits
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    rngusername = randomStringDigits(13)
    rngpassword = randomStringDigits(15)

    driver.get(url)

    time.sleep(4)

    driver.find_element_by_class_name('panel-heading').click()

    time.sleep(1)

    driver.find_element_by_id('freePlan').click()

    time.sleep(4)

    driver.switch_to_frame(0)

    time.sleep(3)

    driver.find_element_by_id('username').send_keys(rngusername)

    time.sleep(1)

    driver.switch_to.default_content()

    time.sleep(1)

    driver.find_element_by_id('password').send_keys(rngpassword)

    time.sleep(1)

    driver.find_element_by_id('passwordc').send_keys(rngpassword)

    time.sleep(1)

    driver.switch_to_frame(1)

    time.sleep(1)

    if notifymail == "x":
        notifymail = "mail@mail.com"
    else:
        pass
    driver.find_element_by_id('notificationEmail').send_keys(notifymail)

    time.sleep(1)

    driver.find_element_by_name('submitBtn').click()

    time.sleep(6)

    print('\033[31m' + "What type of verification do you want to use?" + '\033[0m')
    print('\033[31m' + "(1) Email verification" + '\033[0m')
    print('\033[31m' + "(2) Captcha verification" + '\033[0m')
    verifymethod = input('\033[31m' + "Enter Email Adress for Verification: " + '\033[0m')
    if verifymethod == "1":
        driver.find_element_by_id('id-signup-radio-email').click()

        time.sleep(1)

        driver.find_element_by_id('emailVerification').send_keys(verifymail)

        time.sleep(1)

        driver.find_element_by_class_name('codeVerificator-btn-send').click()

        time.sleep(3)
    elif verifymethod == "2":
        print('\033[31m' + "Please complete the captcha in your browser. " + '\033[0m')
        captchadone = input('\033[31m' + "Hit enter when captcha is complete" + '\033[0m')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/p[3]/button').click()

    print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
    print ('\033[31m' + "Your New Email Password is: "  + '\033[0m' , rngpassword)

    complete = "false"

    while (complete == "false"):
        complete_q = input('\033[31m' + "Did you complete the Verification process? y/n: " + '\033[0m')

        if complete_q == "y":
            driver.close()
            csvData = [[rngusername + '@protonmail.com', rngpassword]]
            with open('list.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
            csvFile.close()
            print ('\033[31m' + 'Great! We added you account details to the table.' + '\033[0m')
            complete = "true"

        else:
            print ('\033[31m' + 'Please try verifing and try again' + '\033[0m')
            time.sleep(1)
            complete = "false"
