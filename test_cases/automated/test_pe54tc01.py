# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPe54tc01():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pe54tc01(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1376, 754)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("sample33")
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input").click()
    login = self.driver.find_element(By.CLASS_NAME, 'dropbtn').text
    assert 'Hello' in login
