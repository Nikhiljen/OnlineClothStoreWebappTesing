# Test Case 5: Register User with existing email


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestFive(baseClass):

    def test_register_User_withExisting_Exit(self):
        log = self.getLogger()
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)

        # 4. Click on 'Signup / Login' button
        # 5. Verify 'New User Signup!' is visible
        signupPage = homepage.signupButton()
        verifyText = signupPage.verifySignUpText()
        assert 'New User Signup!' in verifyText
        log.info("New User Signup!")

        # 6. Enter name and already registered email address
        # 7. Click 'Signup' button
        # 8. Verify error 'Email Address already exist!' is visible
        returnText = signupPage.UserExitEmail()
        assert "Email Address already exist!" in returnText
