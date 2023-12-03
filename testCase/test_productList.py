from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. The products list is visible
# 7. Click on 'View Product' of first product
# 8. User is landed to product detail page
# 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
class TestEight(baseClass):

    def test_ProductListPageButton(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)
        product = homepage.productButton()

        productpagetext = product.productlinkpage()
        assert "ALL PRODUCTS" in productpagetext

        product_list = product.productlist()
        for product_element in product_list:
            assert product_element.is_displayed(), "Products list is not visible on the webpage"

        product.productViewLink()

        productname = product.productName()
        assert "Blue" in productname

        productcategory = product.productCategory()
        assert "Women > Tops" in productcategory

        productprice = product.productPrice()
        assert "Rs. 500" in productprice

        productavailibility = product.productAvailability()
        assert "In Stock" in productavailibility

        productcondition = product.productCondition()
        assert "New" in productcondition

        productbrand = product.productBrand()
        assert "Polo" in productbrand

