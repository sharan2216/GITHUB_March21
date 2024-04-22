from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)

parent_window=driver.current_window_handle
print(parent_window)
time.sleep(3)

likedIn_link = driver.find_element(By.XPATH,"//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']")
likedIn_link.click()
time.sleep(3)

child_windows=driver.window_handles
for child in child_windows:
    if child!=parent_window:
        driver.switch_to.window(child)
        time.sleep(3)
        print(driver.title)
        time.sleep(3)
        driver.close()
driver.switch_to.window(parent_window)
print("Parent window title is :",driver.title)
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.close()

