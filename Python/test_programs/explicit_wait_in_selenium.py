'''
Created on Oct 19, 2019

@author: rajesh
'''

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path = "H:\Drivers\chromedriver.exe")
ac = ActionChains(driver)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
wait = WebDriverWait(driver, 50)
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#Tabbed > a > button")))
click_obj = driver.find_element_by_css_selector("#Tabbed > a > button")
ac.click(click_obj).perform()
handles = driver.window_handles
driver.switch_to.window(handles[2])







