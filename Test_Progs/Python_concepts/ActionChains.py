from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(3)
act=ActionChains(driver)
blogmenu=driver.find_element(By.XPATH,"//span[@id='blogsmenu']")
blogmenu.click()
seleniumbyarunOption = driver.find_element(By.XPATH,"//span[text()='SeleniumByArun']")


