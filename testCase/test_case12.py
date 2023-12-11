# Test Case 12: Add Products in Cart


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestTwelve(baseClass):

    def test_addProductInCart(self):
        # . Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 4. Click 'Products' button
        homepage = HomePage(self.driver)
        product = homepage.productButton()

        # 5. Hover over first product and click 'Add to cart'
        product.productAddToCartItem1()
        # 6. Click 'Continue Shopping' button
        product.continueButton()
        # 7. Hover over second product and click 'Add to cart'
        product.productAddToCartItem2()
        # 8. Click 'View Cart' button
        product.ViewCartButton()

        # 9. Verify both products are added to Cart
        # 10. Verify their prices, quantity and total price
