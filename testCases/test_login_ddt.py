import time

import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import  readConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_002_DDT_Login:
    baseURL = readConfig.getApplicationURL()
    path ="./TestData/LoginData.xlsx"

    logger = LogGen.loggen()
# Test the multiple combination of Valid/Invalid Logins
    @pytest.mark.regression
    def test_login_ddt(self , setup):
        self.logger.info("******** verify login DDT test********")
        self.logger.info("**********Verify Login test**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path ,"Sheet1")
        print("No of rows are " , self.rows)

        lst_status =[] # empty list variable for storing expected result
        for  r in range(2 , self.rows+1):
            self.user = ExcelUtils.readData(self.path ,"Sheet1" , r , 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.expected = ExcelUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title ==  expected_title:
                if self.expected == "Pass":
                    self.logger.info("***********Test is passed********")
                    self.lp.clickLogOut()
                    lst_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("*********Test is Failed**********")
                    self.lp.clickLogOut()
                    lst_status.append("Fail")
            elif actual_title !=  expected_title:
                if self.expected == "Pass":
                    self.logger.info("********Test is failed********")
                    lst_status.append("fail")
                elif self.expected == "Fail":
                    self.logger.info("********Test is passed********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********Login DDT test is passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Login DDT test is failed********")
            self.driver.close()
            assert False

            self.logger.info("******End of Login DDT test is********")




