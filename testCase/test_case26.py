# Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestTwentySix(baseClass):
    def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality(self):
        # Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 4. Scroll down page to bottom
        # 5. Verify 'SUBSCRIPTION' is visible
        subscription = HomePage(self.driver)
        subscription_text_element = subscription.verifySubscriptionTextHomepage()
        assert "SUBSCRIPTION" in subscription_text_element, "Subscription text is not visible."
        self.driver.implicitly_wait(5)

        # 6. Scroll up page to top

        self.driver.execute_script("window.scrollTo(0, 0);")
        # Wait for a short period to allow the scroll-up animation (adjust as needed)
        self.driver.implicitly_wait(5)

        # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
        text_to_verify = "Full-Fledged practice website for Automation Engineers"
        # Wait for the text to be visible on the screen
        return_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='item active'] h2")))
        assert return_text.text == text_to_verify, print("Test is not successfully Passed")