from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class order_confirm(baseClass):
    order_confirm_locator = (By.XPATH, "//p[normalize-space()='Congratulations! Your order has been confirmed!']")

    def __init__(self, driver):
        self.driver = driver
    def OrderConfirmVerification(self):
        return self.driver.find_element(*order_confirm.order_confirm_locator).text