import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import  readConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUserEmail()
    password = readConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self , setup):
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("**********Verify Home Page title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            self.logger.info("*********Home Page title test is passed**********")
            self.driver.close()
            assert True

        else:
            self.logger.error("*********Home Page title test is failed**********")
            self.driver.save_screenshot("/.Screenshots/" + "test1.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self , setup):
        self.logger.info("**********Verify Login test**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********Login test is passed**********")
            self.driver.close()
            assert True

        else:
            self.logger.error("*********Login test is failed**********")
            self.driver.save_screenshot("/.Screenshots/" + "login.png")
            self.driver.close()
            assert False

