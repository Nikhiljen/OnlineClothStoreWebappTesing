# Test Case 21: Add review on product
from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestTwentyOne(baseClass):
    def test_addReview_onProduct(self):

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        text = self.is_homePage_visible()
        assert "Automation" in text
        homepage = HomePage(self.driver)

        # 3. Click on 'Products' button
        product_page = homepage.productButton()
        # 4. Verify user is navigated to ALL PRODUCTS page successfully
        product_page_text = product_page.productlinkpage()
        acctual_text  = "ALL PRODUCTS"
        assert acctual_text == product_page_text, "This text is not correct"

        # 5. Click on 'View Product' button
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()

        # 6. Verify 'Write Your Review' is visible
        review_text = self.driver.find_element(By.CSS_SELECTOR, "a[href='#reviews']").text
        acctual_review_text = "Write Your Review"
        assert acctual_review_text == review_text, "This text is not show"

        # 7. Enter name, email and review
        self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Nikhil")
        self.driver.find_element(By.ID, "email").send_keys("nik@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#review").Send_keys("Its a very good Products")
        # 8. Click 'Submit' button
        self.driver.find_element(By.ID, "button-review").click()
        # 9. Verify success message 'Thank you for your review.'
