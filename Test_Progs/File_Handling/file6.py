from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time


wb=load_workbook("C:\\Users\\shashi\\Desktop\\ExcelSheet.xlsx")
sh=wb['DATA']
sheetrow=[]

driver = webdriver.Chrome()
driver.get("https://qavbox.github.io/demo/webtable/")
driver.maximize_window()
time.sleep(3)
table=driver.find_element(By.XPATH,"//table[@id='table01']")
rows=driver.find_elements(By.XPATH,"//table[@id='table01']//tbody/tr")
col=driver.find_elements(By.XPATH,"//table[@id='table01']//tbody/tr/td")
cells=driver.find_elements(By.TAG_NAME,"td")
print("length of rows is ",len(rows))
for i in range(len(rows)):
    for j in range(len(col)):
        sheetrow.append(cells[j].text)
wb.save("C:\\Users\\shashi\\Desktop\\ExcelSheet.xlsx")





