# Test Case 18: View Category Products


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestEighteen(baseClass):

    def test_view_category_products(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 3. Verify that categories are visible on left sidebar
        homepage = HomePage(self.driver)
        category_text = homepage.category()
        assert "CATEGORY" in category_text

        # 4. Click on 'Women' category
        # 5. Click on any category link under 'Women' category, for example: Dress
        woman_dress_page = homepage.WomanCategory()

        # 6. Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
        category_text = woman_dress_page.woman_dress_category()
        assert "WOMEN - DRESS PRODUCTS" in category_text, "Category text does not match the expected text"
