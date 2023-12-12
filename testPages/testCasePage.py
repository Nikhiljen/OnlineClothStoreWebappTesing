from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class testCasePage(baseClass):
    MessagePack = (By.XPATH, "//div[@class='panel-group']/h5/span")

    def __init__(self, driver):
        self.driver = driver

    def test_case_page(self):
        return self.driver.current_url
