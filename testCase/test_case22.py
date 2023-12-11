# Test Case 22: Add to cart from Recommended items


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.baseClass import baseClass
from testPages.productPage import productPage


class TestTwentyTwo(baseClass):
    def test_addtocartfrom_recommended_items(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 3. Scroll to bottom of page
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "div[class='recommended_items'] h2[class='title text-center']")
        while not element.is_displayed():
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Optionally, you can add a delay or wait for the element explicitly
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))

        # 4. Verify 'RECOMMENDED ITEMS' are visible
        verifiedText = self.driver.find_element(By.CSS_SELECTOR,
                                                "div[class='recommended_items'] h2[class='title text-center']").text
        assert verifiedText == "RECOMMENDED ITEMS"

        # 5. Click on 'Add To Cart' on Recommended product
        self.driver.find_element(By.XPATH, "//div[@class='item active']//div[1]//div[1]//div[1]//div[1]//a[1]").click()
        product_page = productPage(self.driver)

        # 6. Click on 'View Cart' button
        product_page.ViewCartButton()

        # 7. Verify that product is displayed in cart page
        current_url = self.driver.current_url
        assert "https://automationexercise.com/view_cart" == current_url
