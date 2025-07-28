from selenium import webdriver
from selenium.webdriver.common.by import By

def check_saucedemo_elements():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button') # в условии задачи кнопка называется submit, но я переименовала в login (<input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login">). надеюсь, так можно было))

    if username and password and login_button:
        print('элементы найдены')
    else:
        print('ошибка: какие-то элементы отсутствуют')

    driver.quit() # гугол подсказал, что quit можно добавить для закрытия браузера и завершения сессии webdriver

check_saucedemo_elements() 
