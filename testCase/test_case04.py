# Test Case 4: Logout User

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage
class TestFour(baseClass):
    def test_logoutUser(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        self.is_homePage_visible()
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)

        # 4. Click on 'Signup / Login' button
        # 5. Verify 'Login to your account' is visible
        loginPage = homepage.signupButton()
        verifyText = loginPage.verifyLoginText()
        assert 'Login to your account' in verifyText

        # 6. Enter correct email address and password
        # 7. Click 'login' button
        loginPage.loginWithCorrectCredential()

        # 8. Verify that 'Logged in as username' is visible
        loginUserText = self.verifyLoginAsUser()
        assert 'Logged in as Nikhil' in loginUserText

        # 9. Click 'Logout' button
        # 10. Verify that user is navigated to login page
        login_page_url = self.logoutAccountSuccessful()
        assert self.driver.current_url == login_page_url, f"Expected URL: {login_page_url}, Actual URL: {self.driver.current_url}"
