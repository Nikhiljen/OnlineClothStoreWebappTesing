import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.baseClass import baseClass
from testData.testSignUpData import signUpPageData
from testPages.CartPage import CartPage
from testPages.loginePage import loginPage
from testPages.contactUsFrom import contactUs
from testPages.testCasePage import testCasePage
from testPages.productPage import productPage


class HomePage(baseClass):
    subscriptionLocator = (By.ID, "susbscribe_email")
    subscribeButton = (By.ID, "subscribe")
    subscribeText = (By.CSS_SELECTOR, "div[class='single-widget'] h2")
    contactUsButton = (By.CSS_SELECTOR, "a[href='/contact_us']")
    testCaseButton = (By.CSS_SELECTOR, "a[href='/test_cases']")
    productPageButton = (By.CSS_SELECTOR, "a[href='/products']")
    CartPageButton = (By.CSS_SELECTOR, "a[href='/view_cart']")
    viewProductLocator = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    order_confirm_locator = (By.XPATH, "//p[normalize-space()='Congratulations! Your order has been confirmed!']")

    def __init__(self, driver):
        self.driver = driver

    def signupButton(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
        loginepage = loginPage(self.driver)
        return loginepage

    def contactUsButton(self):
        self.driver.find_element(*HomePage.contactUsButton).click()
        contactusPage = contactUs(self.driver)
        return contactusPage

    def testCaseButton(self):
        self.driver.find_element(*HomePage.testCaseButton).click()
        TestCase = testCasePage(self.driver)
        return TestCase

    def productButton(self):
        self.driver.find_element(*HomePage.productPageButton).click()
        productpage = productPage(self.driver)
        return productpage

    def CartButton(self):
        self.driver.find_element(*HomePage.CartPageButton).click()
        cartpage = CartPage(self.driver)
        return cartpage

    def verifySubscriptionTextHompage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(*HomePage.subscribeText).text

    def subscriptionSuccefullonHomepage(self):
        self.driver.find_element(*HomePage.subscriptionLocator).send_keys("nik@gmail.com")
        self.driver.find_element(*HomePage.subscribeButton).click()
        success_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]")))
        return success_message_element

    def viewSampleProduct(self):
        self.driver.find_element(*HomePage.viewProductLocator).click()
        productpage = productPage(self.driver)
        return productpage

    def OrderConfirmVerification(self):
        return self.driver.find_element(*HomePage.order_confirm_locator).text

    @pytest.fixture(params=signUpPageData.homepageTestData)
    def getData(self, request):
        return request.param
