# Test Case 13: Verify Product quantity in Cart
from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestThirteen(baseClass):

    def test_addProductInCart(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 4. Click 'View Product' for any product on home page
        homepage = HomePage(self.driver)
        product = homepage.viewSampleProduct()

        # 5. Verify product detail is opened
        verifyLink = product.productViewLink()
        assert verifyLink == "https://automationexercise.com/product_details/1"

        # 6. Increase quantity to 4
        increased_quantity = 4
        product.product_Quantity(increased_quantity)
        # 7. Click 'Add to cart' button
        product.addToCart()

        # 8. Click 'View Cart' button
        cart_page = product.ViewCartButton()
        # 9. Verify that product is displayed in cart page with exact quantity
        expected_quantity = self.driver.find_element(By.XPath, "// tr[  # id='product-1']/td[4]/button").text
        assert " 4" in expected_quantity, "Return value is not equal to expected value"





