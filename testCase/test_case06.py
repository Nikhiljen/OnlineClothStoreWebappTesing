# Test Case 6: Contact Us Form


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestSix(baseClass):

    def test_contactusFormButton(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        text = self.is_homePage_visible()
        assert "Automation" in text

        contactButton = HomePage(self.driver)

        # 4. Click on 'Contact Us' button
        # 5. Verify 'GET IN TOUCH' is visible
        contactPage = contactButton.contactUsButton()
        verifyText = contactPage.getintouchText()
        assert "GET IN TOUCH" in verifyText

        # 6. Enter name, email, subject and message
        # 7. Upload file
        # 8. Click 'Submit' button
        # 9. Click OK button
        contactPage.fillupdata()
        contactPage.alertcheck()

        # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        successMessage = contactPage.verifyContactusmessage()
        assert "Success! Your details have been submitted successfully." in successMessage

        # 11. Click 'Home' button and verify that landed to home page successfully
        homeUrl = contactPage.homepagereturn()
        assert 'https://automationexercise.com/' == homeUrl
