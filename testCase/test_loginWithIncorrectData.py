from Utilities.baseClass import baseClass
from testPages.logineWithCorrectUser import loginePage


class TestThree(baseClass):
    def test_LogineWithIncorrectData(self):

        self.is_homePage_visible()
        verifyText = self.verifyLogineText()
        assert 'Login to your account' in verifyText

        logine = loginePage(self.driver)
        messageSuceess = logine.logineWithIncorrectCredintial()
        assert "Your email or password is incorrect!" in messageSuceess
