from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class testCasePage(baseClass):
    testCaseButton = (By.CSS_SELECTOR, "a[href='/test_cases']")
    messagedisply = (By.XPATH, "//div[@class='panel-group']/h5/span")


    def __init__(self, driver):
        self.driver = driver

    def testCaselinkpage(self):
        self.driver.find_element(*testCasePage.testCaseButton).click()
        return self.driver.find_element(*testCasePage.messagedisply).text