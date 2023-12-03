# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'View Product' for any product on home page
# 5. Verify product detail is opened
# 6. Increase quantity to 4
# 7. Click 'Add to cart' button
# 8. Click 'View Cart' button
# 9. Verify that product is displayed in cart page with exact quantity
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestThirteen(baseClass):

    def test_addProductInCart(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)
        product = homepage.viewSampleProduct()

        verifyLink = product.productViewLink()
        assert verifyLink == "https://automationexercise.com/product_details/1"

        product.productQuntity(4)
        product.addToCart()

        cartpage = product.ViewCartButton()
        text = cartpage.productQuntity()




