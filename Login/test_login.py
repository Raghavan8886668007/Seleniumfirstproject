from selenium import webdriver
from selenium.webdriver import Chrome
import pytest

def test_login():
    path = "D://python-3.6.5//chromedriver_win32 (2)//chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
    driver.find_element_by_xpath("//input[@type='email']").send_keys("sraghavan43@gmail.com")
    driver.find_element_by_xpath("//input[@type ='password']").send_keys("Akhil@007")
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    driver.maximize_window()
