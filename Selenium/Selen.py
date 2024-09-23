from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://github.com/')

email = driver.find_element('id', 'hero_user_email')
email.send_keys('Artjom21@exmple.com')
email.send_keys(Keys.ENTER)

def waiter(timeout, selector, selector_value):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((selector, selector_value))
        )
        return element
    except:
        return None

element = waiter(10, By.XPATH, '//*[@id="email-container"]/div[2]/button')

if element is not None:
    element.click()


#
# email = driver.find_element('partial link text', '    Download GitHub Mobile ')
# email.click()
# time.sleep(5)
# waiter(10, By.XPATH, '//*[@id="email-container"]/div[2]/button')

# continue_btn = driver.find_element('xpath', '//*[@id="email-container"]/div[2]/button')
# continue_btn.click()
time.sleep(5)

# print(driver.name)
# print(driver.title)
# print(driver.page_source.encode())
# driver.quit()
# driver.close() #закроет вкладку#
