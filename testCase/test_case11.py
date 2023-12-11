# Test Case 11: Verify Subscription in Cart page


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestEleven(baseClass):

    def test_subscribeEmailVerificationCartPage(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)
        # 4. Click 'Cart' button
        Subscription_On_cartPage = homepage.CartButton()

        # 5. Scroll down to footer
        # 6. Verify text 'SUBSCRIPTION'
        subscription_text_element = Subscription_On_cartPage.verifySubscriptionText_Element_onCartPage()
        assert "SUBSCRIPTION" in subscription_text_element, "Subscription text is not visible."

        # 7. Enter email address in input and click arrow button
        # # 8. Verify success message 'You have been successfully subscribed!' is visible
        success_message_element = Subscription_On_cartPage.subscription_Successful_onCartPage()
        assert success_message_element.is_displayed(), "Success message is not visible."
