from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Utilities.baseClass import baseClass
from testPages.orderConfirmPage import order_confirm


class payment(baseClass):
    pay_confirm_orderButton = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def get_formPage(self):
        self.driver.get("//form[@id='payment-form']")

    def CardDetails(self):
        try:
            # Wait for the payment input fields to be present
            name_on_card_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='name_on_card']")))
            card_number_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='card_number']")
            cvc_input = self.driver.find_element(By.XPATH, "//input[@placeholder='ex. 311']")
            expiration_date_month = self.driver.find_element(By.XPATH, "//input[@placeholder='MM']")
            expiration_date_year = self.driver.find_element(By.XPATH, "//input[@placeholder='YYYY']")

            # Enter payment details
            name_on_card_input.send_keys("Nikhil")
            card_number_input.send_keys("1234 5678 9012 3456")
            cvc_input.send_keys("123")
            expiration_date_month.send_keys("12")
            expiration_date_year.send_keys("25")

        except Exception as e:
            print(f"Error: {e}")

    def payOrder(self):
        self.driver.find_element(*payment.pay_confirm_orderButton).click()
        confirmOrder = order_confirm(self.driver)
        return confirmOrder
