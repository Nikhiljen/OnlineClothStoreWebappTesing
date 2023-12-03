from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.baseClass import baseClass
from testPages.CartPage import CartPage


class productPage(baseClass):
    textView = (By.CSS_SELECTOR, ".title.text-center")
    productList = (By.XPATH, "//div[@class='features_items']")
    name = (By.CSS_SELECTOR, "div[class='product-information'] h2")
    category = (By.XPATH, "//div[@class='product-information']/p[1]")
    price = (By.XPATH, "//div[@class='product-information']/span/span")
    availability = (By.XPATH, "//div[@class='product-information']/p[2]")
    condition = (By.XPATH, "//div[@class='product-information']/p[3]")
    brand = (By.XPATH, "//div[@class='product-information']/p[4]")
    serachLocator = (By.ID, "search_product")
    submitSearchButton = (By.ID, "submit_search")
    returnresultText = (By.CSS_SELECTOR, ".title.text-center")
    productMouseHover1 = (By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]")
    productMouseHover2 = (By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]")
    continueShoppingLocator = (By.XPATH, "//div[@class='modal-content']/div[3]/button")
    viewCartLocator = (By.XPATH, "//div[@class='modal-content']/div[2]/p[2]/a")
    productquntityLocator = (By.ID, "quantity")
    addCartButton  = ()

    def __init__(self, driver):
        self.driver = driver

    def productlinkpage(self):
        productText = self.driver.find_element(*productPage.textView).text
        return productText

    def searchProduct(self):
        self.driver.find_element(*productPage.serachLocator).send_keys("Tshirt")
        self.driver.find_element(*productPage.submitSearchButton).click()
        return self.driver.find_element(*productPage.returnresultText).text

    def are_products_visible(self):
        product_elements = self.driver.find_elements(*productPage.productList)

        for product_element in product_elements:
            if not product_element.is_displayed():
                return False

        return True

    def productViewLink(self):
        return self.driver.current_url

    def productName(self):
        return self.driver.find_element(*productPage.name).text

    def productCategory(self):
        return self.driver.find_element(*productPage.category).text

    def productPrice(self):
        return self.driver.find_element(*productPage.price).text

    def productAvailability(self):
        return self.driver.find_element(*productPage.availability).text

    def productCondition(self):
        return self.driver.find_element(*productPage.condition).text

    def productBrand(self):
        return self.driver.find_element(*productPage.brand).text


    def productAddToCartItem1(self):
        productOption1 = self.driver.find_element(*productPage.productMouseHover1)
        actions = ActionChains(self.driver)
        actions.move_to_element(productOption1).perform()
        productaction1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]")))
        actions.move_to_element(productaction1).perform()


    def productAddToCartItem2(self):
        productOption2 = self.driver.find_element(*productPage.productMouseHover2)
        actions = ActionChains(self.driver)
        actions.move_to_element(productOption2).perform()
        productaction2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/a[1]")))
        actions.move_to_element(productaction2).perform()


    def continueButton(self):
        try:
            continueButton = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='modal-content']/div[3]/button")))
            continueButton.click()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as e:
            print(f"Error: {e}")
    def ViewCartButton(self) :
        try:
            viewCartButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                   (By.XPATH, "//u[normalize-space()='View Cart']")))
            viewCartButton.click()
            Cartpage = CartPage(self.driver)
            return Cartpage

        except Exception as e:
            print(f"Error: {e}")

    def productQuntity(self, new_quantity):
        quntity_input = self.driver.find_element(*productPage.productquntityLocator)
        quntity_input.clear()
        quntity_input.send_keys(str(new_quantity))

    def addToCart(self):
        addCartButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='button']")))
        addCartButton.click()
