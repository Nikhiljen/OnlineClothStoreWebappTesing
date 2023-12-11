# Test Case 16: Place Order: Login before Checkout
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestSixteen(baseClass):
    def test_login_before_checkout(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text
        homepage = HomePage(self.driver)

        # 4. Click 'Signup / Login' button
        User_login = homepage.signupButton()
        # 5. Fill email, password and click 'Login' button
        User_login.loginWithCorrectCredential()
        # 6. Verify 'Logged in as username' at top
        self.verifyLoginAsUser()

        # 8. Add products to cart
        product = homepage.viewSampleProduct()
        product.addToCart()
        product.continueButton()
        # 9. Click 'Cart' button
        cart_page = homepage.CartButton()
        # 10. Verify that cart page is displayed
        currentUrl = cart_page.cartPageVerification()
        actualUrl = "https://automationexercise.com/view_cart"
        assert currentUrl == actualUrl

        # 11. Click Proceed To Checkout
        cart_page.CheckoutPageButton()

        # 12. Verify Address Details and Review Your Order

        # 15. Enter description in comment text area and click 'Place Order'
        place_order = cart_page.order_Description()

        # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
        place_order.CardDetails()

        # 17. Click 'Pay and Confirm Order' button
        confirmPage = place_order.payOrder()

        # 18. Verify success message 'Your order has been placed successfully!'
        order_success_message = confirmPage.OrderConfirmVerification()
        assert "Congratulations!" in order_success_message

        # 19. Click 'Delete Account' button
        # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
        delete_account_message = self.verifyDeleteAccountSuccessful()
        assert "ACCOUNT DELETED!" in delete_account_message
