from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class testCasePage(baseClass):

    messagedisply = (By.XPATH, "//div[@class='panel-group']/h5/span")


    def __init__(self, driver):
        self.driver = driver

    def testCasepage(self):
        return self.driver.current_url