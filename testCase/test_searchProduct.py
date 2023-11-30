from Utilities.baseClass import baseClass
from testPages.productPage import productPageTest

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. Enter product name in search input and click search button
# 7. Verify 'SEARCHED PRODUCTS' is visible
# 8. Verify all the products related to search are visible
class TestNine(baseClass):

    def test_ProductListPageButton(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        productSearch = productPageTest(self.driver)

        productSearch.productlinkpage()

        searchproducttext = productSearch.searchProduct()
        assert "SEARCHED PRODUCTS" in searchproducttext

        product_list = productSearch.productsearchList()
        for product_element in product_list:
            assert product_element.is_displayed(), "Products list is not visible on the webpage"

