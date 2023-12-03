# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Test Cases' button
# 5. Verify user is navigated to test cases page successfully
from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage

class TestSeven(baseClass):

    def test_testCasePageButton(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)
        testCasePage = homepage.testCaseButton()

        testcaseurl = testCasePage.testCasepage(self)
        assert 'https://automationexercise.com/test_cases' == testcaseurl, f"Expected URL: {'https://automationexercise.com/test_cases'}, Actual URL: {testcaseurl}"