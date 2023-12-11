# Test Case 9: Search Product
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestNine(baseClass):

    def test_ProductListPageButton(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 4. Click on 'Products' button
        homepage = HomePage(self.driver)
        product = homepage.productButton()

        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        product_page_text = product.product_link_page()
        assert "ALL PRODUCTS" in product_page_text

        # 6. Enter product name in search input and click search button
        # 7. Verify 'SEARCHED PRODUCTS' is visible
        search_product_text = product.searchProduct()
        assert "SEARCHED PRODUCTS" in search_product_text

        # 8. Verify all the products related to search are visible
        product_list = product.are_products_visible()
        assert product_list, "Not all products are visible"
