import time

from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class contactUs(baseClass):
    messageLocator = (By.XPATH, "//div[@class='contact-form']/h2")
    name_path = (By.CSS_SELECTOR, "input[placeholder='Name']")
    email_path = (By.XPATH, "//input[@placeholder='Email']")
    subject_path = (By.CSS_SELECTOR, "input[placeholder='Subject']")
    message_path = (By.ID, "message")
    filepath = (By.XPATH, "//input[@name='upload_file']")

    success_message_path = (By.XPATH, "//div[@class='contact-form']/div[2]")
    home_return_path = (By.XPATH, "//div[@id='form-section']/a/span/i")

    def __init__(self, driver):
        self.driver = driver

    def get_intouchText(self):
        return self.driver.find_element(*contactUs.messageLocator).text

    def fill_up_data(self):
        self.driver.find_element(*contactUs.name_path).send_keys("Nikhil")
        self.driver.find_element(*contactUs.email_path).send_keys("Nikhil@gmail.com")
        self.driver.find_element(*contactUs.subject_path).send_keys("Error while loging")
        self.driver.find_element(*contactUs.message_path).send_keys("Error while loging in our website")

        # Wait for the alert to appear (if necessary)
        time.sleep(2)

    def alert_check(self):
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Accept the alert (click OK)
        alert.accept()

    def verify_Contactus_message(self):
        return self.driver.find_element(*contactUs.success_message_path).text

    def homePage_return(self):
        self.driver.find_element(*contactUs.home_return_path).click()
        return self.driver.current_url
