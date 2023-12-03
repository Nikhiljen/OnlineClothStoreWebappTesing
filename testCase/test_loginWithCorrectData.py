# Test Case 2: Login User with correct email and password
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage
class TestTwo(baseClass):
    def test_LogineWithCorrectData(self):
        self.is_homePage_visible()

        homepage = HomePage(self.driver)

        signupPage = homepage.signupButton()
        UserSignup = signupPage.newUserSignUp()
        UserSignup.accountInformationPage()
        UserSignup.addressInformationPage()
        signUpText = UserSignup.VerifyAccountCreationPage()
        assert "ACCOUNT CREATED!" in signUpText

        self.logoutAccountSuccessful()

        verifyText = signupPage.verifyLogineText()
        assert 'Login to your account' in verifyText

        signupPage.logineWithCorrectCredintial()

        loginUserText = self.verifyLogineAsUser()
        assert 'Logged in as Nikhil' in loginUserText

        # deleteAccountText = self.verifyDeleteAccountSuccessful()
        # assert "ACCOUNT DELETED!" in deleteAccountText
