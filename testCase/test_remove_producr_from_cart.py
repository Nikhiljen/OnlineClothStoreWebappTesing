from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage

class TestSeventeen(baseClass):
    def test_removeProductFromCart(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)

        # 4. Add products to cart

        product = homepage.viewSampleProduct()
        product.addToCart()
        product.continueButton()

        # 5. Click 'Cart' button
        # 6. Verify that cart page is displayed
        cart_page = homepage.CartButton()

        currentUrl = cart_page.cartPageVerification()
        actualUrl = "https://automationexercise.com/view_cart"
        assert currentUrl == actualUrl

        # 7. Click 'X' button corresponding to particular product
        current_url = cart_page.removeProduct()
        # 8. Verify that product is removed from the cart
        expected_url = "https://automationexercise.com/products"
        assert expected_url==  current_url
