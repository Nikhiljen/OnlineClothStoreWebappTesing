from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage
from testCase.test_HomePage import homepage


# Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Scroll down to footer
# 5. Verify text 'SUBSCRIPTION'
# 6. Enter email address in input and click arrow button
# 7. Verify success message 'You have been successfully subscribed!' is visible
class TestTen(baseClass):

    def test_subscribeVerificaton(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        subscribtion = HomePage(self.driver)
        subscription_text_element = subscribtion.verifySubscriptionTextElement()
        assert  "SUBSCRIPTION" in subscription_text_element,  "Subscription text is not visible."

        success_message_element = subscribtion.subscriptionSuccefull()
        assert success_message_element.is_displayed(), "Success message is not visible."