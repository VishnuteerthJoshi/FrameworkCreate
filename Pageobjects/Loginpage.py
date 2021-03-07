from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

class loginpage():
    textbox_username_id="txtUsername"
    textbox_password_id="txtPassword"
    butten_loginbutton_id="btnLogin"
    butten_logoutbutten_linktext="Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def loginbutten(self):
        self.driver.find_element_by_id(self.butten_loginbutton_id).click()

    def logoutbutten(self):
        self.driver.find_element_by_linktext(self.butten_logoutbutten_linktext).click()



