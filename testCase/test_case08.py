# Test Case 8: Verify All Products and product detail page
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestEight(baseClass):

    def test_ProductListPageButton(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)

        # 4. Click on 'Products' button
        product = homepage.productButton()

        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        product_page_text = product.product_link_page()
        assert "ALL PRODUCTS" in product_page_text

        # 6. The products list is visible
        product_list = product.productlist()
        for product_element in product_list:
            assert product_element.is_displayed(), "Products list is not visible on the webpage"

        # 7. Click on 'View Product' of first product
        # 8. User is landed to product detail page
        product.productViewLink()

        # 9. Verify that detail is visible: product name, category, price, availability, condition, brand
        product_name = product.productName()
        assert "Blue" in product_name

        product_category = product.productCategory()
        assert "Women > Tops" in product_category

        product_price = product.productPrice()
        assert "Rs. 500" in product_price

        product_availability = product.productAvailability()
        assert "In Stock" in product_availability

        product_condition = product.productCondition()
        assert "New" in product_condition

        product_brand = product.productBrand()
        assert "Polo" in product_brand
