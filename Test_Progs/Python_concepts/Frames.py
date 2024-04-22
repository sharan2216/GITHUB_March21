from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
time.sleep(3)
# alt=driver.switch_to.alert
# alt_text=alt.text
# print(alt_text)
# alt.accept()
driver.find_element(By.XPATH,"//button[@id='search_button']").click()
# driver.find_element(By.XPATH,"//div[@class='sc-ifAKCX gLwVlD']").click()
time.sleep(2)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
time.sleep(2)
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='gsi_892028_685616']"))
ele1=driver.find_element(By.XPATH,'//*[@id="container"]/div')
ele1.click()
# driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]').click()
time.sleep(300)
