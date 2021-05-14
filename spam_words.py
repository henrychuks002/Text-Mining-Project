#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:45:18 2021

@author: Henry Chuks
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import time

opt = Options()
opt.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
driver.maximize_window()
driver.get('https://damngoodwriters.com/post/spam-trigger-words')
driver.implicitly_wait(10)
time.sleep(5)

words = []
for c in range(35,473):
    try:
        find_words = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[1]/p['+str(c)+']') 
    except StaleElementReferenceException:
        find_words = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[1]/p['+str(c)+']') 
    words.append(find_words.text)

with open("Word.txt", "w") as f:
    for word in words:
        f.write(word+', ')
    
print('Done')