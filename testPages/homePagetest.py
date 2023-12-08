import pytest

from selenium.webdriver.common.by import By
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
    ContactUsButton = (By.CSS_SELECTOR, "a[href='/contact_us']")
    TestCaseButton = (By.CSS_SELECTOR, "a[href='/test_cases']")
    productPageButton = (By.CSS_SELECTOR, "a[href='/products']")
    CartPageButton = (By.CSS_SELECTOR, "a[href='/view_cart']")
    viewProductLocator = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    category_locator = (By.XPATH, "//div[@class='left-sidebar']/h2")
    woman_category = (By.XPATH, "//a[@href='#Women']")
    woman_category_productList = (By.XPATH, "//div[@id='Women']/div/ul/li/a")
    woman_dress_category = (By.CSS_SELECTOR, "a[href='/category_products/1']")
    Men_category = (By.CSS_SELECTOR, "//a[normalize-space()='Men']")

    def __init__(self, driver):
        self.driver = driver

    def signupButton(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
        loginepage = loginPage(self.driver)
        return loginepage

    def contactUsButton(self):
        self.driver.find_element(*HomePage.ContactUsButton).click()
        contactusPage = contactUs(self.driver)
        return contactusPage

    def testCaseButton(self):
        self.driver.find_element(*HomePage.TestCaseButton).click()
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

    def category(self):
        category_text = self.driver.find_element(*HomePage.category_locator).text
        return category_text

    def WomanCategory(self):
        self.driver.find_element(*HomePage.woman_category).click()
        # self.driver.find_element(By.CSS_SELECTOR , "a[href = '/category_products/1']").click()
        product_list = []
        product_list = self.driver.find_elements(*HomePage.woman_category_productList)
        for product in product_list:
            if (product.text == "Dress"):
                product.click()
                product_page = productPage(self.driver)
                return product_page
                break;

    @pytest.fixture(params=signUpPageData.homepageTestData)
    def getData(self, request):
        return request.param
