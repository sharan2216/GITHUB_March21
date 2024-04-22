
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Test_Progs.NEW_PROGS.dropdown import driver

wait= WebDriverWait(driver,10)
alt=wait.until(EC.alert_is_present())
# alt.authenticateUsing(new UserAndPassword(**username**,**password**))