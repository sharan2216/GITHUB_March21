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
blogsmenu=driver.find_element(By.XPATH,"//span[@id='blogsmenu']")
blogsmenu.click()
time.sleep(2)
seleniumbyarunOption = driver.find_element(By.XPATH,"//span[text()='SeleniumByArun']")
# act.move_to_element(blogsmenu).move_to_element(seleniumbyarunOption).key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()
# time.sleep(5)
act.move_to_element(blogsmenu).move_to_element(seleniumbyarunOption).key_down(Keys.CONTROL).send_keys("a").key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys("v").perform()