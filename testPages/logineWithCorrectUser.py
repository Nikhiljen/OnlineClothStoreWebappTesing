from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class loginePage(baseClass):
    userNameLocator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    passwordLocator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    logineButton = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    unsccessfullMessage = (By.XPATH, "//div[@class='login-form']/form/p")

    def __init__(self, driver):
        self.driver = driver

    def logineWithCorrectCredintial(self):
        self.driver.find_element(*loginePage.userNameLocator).send_keys("nikhiljengte@gmail.com")
        self.driver.find_element(*loginePage.passwordLocator).send_keys("nikhil123")
        self.driver.find_element(*loginePage.logineButton).click()

    def logineWithIncorrectCredintial(self):
        self.driver.find_element(*loginePage.userNameLocator).send_keys("nikhiljengte@gmail.com")
        self.driver.find_element(*loginePage.passwordLocator).send_keys("nikhil123")
        self.driver.find_element(*loginePage.logineButton).click()
        return self.driver.find_element(*loginePage.unsccessfullMessage).text
