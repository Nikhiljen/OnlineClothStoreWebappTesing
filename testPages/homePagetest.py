import pytest
from selenium.common import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.baseClass import baseClass
from testData.testSignUpData import signUpPageData


class HomePage(baseClass):
    tileLocator = (By.ID, "id_gender1")
    Name = (By.ID, "name")
    Email = (By.ID, "email")
    Password = (By.ID, "password")
    Day = (By.ID, "days")
    Month = (By.ID, "months")
    Year = (By.ID, "years")
    NewsLetter = (By.ID, "newsletter")
    Optin = (By.CSS_SELECTOR, "#optin")
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
    subitMessage = (By.CSS_SELECTOR, ".title.text-center")
    continueButton = (By.CSS_SELECTOR, ".btn.btn-primary")
    subscriptionLocator = (By.ID, "susbscribe_email")
    subscribeButton = (By.ID, "subscribe")
    subscribeText = (By.CSS_SELECTOR, "div[class='single-widget'] h2")

    def __init__(self, driver):
        self.driver = driver

    def accountInformationPage(self):
        self.driver.find_element(*HomePage.tileLocator).click()
        assert self.driver.find_element(*HomePage.Name).get_attribute('value') == "Nikhil"
        assert self.driver.find_element(*HomePage.Email).get_attribute('value') == "npjengte8@gmail.com"
        self.driver.find_element(*HomePage.Password).send_keys("Nikhil@123")
        Select(self.driver.find_element(*HomePage.Day)).select_by_value("4")
        Select(self.driver.find_element(*HomePage.Month)).select_by_visible_text("June")
        Select(self.driver.find_element(*HomePage.Year)).select_by_value("1992")

    def addressInformationPage(self):
        self.driver.find_element(*HomePage.firstName).send_keys("Nikhil")
        self.driver.find_element(*HomePage.lastName).send_keys("Jengte")
        self.driver.find_element(*HomePage.companyName).send_keys("PDM")
        self.driver.find_element(*HomePage.address1).send_keys("Tahsil Office Mul")
        self.driver.find_element(*HomePage.address2).send_keys("Chandrapur")
        Select(self.driver.find_element(*HomePage.countryName)).select_by_visible_text("India")
        self.driver.find_element(*HomePage.stateName).send_keys("Maharashtra")
        self.driver.find_element(*HomePage.cityName).send_keys("Mul")
        self.driver.find_element(*HomePage.zipcodeNo).send_keys("441224")
        self.driver.find_element(*HomePage.mobileNo).send_keys("1234567890")
        self.driver.find_element(*HomePage.submitButton).click()

    def VerifyAccountCreationPage(self):
        accountCreationtext = self.driver.find_element(*HomePage.subitMessage).text
        self.driver.find_element(*HomePage.continueButton).click()
        return accountCreationtext


    def verifySubscriptionTextElement(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(*HomePage.subscribeText).text

    def subscriptionSuccefull(self):
        self.driver.find_element(*HomePage.subscriptionLocator).send_keys("nik@gmail.com")
        self.driver.find_element(*HomePage.subscribeButton).click()
        success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]")))
        return success_message_element


    @pytest.fixture(params=signUpPageData.homepageTestData)
    def getData(self, request):
        return request.param


