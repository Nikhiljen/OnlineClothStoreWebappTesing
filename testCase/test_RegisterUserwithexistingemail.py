from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class TestFive(baseClass):
    nameLocator = (By.CSS_SELECTOR, "input[placeholder='Name']")
    emailLocator = (By.XPATH, "//input[@data-qa='signup-email']")
    signUpButton = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    verifyText2 = (By.XPATH, "//div[@class='signup-form']/form/p")


    def test_verifyUseralredyExit(self):

        log = self.getLogger()

        self.is_homePage_visible()
        verifyText = self.verifySignUpText()
        assert 'New User Signup!' in verifyText
        log.info("New User Signup!")
        self.driver.find_element(*TestFive.nameLocator).send_keys("Nikhil")
        self.driver.find_element(*TestFive.emailLocator).send_keys("npjengte@gmail.com")
        self.driver.find_element(*TestFive.signUpButton).click()
        verifyText = self.driver.find_element(*TestFive.verifyText2).text
        assert "Email Address already exist!" in verifyText