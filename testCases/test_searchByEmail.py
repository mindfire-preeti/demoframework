import pytest

from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import  readConfig
from utilities.customLogger import LogGen

@pytest.mark.regression
class Test_004_SearchCutsomer:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUserEmail()
    password = readConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_searchByEmail(self ,setup):
        self.logger.info("**********Test_0013_AddCustomer**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login is successfull***********")
        self.logger.info("*********Starting Search customer***********")

        self.addCust = AddCustomer(self.driver)  # create object of add customer class
        self.searchCust = SearchCustomer(self.driver)

        self.addCust.clickOnCustomerLink()
        self.addCust.clickOnCustomerSubMenu()
        self.searchCust.setSearchTerm("admin@yourStore.com")
        self.searchCust.clickSearch()
        searchStatus = self.searchCust.validateEmailResult("admin@yourStore.com")
        assert True == searchStatus
        self.logger.info("*********TC_Search result finished***********")
        self.driver.close()
        