# Test Case 3: Login User with incorrect email and password
import pytest

from Utilities.baseClass import baseClass
from testData.testSignUpData import signUpPageData
from testPages.homePagetest import HomePage


class TestThree(baseClass):
    def test_LoginWithIncorrectData(self, getData):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        self.is_homePage_visible()
        text = self.is_homePage_visible()
        assert "Automation" in text
        homepage = HomePage(self.driver)

        # 4. Click on 'Signup / Login' button
        # 5. Verify 'Login to your account' is visible
        signupPage = homepage.signupButton()
        verifyText = signupPage.verifyLoginText()
        assert 'Login to your account' in verifyText

        # 6. Enter incorrect email address and password
        # 7. Click 'login' button
        # 8. Verify error 'Your email or password is incorrect!' is visible
        message_Success = signupPage.loginWithIncorrectCredential(getData)
        assert "Your email or password is incorrect!" in message_Success

    @pytest.fixture(params=signUpPageData.getTestData("TC0003"))
    def getData(self, request):
        return request.param
