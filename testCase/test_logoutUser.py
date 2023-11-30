from Utilities.baseClass import baseClass
from testPages.logineWithCorrectUser import loginePage


class TestFour(baseClass):
    def test_LogineWithCorrectData(self):

        self.is_homePage_visible()
        verifyText = self.verifyLogineText()
        assert 'Login to your account' in verifyText

        logine = loginePage(self.driver)
        logine.logineWithCorrectCredintial()

        loginUserText = self.verifyLogineAsUser()
        assert 'Logged in as Nikhil' in loginUserText


