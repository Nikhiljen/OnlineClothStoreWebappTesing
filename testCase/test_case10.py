# Test Case 10: Verify Subscription in home page
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestTen(baseClass):

    def test_subscribeEmailVerificationHomepage(self):
        # Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 4. Scroll down to footer
        subscription = HomePage(self.driver)

        # 5. Verify text 'SUBSCRIPTION'
        # 6. Enter email address in input and click arrow button
        subscription_text_element = subscription.verifySubscriptionTextHomepage()
        assert "SUBSCRIPTION" in subscription_text_element, "Subscription text is not visible."

        # 7. Verify success message 'You have been successfully subscribed!' is visible
        success_message_element = subscription.subscriptionSuccessfulHomepage()
        assert success_message_element.is_displayed(), "Success message is not visible."
