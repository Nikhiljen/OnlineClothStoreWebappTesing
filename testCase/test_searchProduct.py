from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage

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
        
        homepage = HomePage(self.driver)
        product = homepage.productButton()

        productpagetext = product.productlinkpage()
        assert "ALL PRODUCTS" in productpagetext

        searchproducttext = product.searchProduct()
        assert "SEARCHED PRODUCTS" in searchproducttext

        product_list = product.are_products_visible()
        assert product_list, "Not all products are visible"
