import time

from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class contactUs(baseClass):
    messageLocator = (By.XPATH, "//div[@class='contact-form']/h2")
    namepath = (By.CSS_SELECTOR, "input[placeholder='Name']")
    emailpath = (By.XPATH, "//input[@placeholder='Email']")
    subjectpath = (By.CSS_SELECTOR, "input[placeholder='Subject']")
    messagepath = (By.ID, "message")
    filepath = (By.XPATH, "//input[@name='upload_file']")
    submitpath = (By.CSS_SELECTOR, "input[value='Submit']")
    successmessagepath = (By.XPATH, "//div[@class='contact-form']/div[2]")
    homereturnpath = (By.XPATH, "//div[@id='form-section']/a/span/i")

    def __init__(self, driver):
        self.driver = driver

    def getintouchText(self):
        return self.driver.find_element(*contactUs.messageLocator).text

    def fillupdata(self):
        self.driver.find_element(*contactUs.namepath).send_keys("Nikhil")
        self.driver.find_element(*contactUs.emailpath).send_keys("Nikhil@gmail.com")
        self.driver.find_element(*contactUs.subjectpath).send_keys("Error while loging")
        self.driver.find_element(*contactUs.messagepath).send_keys("Error while loging in our website")
        self.driver.find_element(*contactUs.submitpath).click()
        # Wait for the alert to appear (if necessary)
        time.sleep(2)

    def alertcheck(self):
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Accept the alert (click OK)
        alert.accept()

    def verifyContactusmessage(self):
        return self.driver.find_element(*contactUs.successmessagepath).text

    def homepagereturn(self):
        self.driver.find_element(*contactUs.homereturnpath).click()
        return self.driver.current_url
