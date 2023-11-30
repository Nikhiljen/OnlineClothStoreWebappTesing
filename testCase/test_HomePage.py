import time

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestOne(baseClass):
    def test_HomePageVisible(self):
        log = self.getLogger()

        text = self.is_homePage_visible()
        assert "automation" in text

        verifyText = self.verifySignUpText()
        assert 'New User Signup!' in verifyText
        log.info("New User Signup!")

        verifySignupTextPage = self.signUpData()
        assert "ENTER ACCOUNT INFORMATION" in verifySignupTextPage

        homepage = HomePage(self.driver)

        homepage.accountInformationPage()
        homepage.addressInformationPage()

        signUpText = homepage.VerifyAccountCreationPage()
        assert "ACCOUNT CREATED!" in signUpText

        loginUserText = self.verifyLogineAsUser()
        assert 'Logged in as Nikhil' in loginUserText

        deleteAccountText = self.verifyDeleteAccountSuccessful()
        assert "ACCOUNT DELETED!" in deleteAccountText
