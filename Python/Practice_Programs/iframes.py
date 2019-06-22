'''
Created on Apr 17, 2019

@author: rajesh
'''

from selenium import webdriver

driver = webdriver.Chrome("H:\\chromedriver.exe")
driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/')

driver.find_element_by_css_selector('a[href="/frames"]').click()

driver.find_element_by_css_selector('#content > div > ul > li:nth-child(1) > a').click()