from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestFive(baseClass):

    def test_verifyUseralredyExit(self):
        log = self.getLogger()

        self.is_homePage_visible()
        homepage = HomePage(self.driver)

        signupPage = homepage.signupButton()

        verifyText = signupPage.verifySignUpText()
        assert 'New User Signup!' in verifyText
        log.info("New User Signup!")

        returnText = signupPage.UserExitEmail()
        assert "Email Address already exist!" in returnText


