import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchCustomer:
    txtEmail = (By.ID , 'SearchEmail')
    txtFirstName = (By.ID , 'SearchFirstName')
    txtLastName = (By.ID , 'SearchLastName')
    btnSearch = (By.ID , 'search-customers')
    emailRowData = (By.CSS_SELECTOR , 'tbody>tr>td:nth-of-type(2)')

    def __init__(self , driver):
        self.driver = driver

    def setSearchTerm(self , email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.txtEmail)).send_keys(email)

    def clickSearch(self):
        self.driver.find_element(*self.btnSearch).click()

    def validateEmailResult(self ,email):
        flag = False
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.emailRowData))
        emailText = self.driver.find_element(*self.emailRowData).text
        print(emailText)
        if emailText == email:
            flag = True
        return flag