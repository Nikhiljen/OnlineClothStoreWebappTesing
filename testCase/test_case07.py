# Test Case 7: Verify Test Cases Page


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage

class TestSeven(baseClass):

    def test_testCasePageButton(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        homepage = HomePage(self.driver)

        # 4. Click on 'Test Cases' button
        testCasePage = homepage.testCaseButton()

        # 5. Verify user is navigated to test cases page successfully
        testcase_url = testCasePage.testCasepage()
        assert 'https://automationexercise.com/test_cases' == testcase_url, f"Expected URL: {'https://automationexercise.com/test_cases'}, Actual URL: {testcase}"