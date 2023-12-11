# Test Case 19: View & Cart Brand Products
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestTwenty(baseClass):
    def test_view_and_cartBrandProducts(self):

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 3. Click on 'Products' button
        homepage = HomePage(self.driver)
        Product_page = homepage.productButton()

        # 4. Verify that Brands are visible on left sidebar
        verify_Brand_text = Product_page.Brands_product()
        assert "BRANDS" in verify_Brand_text

        # 5. Click on any brand name
        # 6. Verify that user is navigated to brand page and brand products are displayed
        link_getting = Product_page.Brands_product_list()
        # 7. On left sidebar, click on any other brand link
        # 8. Verify that user is navigated to that brand page and can see products
        actual_link = "https://automationexercise.com/brand_products/Madame"
        assert actual_link == link_getting
