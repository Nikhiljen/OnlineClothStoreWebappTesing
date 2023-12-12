import inspect
import logging

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from testData.testSignUpData import signUpPageData


@pytest.mark.usefixtures("Setup")
class baseClass:
    timeout = 10
    deleteAccountButton = (By.CSS_SELECTOR, "a[href='/delete_account']")
    accountDeleteMessage = (By.CSS_SELECTOR, "h2[class='title text-center'] b")
    continueButtonAfterDeleteAccount = (By.CSS_SELECTOR, ".btn.btn-primary")
    loginUserLocator = (By.XPATH, "//li[10]//a[1]")
    logoutLocator = (By.CSS_SELECTOR, "a[href='/logout']")

    @staticmethod
    def getLogger():
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

    def verifyLoginAsUser(self):
        loginUserText = self.driver.find_element(*baseClass.loginUserLocator).text
        return loginUserText

    def verifyDeleteAccountSuccessful(self):
        self.driver.find_element(*baseClass.deleteAccountButton).click()
        deleteAccountMessageText = self.driver.find_element(*baseClass.accountDeleteMessage).text
        self.driver.find_element(*baseClass.continueButtonAfterDeleteAccount).click()
        return deleteAccountMessageText

    def logoutAccountSuccessful(self):
        self.driver.find_element(*baseClass.logoutLocator).click()
        login_page_url = 'https://automationexercise.com/login'
        return login_page_url
