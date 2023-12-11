# Test Case 15: Place Order: Register before Checkout
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage

class TestFourteen(baseClass):
    def test_palceOrderafterRegistration(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)
        # 4. Click 'Signup / Login' button
        new_user = homepage.signupButton()
        new_user_details = new_user.newUserSignUp()

        # 5. Fill all details in Signup and create account
        new_user_details.accountInformationPage()
        new_user_details.addressInformationPage()

        # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        new_user_details.VerifyAccountCreationPage()

        # 7. Verify ' Logged in as username' at top
        self.verifyLogineAsUser()

        # 8. Add products to cart
        # 9. Click 'Cart' button
        product = homepage.viewSampleProduct()
        product.addToCart()

        # 10. Verify that cart page is displayed
        cartpage = product.ViewCartButton()
        currentUrl = cartpage.cartPageVerification()
        acctualUrl = "https://automationexercise.com/view_cart"
        assert currentUrl == acctualUrl

        # 11. Click Proceed To Checkout
        cartpage.CheckoutPageButton()

        # 14. Verify Address Details and Review Your Order

        # 15. Enter description in comment text area and click 'Place Order'
        place_order = cartpage.order_Description()

        # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
        place_order.CardDetails()

        # 17. Click 'Pay and Confirm Order' button
        confirmPage = place_order.payOrder()

        # 18. Verify success message 'Your order has been placed successfully!'
        order_success_message = confirmPage.OrderConfirmVerification()
        assert "Congratulations!" in order_success_message

        # 19. Click 'Delete Account' button
        # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
        delete_account_messge = self.verifyDeleteAccountSuccessful()
        assert "ACCOUNT DELETED!" in delete_account_messge
