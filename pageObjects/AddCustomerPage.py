from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    linkCustomer = (By.XPATH , '//a[@href="#"]//p[contains(text() , "Customers")]')
    lnkCustomerSubmenu = (By.XPATH , '//a[@href="/Admin/Customer/List"]//p')
    btnAddNew = (By.CSS_SELECTOR , 'a[href="/Admin/Customer/Create"]')
    txtEmail = (By.ID, 'Email')
    txtPassword = (By.ID , 'Password')
    txtFirstName =(By.ID , 'FirstName')
    txtLastName = (By.ID, 'FirstName')
    rdFGender = (By.ID , 'Gender_Female')
    rdMGender = (By.ID, 'Gender_Male')
    txtDate = (By.ID , 'DateOfBirth')
    txtCompany = (By.NAME, 'Company')
    inputTaxExempt = (By.ID , 'IsTaxExempt')
    lstCustomerRole = (By.XPATH , '//ul[@id="SelectedCustomerRoleIds_taglist"]//parent::div')
    lstDropDonwOptions = (By.CSS_SELECTOR , 'ul[id="SelectedCustomerRoleIds_listbox"]>li[role="option"]')
    lstOptionAdministrators = (By.XPATH, '//ul/li[text()="Administrators"]')
    lstOptionGuests = (By.XPATH, '//ul/li[text()="Guests"]')
    lstOptionRegistered = (By.XPATH, '//ul/li[text()="Registered"]')
    lstOptionVendors = (By.XPATH, '//ul/li[text()="Vendors"]')
    lstOptionForumModerator = (By.XPATH , '//ul/li[text()="Forum Moderators"]' )
    lstOptionDelete = (By.CSS_SELECTOR , 'ul#SelectedCustomerRoleIds_taglist>li>span[title="delete"]')

    ddVendor = (By.ID , 'VendorId')
    txtCompany = (By.ID , 'Company')
    ddVendorOption = (By.XPATH , '//select[@id="VendorId"]/option[text() = "Vendor 1"]')
    txtAdminComment = (By.XPATH , '//textarea[@name="AdminComment"]')
    btnSave = (By.CSS_SELECTOR , 'button[name="save"]')
    successMessage = (By.TAG_NAME, 'body')

    # this will instantiate an local driver
    def __init__(self , driver):
        self.driver = driver

    def clickOnCustomerLink(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.linkCustomer)).click()

    def clickOnCustomerSubMenu(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.lnkCustomerSubmenu)).click()

    def clickonAddNewCustomer(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btnAddNew)).click()

    def setEmail(self , email):
        self.driver.find_element(*self.txtEmail).send_keys(email)

    def setPassword(self , password):
        self.driver.find_element(*self.txtPassword).send_keys(password)

    def setFirstName(self ,firstName):
        self.driver.find_element(*self.txtPassword).send_keys(firstName)

    def setLastName(self , LastName):
        self.driver.find_element(*self.txtLastName).send_keys(LastName)

    def setCustomerRoles(self , role):
        self.driver.find_element(*self.lstCustomerRole).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.lstDropDonwOptions))

        if role =="Administrators":
            self.lstOption = self.driver.find_element(*self.lstOptionAdministrators)

        elif role == "Guests":
            self.driver.find_element(self.lstOptionDelete).click()
            self.lstOption = self.driver.find_element(*self.lstOptionGuests)

        elif role == "Forum Moderator":
            self.lstOption = self.driver.find_element(*self.lstOptionForumModerator)

        elif role =="Registered":
            self.lstOption= self.driver.find_element(*self.lstOptionRegistered)

        elif role == "vendors":
            self.lstOption = self.driver.find_element(*self.lstOptionVendors)

        else:
            self.lstOption = self.driver.find_element(*self.lstOptionGuests)

        self.driver.execute_script('arguments[0].click();' , self.lstOption)

    def setManagerOfVendor(self , value):
        dropDownValue = Select(self.driver.find_element(*self.ddVendor))
        dropDownValue.select_by_visible_text(value)

    def setGender(self , gender):
        if gender == "Female":
            self.driver.find_element(*self.rdFGender).click()
        elif gender == "Male":
            self.driver.find_element(*self.rdMGender).click()
        else:
            self.driver.find_element(*self.rdFGender).click()

    def setDOB(self , date):
        self.driver.find_element(*self.txtDate).send_keys(date)

    def setCompanyName(self , name):
        self.driver.find_element(*self.txtCompany).send_keys(name)

    def setAdminComment(self , comment):
        self.driver.find_element(*self.txtAdminComment).send_keys(comment)

    def saveOn(self):
        self.driver.find_element(*self.btnSave).click()










