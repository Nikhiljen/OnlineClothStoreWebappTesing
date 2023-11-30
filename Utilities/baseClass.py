import inspect
import logging

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("Setup")
class baseClass:
    timeout = 10
    deleteAccountButton = (By.CSS_SELECTOR, "a[href='/delete_account']")
    accountDeleteMessage = (By.CSS_SELECTOR, "h2[class='title text-center'] b")
    continueButtonAfterDeleteAccount = (By.CSS_SELECTOR, ".btn.btn-primary")
    logineUserLocator = (By.XPATH, "//li[10]//a[1]")
    logoutLocator = (By.XPATH, "a[href='/logout']")
    nameLocator = (By.CSS_SELECTOR, "input[placeholder='Name']")
    emailLocator = (By.XPATH, "//input[@data-qa='signup-email']")
    signUpButton = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    verifyText2 = (By.XPATH, "//div[@class='login-form']/h2[1]")

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(r"D:\AutomatedStore\logReports\reports.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def is_homePage_visible(self):
        log = self.getLogger()
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            element_present = EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Website for automation practice']"))
            wait.until(element_present)
            log.info("Page loaded successfully!")   
            return self.driver.title
        except TimeoutException:
            log.info("Timed out waiting for page to load.")

    def signUpData(self):
        self.driver.find_element(*baseClass.nameLocator).send_keys("Nikhil")
        self.driver.find_element(*baseClass.emailLocator).send_keys("npjengte8@gmail.com")
        self.driver.find_element(*baseClass.signUpButton).click()
        verifyText = self.driver.find_element(*baseClass.verifyText2).text
        return verifyText

    def verifySignUpText(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
        verifyText = self.driver.find_element(By.CSS_SELECTOR, "div[class='signup-form'] h2").text
        return verifyText

    def verifyLogineText(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
        logineText = self.driver.find_element(By.CSS_SELECTOR, "div[class='login-form'] h2").text
        return logineText

    def verifyLogineAsUser(self):
        logineUserText = self.driver.find_element(*baseClass.logineUserLocator).text
        # print(logineUserText)
        return logineUserText

    def verifyDeleteAccountSuccessful(self):
        self.driver.find_element(*baseClass.deleteAccountButton).click()
        deleteAccountMessgaeText = self.driver.find_element(*baseClass.accountDeleteMessage).text
        self.driver.find_element(*baseClass.continueButtonAfterDeleteAccount).click()
        return deleteAccountMessgaeText

    def logoutAccountSuccessful(self):
        self.driver.find_element(*baseClass.logoutLocator).click()
