# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Test Cases' button
# 5. Verify user is navigated to test cases page successfully
from Utilities.baseClass import baseClass
from testPages.testCasePage import testCasePage


class TestSeven(baseClass):

    def test_testCasePageButton(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        returnText = testCasePage.testCaselinkpage(self)
        assert "Below is the list of test Cases for you to practice the Automation" in returnText