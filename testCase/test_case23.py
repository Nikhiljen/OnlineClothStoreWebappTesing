# Test Case 23: Verify address details in checkout page

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestTwentyThree(baseClass):
    def test_verify_Address_Details_In_CheckoutPage(self):
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
        cart_page = product.ViewCartButton()
        currentUrl = cart_page.cartPageVerification()
        actual_Url = "https://automationexercise.com/view_cart"
        assert currentUrl == actual_Url

        # 11. Click Proceed To Checkout
        cart_page.CheckoutPageButton()

        # 12. Verify Address Details and Review Your Order
        # 13. Verify that the billing address is same address filled at the time registration of account

        # 14. Click 'Delete Account' button
        # 15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
        delete_account_message = self.verifyDeleteAccountSuccessful()
        assert "ACCOUNT DELETED!" in delete_account_message
