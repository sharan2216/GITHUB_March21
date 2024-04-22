from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://demo.opencart.com/admin/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"input-username").send_keys("demo")
driver.find_element(By.ID,"input-password").send_keys("demo")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@type='submit']").click()
# time.sleep(4)
# alt=driver.switch_to.alert
# time.sleep(3)
# alt.accept()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='btn-close']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[contains(text(),' Sales')]").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Orders')]").click()
# driver.find_element(By.XPATH,"//form[@id='form-order']//tr[3]//td[1]").click()
time.sleep(3)
expected_name='Luis Lopez'
customer_names=driver.find_elements(By.XPATH,"//form[@id='form-order']//tr//td[4]")
i=0
for cust in customer_names:
    if cust.text.__eq__(expected_name):
        xpath_text="//form[@id='form-order']//tr["+str(i)+"]/td[1]"
        driver.find_element(By.XPATH,xpath_text).click()
        time.sleep(3)
        print(xpath_text)
    i=i+1
    # ftext=driver.find_element(By.XPATH,"//form[@id='form-order']//tr[i]//td[3]".text)
    # print(ftext)
time.sleep(5)