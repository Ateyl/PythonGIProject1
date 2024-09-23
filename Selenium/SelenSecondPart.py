from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random



driver = webdriver.Chrome()
driver.get('https://www.google.com/')
# driver.set_window_size(1920, 1080)
# print(driver.get_window_position())
# print(driver.get_window_size().get('width'))
# driver.set_window_position(0,0)
# print(driver.get_window_rect())
# driver.fullscreen_window()
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
# driver.minimize_window()
# time.sleep(3)

# driver.save_screenshot('main.png')

div = driver.find_element(By.CSS_SELECTOR, '#CXQnmb > div > div > div.GZ7xNe > div')
# div.screenshot('main.png')
time.sleep(2)
# print(driver.current_url)
google = driver.current_window_handle
driver.switch_to.new_window('window')
driver.get('https://github.com/')
github = driver.current_window_handle
time.sleep(2)
driver.switch_to.new_window(google)
time.sleep(2)
print(driver.window_handles)