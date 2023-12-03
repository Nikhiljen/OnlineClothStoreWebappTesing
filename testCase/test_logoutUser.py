# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Logout' button
# 10. Verify that user is navigated to login page

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage
class TestFour(baseClass):
    def test_logoutUser(self):
        self.is_homePage_visible()

        homepage = HomePage(self.driver)
        loginPage = homepage.signupButton()
        loginPage.logineWithCorrectCredintial()

        loginUserText = self.verifyLogineAsUser()
        assert 'Logged in as Nikhil' in loginUserText

        login_page_url = self.logoutAccountSuccessful()
        assert self.driver.current_url == login_page_url, f"Expected URL: {login_page_url}, Actual URL: {self.driver.current_url}"
