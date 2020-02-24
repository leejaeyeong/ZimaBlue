from selenium import webdriver
import os 
# Create a new cromedriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
# Go to www.google.com
driver.get("https://lib.koreatech.ac.kr/#/")
# Saves a .png file with name my_screenshot_name to the directory that
# you are running the program from.
screenshot_name = "my_screenshot_name.png"
driver.save_screenshot(screenshot_name)


# ver80 이상에서 동작 
#https://chromedriver.chromium.org/downloads