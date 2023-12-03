# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'Cart' button
# 5. Scroll down to footer
# 6. Verify text 'SUBSCRIPTION'
# 7. Enter email address in input and click arrow button
# # 8. Verify success message 'You have been successfully subscribed!' is visible
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestEleven(baseClass):

    def test_subscribeEmailVerificatononCartPage(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)
        SubscriptionOncartPage = homepage.CartButton()

        subscription_text_element = SubscriptionOncartPage.verifySubscriptionTextElementonCartPage()
        assert "SUBSCRIPTION" in subscription_text_element, "Subscription text is not visible."

        success_message_element = SubscriptionOncartPage.subscriptionSuccefullonCartPage()
        assert success_message_element.is_displayed(), "Success message is not visible."