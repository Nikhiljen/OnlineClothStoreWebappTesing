from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class signUpPage:
    verifyText2 = (By.XPATH, "//div[@class='login-form']/h2[1]")
    tileLocator = (By.ID, "id_gender1")
    Name = (By.ID, "name")
    Email = (By.ID, "email")
    Password = (By.ID, "password")
    Day = (By.ID, "days")
    Month = (By.ID, "months")
    Year = (By.ID, "years")
    NewsLetter = (By.ID, "newsletter")
    Option = (By.CSS_SELECTOR, "#optin")
    firstName = (By.CSS_SELECTOR, "#first_name")
    lastName = (By.ID, "last_name")
    companyName = (By.CSS_SELECTOR, "#company")
    address1 = (By.XPATH, "//input[@id='address1']")
    address2 = (By.CSS_SELECTOR, "#address2")
    countryName = (By.CSS_SELECTOR, "#country")
    stateName = (By.CSS_SELECTOR, "#state")
    cityName = (By.CSS_SELECTOR, "#city")
    zipcodeNo = (By.CSS_SELECTOR, "#zipcode")
    mobileNo = (By.CSS_SELECTOR, "#mobile_number")
    submitButton = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    submitMessage = (By.CSS_SELECTOR, ".title.text-center")
    continueButton = (By.CSS_SELECTOR, ".btn.btn-primary")

    def __init__(self, driver):
        self.driver = driver

    def accountInformationText(self):
        verifyText = self.driver.find_element(*signUpPage.verifyText2).text
        return verifyText

    def accountInformationPage(self, getData):
        self.driver.find_element(*signUpPage.tileLocator).click()
        assert self.driver.find_element(*signUpPage.Name).get_attribute('value') == getData["Name"]
        assert self.driver.find_element(*signUpPage.Email).get_attribute('value') == getData["email"]
        self.driver.find_element(*signUpPage.Password).send_keys(getData["password"])
        Select(self.driver.find_element(*signUpPage.Day)).select_by_value(getData["Day"])
        Select(self.driver.find_element(*signUpPage.Month)).select_by_visible_text(getData["Month"])
        Select(self.driver.find_element(*signUpPage.Year)).select_by_value(getData["year"])

    def addressInformationPage(self, getData):
        self.driver.find_element(*signUpPage.firstName).send_keys(getData["FirstName"])
        self.driver.find_element(*signUpPage.lastName).send_keys(getData["LastName"])
        self.driver.find_element(*signUpPage.companyName).send_keys(getData["Company"])
        self.driver.find_element(*signUpPage.address1).send_keys(getData["Address"])
        self.driver.find_element(*signUpPage.address2).send_keys(getData["Address2"])
        Select(self.driver.find_element(*signUpPage.countryName)).select_by_visible_text(getData["country"])
        self.driver.find_element(*signUpPage.stateName).send_keys(getData["State"])
        self.driver.find_element(*signUpPage.cityName).send_keys(getData["City"])
        self.driver.find_element(*signUpPage.zipcodeNo).send_keys(getData["Zipcode"])
        self.driver.find_element(*signUpPage.mobileNo).send_keys(getData["MobileNumber"])
        self.driver.find_element(*signUpPage.submitButton).click()
        
    def VerifyAccountCreationPage(self):
        account_Creation_text = self.driver.find_element(*signUpPage.submitMessage).text
        self.driver.find_element(*signUpPage.continueButton).click()
        return account_Creation_text
