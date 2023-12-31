# Test Case : Place Order: Register while Checkout
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestFourteen(baseClass):

    def test_place_Order_register_while_checkout(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)

        # 4. Add products to cart
        product = homepage.viewSampleProduct()
        product.addToCart()

        # 5. Click 'Cart' button
        # 6. Verify that cart page is displayed
        cart_page = product.ViewCartButton()
        currentUrl = cart_page.cartPageVerification()
        actualUrl = "https://automationexercise.com/view_cart"
        assert currentUrl == actualUrl

        # 7. Click Proceed To Checkout
        cart_page.CheckoutPageButton()

        # 8. Click 'Register / Login' button
        # 9. Fill all details in Signup and create account
        # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        # 11. Verify ' Logged in as username' at top
        register_page = cart_page.register_link()

        new_user_details = register_page.newUserSignUp()
        new_user_details.accountInformationPage()
        new_user_details.addressInformationPage()
        New_account_text = new_user_details.VerifyAccountCreationPage()
        assert "ACCOUNT CREATED!" in New_account_text
        login_User = self.verifyLoginAsUser()
        assert "Logged in as Nikhil" in login_User

        # 12.Click 'Cart' button
        cart_page_link = homepage.CartButton()
        # 13. Click 'Proceed To Checkout' button
        cart_page_link.CheckoutPageButton()

        # 14. Verify Address Details and Review Your Order
        # 15. Enter description in comment text area and click 'Place Order'
        place_order = cart_page_link.order_Description()

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
