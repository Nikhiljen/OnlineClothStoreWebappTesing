
from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass
from testPages.AccountCreation import signUpPage


class loginPage(baseClass):
    nameLocator = (By.CSS_SELECTOR, "input[placeholder='Name']")
    emailLocator = (By.XPATH, "//input[@data-qa='signup-email']")
    signUpButton = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    userNameLocator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    passwordLocator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    loginButton = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    unsuccessfulMessage = (By.XPATH, "//div[@class='login-form']/form/p")
    verifyText2 = (By.XPATH, "//div[@class='signup-form']/form/p")

    def __init__(self, driver):
        self.driver = driver

    def verifySignUpText(self):
        verifyText = self.driver.find_element(By.CSS_SELECTOR, "div[class='signup-form'] h2").text
        return verifyText

    def verifyLoginText(self):
        loginText = self.driver.find_element(By.CSS_SELECTOR, "div[class='login-form'] h2").text
        return loginText

    def newUserSignUp(self, getData):
        self.driver.find_element(*loginPage.nameLocator).send_keys(getData["Name"])
        self.driver.find_element(*loginPage.emailLocator).send_keys(getData["email"])
        self.driver.find_element(*loginPage.signUpButton).click()
        account_creation_Page = signUpPage(self.driver)
        return account_creation_Page

    def loginWithCorrectCredential(self, getData):
        self.driver.find_element(*loginPage.userNameLocator).send_keys(getData["email"])
        self.driver.find_element(*loginPage.passwordLocator).send_keys(getData["password"])
        self.driver.find_element(*loginPage.loginButton).click()

    def loginWithIncorrectCredential(self, getData):
        self.driver.find_element(*loginPage.userNameLocator).send_keys(getData["email"])
        self.driver.find_element(*loginPage.passwordLocator).send_keys(getData["password"])
        self.driver.find_element(*loginPage.loginButton).click()
        return self.driver.find_element(*loginPage.unsuccessfulMessage).text

    def UserExitEmail(self, getData):
        self.driver.find_element(*loginPage.nameLocator).send_keys(getData["Name"])
        self.driver.find_element(*loginPage.emailLocator).send_keys(getData["email"])
        self.driver.find_element(*loginPage.signUpButton).click()
        verifyText = self.driver.find_element(*loginPage.verifyText2).text
        return verifyText
