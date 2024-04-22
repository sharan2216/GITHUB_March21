from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@class='signinbtn']").click()
time.sleep(3)
alt=driver.switch_to.alert
alt_text=alt.text
print(alt_text)
alt.dismiss()

driver.find_element(By.XPATH,"//input[@id='login1']").send_keys("selenium")
time.sleep(3)