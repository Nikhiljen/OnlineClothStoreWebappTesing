# Test Case 6: Contact Us Form
from selenium.webdriver.common.by import By

from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestSix(baseClass):

    def test_contactusFormButton(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        # 4. Click on 'Contact Us' button
        contactButton = HomePage(self.driver)
        contactPage = contactButton.contactUsButton()

        # 5. Verify 'GET IN TOUCH' is visible
        verifyText = contactPage.get_intouchText()
        assert "GET IN TOUCH" in verifyText

        # 6. Enter name, email, subject and message
        contactPage.fill_up_data()

        # 7. Upload file
        # using send keys need file path and file input locator

        # 8. Click 'Submit' button
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

        # 9. Click OK button
        contactPage.alert_check()

        # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        successMessage = contactPage.verify_Contactus_message()
        assert "Success! Your details have been submitted successfully." in successMessage

        # 11. Click 'Home' button and verify that landed to home page successfully
        homeUrl = contactPage.homePage_return()
        assert 'https://automationexercise.com/' == homeUrl
