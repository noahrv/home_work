from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

if username and password and login_button:
    print('элементы найдены')
else:
    print('ошибка: какие-то элементы отсутствуют')

driver.quit()
