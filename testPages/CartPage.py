from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.baseClass import baseClass
from testPages.loginePage import loginPage
from testPages.PaymentPage import payment


class CartPage(baseClass):
    CartPage_Subscription_Text = (By.CSS_SELECTOR, "div[class='single-widget'] h2")
    CartPage_subscribe_email = (By.ID, "susbscribe_email")
    CartPage_subscribe_Button = (By.CSS_SELECTOR, "#subscribe")
    CartProduct_quantity = (By.XPATH, "//td[@class='cart_quantity']/button")
    CheckOutButtonLocator = (By.CSS_SELECTOR, ".btn.btn-default.check_out")
    orderDescription = (By.XPATH, "//textarea[@name='message']")
    placeOrderButton = (By.XPATH, "//a[normalize-space()='Place Order']")
    remove_Product_button = (By.XPATH, "//td[@class='cart_delete']/a")

    def __init__(self, driver):
        self.driver = driver

    def verifySubscriptionText_Element_onCartPage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(*CartPage.CartPage_Subscription_Text).text

    def subscription_Successful_onCartPage(self):
        self.driver.find_element(*CartPage.CartPage_subscribe_email).send_keys("nik@gmail.com")
        self.driver.find_element(*CartPage.CartPage_subscribe_Button).click()
        success_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]")))
        return success_message_element

    def cartPageVerification(self):
        return self.driver.current_url

    def CheckoutPageButton(self):
        self.driver.find_element(*CartPage.CheckOutButtonLocator).click()

    def register_link(self):
        try:
            register_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='modal-content']/div[2]/p[2]/a")))
            register_link.click()
            login_page = loginPage(self.driver)
            return login_page

        except Exception as e:
            print(f"Error: {e}")

    def continueOnCart(self):
        try:
            Cart_page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='modal-content']/div[3]/button")))
            Cart_page.click()

        except Exception as e:
            print(f"Error: {e}")

    def order_Description(self):
        self.driver.find_element(*CartPage.orderDescription).send_keys("Place Order a T-Shirt")
        self.driver.find_element(*CartPage.placeOrderButton).click()
        paymentPage = payment(self.driver)
        return paymentPage

    def removeProduct(self):
        self.driver.find_element(*CartPage.remove_Product_button).click()

        try:
            product_page = (By.CSS_SELECTOR, "span[id='empty_cart'] a")

            # Wait for the element to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(product_page)
            )

            # Interact with the element
            element.click()
            product_page_url = self.driver.current_url
            return product_page_url

        except Exception as e:
            print(f"Error: {e}")
