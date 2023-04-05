#python : DUP - Topic :NLP Selenium
#https://chromedriver.chromium.org/home

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

import selenium
selenium.__version__

#pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#driver and options
DRIVER_PATH = 'c:/chromeDriver/chromedriver111'
options = Options()
print(options)
options.headless = True
options.add_argument("--window-size=1920,1200")


#page1
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')


#page2
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.nintendo.com/")
print(driver.page_source)
driver.quit()


#au page
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
au = 'https://amity.edu/'
driver.get(au)
driver.title
driver.current_url

#https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html

driver.fullscreen_window()

driver.current_window_handle

from selenium.webdriver.common.by import By

all_links = driver.find_elements(By.TAG_NAME, 'a')
for i in all_links:  print(i)

#from selenium.webdriver.common.keys import Keys
elems = driver.find_elements(By.XPATH, "//a[@href]")
len(elems)
for elem in elems:    print(elem.get_attribute("href"))


elems = driver.find_elements(By.TAG_NAME,'a')
len(elems)
for elem in elems:
  href = elem.get_attribute('href')
  if href is not None:
    print(href)

elems = driver.find_elements(By.CLASS_NAME, "top_megamenu")
elems.length
len(elems)
for elem in elems:    print(elem.get_attribute("outerHTML"))

driver.refresh()
driver.get(au)

find_element(By.ID, '')
XP1 = driver.find_elements(By.XPATH,"//*[@id='admission1_repcoursebind_ctl00_lbldetails']")
XP1.text
type(XP1)
for x in XP1:    print(x.get_attribute("textContent"))


driver.find_element(By.CLASS_NAME, 'wow fadeInUp')

E1 = driver.find_element(By.ID, 'page-top')
E1.text
h1
h1 = driver.find_element(By.CLASS_NAME, 'someclass')
h1 = driver.find_element(By.XPATH, '//h1')
h1 = driver.find_element(By.XPATH, '/html/body/h1')
h1 = driver.find_element(By.ID, 'greatID')
driver.find_element(By.CLASS_NAME, 'wow fadeInDown')



#screenshot------
folder = 'C:/Users/du/Pictures/Screenshots'
driver.save_screenshot('C:/Users/du/Pictures/Screenshots/au.png')
#help(driver.save_screenshot)


find_element(By.ID, 'id')
find_element(By.NAME, 'name')
find_element(By.XPATH, 'xpath')
driver.find_element(By.XPATH, " ")
driver.find_elements(By.XPATH, " ")

driver.find_element(By.CLASS_NAME, " ")
driver.find_elements(By.CLASS_NAME, " ")