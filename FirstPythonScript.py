'''
Created on Mar 13, 2022

@author: Cristina
'''

#!/usr/bin/python
# -*- coding: latin-1 -*-

from selenium import webdriver
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os,sys
from pickle import TRUE, FALSE

# Opening JSON file
f = open('Parameters.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

driver = webdriver.Chrome(executable_path='C:\\Users\\Cristina\\Downloads\\chromedriver_win32\\chromedriver_99.0.4844.51.exe')

driver.get('https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=categories%23compute&trk=33ffcbe8-beac-4ead-b902-a91ced7f226f&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|Solution|EEM|EN|Text|EU&s_kwcid=AL!4422!3!495118606976!e!!g!!amazon%20cloud&ef_id=Cj0KCQiAybaRBhDtARIsAIEG3kmEDKgPp0YVVMsFG96FN-fNdsB-kK2jS-AktqhIkHvkBVrs47_iv7saApUTEALw_wcB:G:s&s_kwcid=AL!4422!3!495118606976!e!!g!!amazon%20cloud')

try:
    
    #driver.implicitly_wait(10)
    
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']")))

    #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
    
    driver.find_element(by=By.XPATH, value="//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
    
except:
    
    print("Element not found!")
    driver.quit()

try:
    
    #driver.implicitly_wait(10)
    
    element = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH,"//input[@name='emailAddress']")))

    #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
    
    driver.find_element(by=By.XPATH, value="//input[@name='emailAddress']").send_keys("chrischaosster@gmail.com")
    
    driver.find_element(by=By.XPATH, value="//input[@name='fullName']").send_keys("cris account")
    
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Verify email address')]").click()
    
except:
    
    print("Element not found!")
    driver.quit()
    
main_window = driver.current_window_handle
parent = driver.window_handles[0]
#driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.CONTROL + 't')
#driver.find_element_by_tag_name('body').send_keys()    
try:

    driver.execute_script("window.open('');")
    driver.window_handles
    time.sleep(10)
    chld = driver.window_handles[1]
    #window_name = driver.window_handles[1]
    driver.switch_to.window(chld)
    time.sleep(10)
    driver.get('http://gmail.com')
   
except:
    print("Oops!", sys.exc_info()[0], "occurred.")
    driver.quit()
    
def elementExists(xPathParameter):
    exist = False
    element = driver.find_element(By,By.XPATH,value=xPathParameter)
    
    if element > 0:
        exist = True
    else:
        exist = False
        
    print(exist)

    return exist
    

try:
    
    #driver.implicitly_wait(10),
    
    element = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH,"//input[@type='email']")))

    #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
    
    driver.find_element(by=By.XPATH,value="//input[@type='email']").send_keys("chrischaosster@gmail.com")
       
    if elementExists("//div[@data-value='ro' and @tabindex='0']") == True: 
        driver.find_element(by=By.XPATH, value="//div[@data-value='ro' and @tabindex='0']").click()
        driver.find_element(by=By.XPATH,value="//input[@type='email']").send_keys("chrischaosster@gmail.com")
        driver.find_element(by=By.XPATH, value="//div[@data-value='en' and @tabindex='0']").click()
        time.sleep(500)
        driver.find_element(by=By.XPATH, value="//span[contains(text(),'Next')]").click()
    elif elementExists("//div[@data-value='en' and @tabindex='0']") == True:
        driver.find_element(by=By.XPATH, value="//span[contains(text(),'Next')]").click()
    else:
        print("Did not find the right option")
        driver.quit

    try:
    
    #driver.implicitly_wait(10)
    
        element = WebDriverWait(driver,10000).until(EC.presence_of_element_located((By.XPATH,"//input[@type='password']")))
    
        #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
        
        driver.find_element(by=By.XPATH,value="//input[@type='password']").send_keys("Pitic1982")
        
        driver.find_element(by=By.XPATH, value="//span[contains(text(),'Next')]").click()
    
    except:
        
        print("Element not found!")
        #driver.quit()
        
    try:
    
    #driver.implicitly_wait(10)
    
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//span[@title='AWS Email Verification']")))
    
        #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
        
        driver.find_element(by=By.XPATH,value="//span[@title='AWS Email Verification']").click()
    
        try:
            
            #driver.implicitly_wait(10)
            
            element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Verification code')]/following-sibling::div")))
        
            #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
            
            text = driver.find_element(by=By.XPATH, value="//div[contains(text(),'Verification code')]/following-sibling::div").text
            
            driver.close()
            
            driver.switch_to_window(driver.window_handles[0])
            
            #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
            
        except:
            
            print("Element not found!")
           # driver.quit()
    
    except:
        
        print("Element not found!")
       # driver.quit()
    
