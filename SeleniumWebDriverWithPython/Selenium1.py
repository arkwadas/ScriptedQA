from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https:/google.com')

time.sleep(1)
print('strona :', driver.title)

# button1_accept = driver.find_element(by= 'id', value= 'L2AGLb')
button1_accept = driver.find_element(by= 'id', value= 'L2AGLb').click()
time.sleep(1)

textarea_googleFinder = driver.find_element(by= 'id', value= 'APjFqb')
time.sleep(1)

textarea_googleFinder.send_keys('Koduj z pythonem')
textarea_googleFinder.send_keys(Keys.RETURN)

driver.get_screenshot_as_file('Selenium01.png')

time.sleep(1)

# search_button1 = driver.find_element(by= 'name', value= 'btnK')
# search_button1.submit()
# time.sleep(1)

# print(button1_accept)
# print(type)

# button1_accept.click()
# time.sleep(1)

driver.quit()