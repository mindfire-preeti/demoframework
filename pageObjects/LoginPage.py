from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username = (By.ID , 'Email')
    textbox_password = (By.ID , 'Password')
    button_login = (By.CSS_SELECTOR ,'button[class*="login-button"]')
    button_logout = (By.CSS_SELECTOR , 'a[href="/logout"]')

    # this constructor will initialize driver and will be called at the time of object creation
    def __init__(self , driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(*self.textbox_username).clear()
        self.driver.find_element(*self.textbox_username).send_keys(username)

    def setPassword(self , password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.button_login).click()

    def clickLogOut(self):
        self.driver.find_element(*self.button_logout).click()

