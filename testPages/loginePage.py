from selenium.webdriver.common.by import By

from testPages.AccountCreation import signUpPage


class loginPage:
    nameLocator = (By.CSS_SELECTOR, "input[placeholder='Name']")
    emailLocator = (By.XPATH, "//input[@data-qa='signup-email']")
    signUpButton = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    userNameLocator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    passwordLocator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    logineButton = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    unsccessfullMessage = (By.XPATH, "//div[@class='login-form']/form/p")
    verifyText2 = (By.XPATH, "//div[@class='signup-form']/form/p")

    def __init__(self, driver):
        self.driver = driver

    def verifySignUpText(self):
        verifyText = self.driver.find_element(By.CSS_SELECTOR, "div[class='signup-form'] h2").text
        return verifyText

    def verifyLogineText(self):
        logineText = self.driver.find_element(By.CSS_SELECTOR, "div[class='login-form'] h2").text
        return logineText

    def newUserSignUp(self):
        self.driver.find_element(*loginPage.nameLocator).send_keys("Nikhil")
        self.driver.find_element(*loginPage.emailLocator).send_keys("npjengte10@gmail.com")
        self.driver.find_element(*loginPage.signUpButton).click()
        accountcreationPage = signUpPage(self.driver)
        return accountcreationPage
    
    def logineWithCorrectCredintial(self):
        self.driver.find_element(*loginPage.userNameLocator).send_keys("npjengte9@gmail.com")
        self.driver.find_element(*loginPage.passwordLocator).send_keys("Nikhil@123")
        self.driver.find_element(*loginPage.logineButton).click()

    def logineWithIncorrectCredintial(self):
        self.driver.find_element(*loginPage.userNameLocator).send_keys("nikhiljengte@gmail.com")
        self.driver.find_element(*loginPage.passwordLocator).send_keys("nikhil123")
        self.driver.find_element(*loginPage.logineButton).click()
        return self.driver.find_element(*loginPage.unsccessfullMessage).text
    
    
    def UserExitEmail(self):
        self.driver.find_element(*loginPage.nameLocator).send_keys("Nikhil")
        self.driver.find_element(*loginPage.emailLocator).send_keys("npjengte@gmail.com")
        self.driver.find_element(*loginPage.signUpButton).click()
        verifyText = self.driver.find_element(*loginPage.verifyText2).text
        return verifyText

