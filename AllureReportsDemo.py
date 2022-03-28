'''
Created on Mar 27, 2022

@author: Cristina
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        
        try:
            self.driver = webdriver.Chrome(executable_path='C:\\Users\\Cristina\\Downloads\\chromedriver_win32\\chromedriver_99.0.4844.51.exe')
            self.driver.get("https://www.emag.ro/")
            status = self.driver.find_element(by=By.XPATH, value = "//img[@alt='eMAG']").is_displayed()
            
            if status == True:
                assert True
            else:
                assert False
                
            self.driver.close()
            
        except:
            print("Element not found!")
            self.driver.quit()
            assert False
               
    @allure.severity(allure.severity_level.NORMAL)      
    def test_listemployees(self):
        
        pytest.skip("skipping this test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
             
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\Cristina\\Downloads\\chromedriver_win32\\chromedriver_99.0.4844.51.exe')
        self.driver.get("https://www.emag.ro/")
        
        self.driver.find_element(by=By.ID, value = 'my_account').click()
        self.driver.find_element(by=By.ID, value = 'user_login_email').send_keys("cristina.codoban82@gmail.com")
        self.driver.find_element(by=By.ID, value='user_login_continue').click()
        allure.attach(self.driver.get_screenshot_as_png(),name="LoginFaliedScreenshot",
                          attachment_type=AttachmentType.PNG)
        self.driver.find_element(by=By.ID, value = 'user_login_password').send_keys("Pitic1982")
        self.driver.find_element(by=By.ID, value='user_login_continue').click()
                    
        elementIsPresent = self.driver.find_element(by=By.XPATH, value="span[contains(text(),'Laptop, Tablete & Telefoane')]").is_displayed()
        
        if elementIsPresent == True:
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="LoginFaliedScreenshot1",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
                
      
