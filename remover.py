## Insta silent removerpy

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

get_username= input('Please type your username:')
get_password= input('Please type your password:')


# get the executable gecko driver for running firefox
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# If we cannot find what we are looking for, selenium will wait 5 secs and try again
browser.implicitly_wait(5) 

instagram_link= "https://www.instagram.com/"
profile_link = instagram_link + get_username
# go to the instagram page --> this is the print("hello world") for selenium
browser.get(instagram_link)

# get the username box
username_input = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
# alternatively; username_input = browser.find_element("name", "username")

# get the password box
password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
# alternatively; password_input = browser.find_element("name", "password")

# locate the login button
login_button =browser.find_element(By.XPATH, '//button[@type="submit"]')

# login to instagtam
username_input.send_keys(get_username)
password_input.send_keys(get_password)
login_button.click()

# direct to the user profile
sleep(2) # we need a buffer time to direct while logged in, otherwise we load a brand new page...
browser.get(profile_link) 

# browser.close()