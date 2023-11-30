from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass


class productPageTest(baseClass):
    productPageButton = (By.CSS_SELECTOR, "a[href='/products']")
    textView = (By.CLASS_NAME, "title.text-center")
    productList = (By.XPATH, "//div[@class='features_items']")
    productView = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    name = (By.CSS_SELECTOR, "div[class='product-information'] h2")
    category = (By.XPATH, "//div[@class='product-information']/p[1]")
    price = (By.XPATH, "//div[@class='product-information']/span/span")
    availability = (By.XPATH, "//div[@class='product-information']/p[2]")
    condition = (By.XPATH, "//div[@class='product-information']/p[3]")
    brand = (By.XPATH, "//div[@class='product-information']/p[4]")
    serachLocator = (By.ID, "search_product")
    submitSearchButton = (By.ID, "submit_search")
    returnresultText = (By.CSS_SELECTOR, ".title.text-center")
    productRelatedSearch = (By.CSS_SELECTOR, ".features_items")

    def __init__(self, driver):
        self.driver = driver

    def productlinkpage(self):
        self.driver.find_element(*productPageTest.productPageButton).click()
        productText = self.driver.find_element(*productPageTest.textView).text
        return productText

    def searchProduct(self):
        self.driver.find_element(*productPageTest.serachLocator).send_keys("Tshirt")
        self.driver.find_element(*productPageTest.submitSearchButton).click()
        return self.driver.find_element(*productPageTest.returnresultText).text

    def productsearchList(self):
        return self.driver.find_elements(*productPageTest.productRelatedSearch)

    def productlist(self):
        return self.driver.find_elements(*productPageTest.productList)

    def productViewLink(self):
        self.driver.find_element(*productPageTest.productView).click()

    def productName(self):
        return self.driver.find_element(*productPageTest.name).text

    def productCategory(self):
        return self.driver.find_element(*productPageTest.category).text

    def productPrice(self):
        return self.driver.find_element(*productPageTest.price).text

    def productAvailability(self):
        return self.driver.find_element(*productPageTest.availability).text

    def productCondition(self):
        return self.driver.find_element(*productPageTest.condition).text

    def productBrand(self):
        return self.driver.find_element(*productPageTest.brand).text
