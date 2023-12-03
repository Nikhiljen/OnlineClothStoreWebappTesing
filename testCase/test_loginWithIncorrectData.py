# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter incorrect email address and password
# 7. Click 'login' button
# 8. Verify error 'Your email or password is incorrect!' is visible

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestThree(baseClass):
    def test_LogineWithIncorrectData(self):

        self.is_homePage_visible()
        homepage = HomePage(self.driver)

        signupPage = homepage.signupButton()
        verifyText = signupPage.verifyLogineText()
        assert 'Login to your account' in verifyText

        messageSuceess = signupPage.logineWithIncorrectCredintial()
        assert "Your email or password is incorrect!" in messageSuceess