except:
    
    print("Element not found!")
   # driver.quit()
    

try:
            
    #driver.implicitly_wait(10)
    
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//awsui-input[@id='otp']")))

    #driver.find_element_by_xpath("//div[@class='lb-none-v-margin lb-btn']//a[@class='lb-btn-p-primary']").click()
    
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='otp']").send_keys(text)
    
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Verify')]").click()
    
    
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
            
except:
    
    print("Element not found!")
    driver.quit()

try:
            
    #check if message is displayed in the interface   
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Your email address has been successfully verified.')]")))
    #insert password
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='password").send_keys("Pitic1982#")
    #insert confirmation password
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='rePassword']").send_keys("Pitic1982#")
    #press Continue button
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Continue (step 1 of 5)')]").click()
    
except:
    
    print("Element not found!")
    driver.quit()
        
try:
            
    #check if message is displayed in the interface   
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//input[@name='accountType' and @value='Personal']")))
    #check Personal account
    driver.find_element(by=By.XPATH, value="//input[@name='accountType' and @value='Personal']").click()
    #insert fullname
    driver.find_element(by=By.XPATH, value="//input[@name='address.fullName']").send_keys("Cris")
    #insert phone
    driver.find_element(by=By.XPATH, value="//input[@name='address.phoneNumber']").send_keys("+40720909286")
    #insert country
    driver.find_element(by=By.XPATH, value="//div[@awsui-select-dropdown-region='filter']").send_keys("romania")
    #select option Romania
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Romania')]").click()
    #insert address
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='address.addressLine1']").send_keys("general magheru, 57")
    #insert city
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='address.city']").send_keys("craiova")
    #insert region, state
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='address.state']").send_keys("dolj")
    #insert postal code
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='address.postalCode']").send_keys("200548")
    #check agreements
    driver.find_element(by=By.XPATH, value="//input[@name='agreement']").click()
    #click Continue button
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Continue (step 2 of 5)')]").click()
    
except:
    
    print("Element not found!")
    driver.quit()
    


try:
            
    #check if cardNumber field is displayed in the interface   
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//awsui-input[@id='cardNumber']")))
    #insert cardNumber
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='cardNumber']").send_keys(data["cardNumber"])
    #click expiration month
    driver.find_element(by=By.XPATH, value="//awsui-select[@id='expirationMonth']").click()
    #insert expiration month
    driver.find_element(by=By.XPATH, value="//div[@title='" + data["expiryMonth"] + "']").click()
    #click expiration year
    driver.find_element(by=By.XPATH, value="//awsui-select[@id='expirationYear']").click()
    #insert expiration year
    driver.find_element(by=By.XPATH, value="//div[@title='" + data["expiryYear"] + "']").click()
    #insert cardholder's name
    driver.find_element(by=By.XPATH, value="//input[@name='accountHolderName']").send_keys(data["name"])
    #check box Use my contact address
    driver.find_element(by=By.XPATH, value="//input[@name='addressType' and @value='Existing']").click()
    #press Continue button
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Verify and Continue (step 3 of 5)]").click()
    
except:
    
    print("Element not found!")
    driver.quit()
    
try:
            
    #check if checkbox is displayed in the interface   
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//input[@name='divaMethod' and @value='Sms']")))
    #check the checkbox with Text message
    driver.find_element(by=By.XPATH, value="//input[@name='divaMethod' and @value='Sms']").click()
    #click drop down list country
    driver.find_element(by=By.XPATH, value="//awsui-select[@id='country']").click()
    #insert country Romania
    driver.find_element(by=By.XPATH, value="//awsui-input[@class='awsui-select-dropdown-filter']").send_keys("romania")
    #select option Romania
    driver.find_element(by=By.XPATH, value="//div[@title='Romania (+40)']").click()
    #insert phone number
    driver.find_element(by=By.XPATH, value="//awsui-input[@id='phoneNumber']").send_keys("720909286")
    #press Send sms button
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'Send SMS (step 4 of 5)]").click()
except:
    
    print("Element not found!")
    driver.quit()
    
    
    
f.close()


if __name__ == '__main__':
    pass