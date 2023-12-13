# Test Case 2: Login User with correct email and password
import pytest

from Utilities.baseClass import baseClass
from testData.testSignUpData import signUpPageData
from testPages.homePagetest import HomePage


class TestTwo(baseClass):
    def test_LoginWithCorrectData(self, getData):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        self.is_homePage_visible()
        text = self.is_homePage_visible()
        assert "Automation" in text
        homepage = HomePage(self.driver)

        signupPage = homepage.signupButton()
        # 4. Click on 'Signup / Login' button
        # 5. Verify 'Login to your account' is visible
        verifyText = signupPage.verifyLoginText()
        assert 'Login to your account' in verifyText

        # 6. Enter correct email address and password
        # 7. Click 'login' button
        signupPage.loginWithCorrectCredential(getData)

        # 8. Verify that 'Logged in as username' is visible
        loginUserText = self.verifyLoginAsUser()
        assert 'Logged in as Nikhil' in loginUserText

        # 9. Click 'Delete Account' button
        # 10. Verify that 'ACCOUNT DELETED!' is visible
        # deleteAccountText = self.verifyDeleteAccountSuccessful()
        # assert "ACCOUNT DELETED!" in deleteAccountText

    @pytest.fixture(params=signUpPageData.getTestData("TC0002"))
    def getData(self, request):
        return request.param
