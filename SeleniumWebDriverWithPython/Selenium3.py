from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon
from Selenium2 import make_screenshot # importowanie z pliku chce się uruchomić zawsze, żeby teo uniktnąć trzeba dodać do selenium 2 warunek if __name__ == '__main__':

def czekaj_na_id(element_id):
    timeout = 5
    timeout_message = f'Element o ID {element_id} nie pojawił się w czasie {timeout} s.'
    lokalizator = (By.ID, element_id)
    znaleziono = excon.visibility_of_element_located(lokalizator)    #sprawdzamy, czy element jest
    oczekiwator = WebDriverWait(driver, timeout)    #jak długo czekac i gdzie
    return oczekiwator.until(znaleziono, timeout_message)    #zwrotka

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

try: #wykonaj tray
    login_button = czekaj_na_id('login-button')
except TimeoutException: #wykonaj except
    print('Nie znaleziono')
    raise
else: #jeżeli Ci sie nie uda except to zrób else
    print('znaleziono')
finally: # fykonaj na samym końcu niezależnie od w/w

    make_screenshot(driver)
    driver.quit()