import string
import random

import pytest
from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import  readConfig
from utilities.customLogger import LogGen

class  Test_003_AddCustomer:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUserEmail()
    password = readConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addNewCustomer(self , setup):
        self.logger.info("**********Test_0013_AddCustomer**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login is successfull")
        self.logger.info("*********Starting add customer***********")

        self.addCust = AddCustomer(self.driver) # create object of add customer class

        self.addCust.clickOnCustomerLink()
        self.addCust.clickOnCustomerSubMenu()
        self.addCust.clickonAddNewCustomer()

        self.email = random_generator() +"@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Preeti")
        self.addCust.setLastName("Sharma")
        self.addCust.setGender("Female")
        self.addCust.setDOB("01/09/1987")
        self.addCust.setCompanyName("Qa company")

        self.addCust.setCustomerRoles("Administrators")
        self.addCust.setManagerOfVendor("Vendor 1")
        self.addCust.setAdminComment("This is testing........")
        self.addCust.saveOn()

        self.logger.info("*********Saving customer info***********")

        self.msg = self.driver.find_element(By.TAG_NAME ,'body').text
        print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*********Add Customer Test passes***********")
        else:
            self.driver.save_screenshot('./Screenshots/' + 'test_customer_scr.png')
            self.logger.info("*********Add Customer Test failed***********")
            assert True == False

        self.driver.close()
        self.logger.info("*********Ending Add Customer Test***********")

def random_generator(size=8 , chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))









