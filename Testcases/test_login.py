from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from Pageobjects.Loginpage import loginpage
from Utilities.customLog import Loggen

class Test_001_login:

    base_url="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    username="Admin"
    password="admin123"
    logger=Loggen.loggen()

    def test_titlehomepage(self,setup):
        self.logger.info("*******Test_001_login************")
        self.logger.info("*******************This is first login***************")
        self.driver=setup
        self.driver.get(self.base_url)
        act_homepage=self.driver.title
        time.sleep(3)
       # self.driver.maximize_window()
        if act_homepage=="OrangeHRM":
            assert True
            self.logger.info("***************Login successful**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_titlehomepage.png")
            self.logger.info("*************************Login not successful******************")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp=loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.loginbutten()
        act_title=self.driver.title

        if act_title=="OrangeHRM":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False






