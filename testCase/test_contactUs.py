

from Utilities.baseClass import baseClass
from testPages.contactUsFrom import contactUs


# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Contact Us' button
# 5. Verify 'GET IN TOUCH' is visible
# 6. Enter name, email, subject and message
# 7. Upload file
# 8. Click 'Submit' button
# 9. Click OK button
# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
# 11. Click 'Home' button and verify that landed to home page successfully


class TestSix(baseClass):

    def test_contactusFormButton(self):
        text = self.is_homePage_visible()
        assert "Automation" in text

        contactclick = contactUs(self.driver)

        verifyText = contactclick.contactUsElement()
        assert "GET IN TOUCH" in verifyText

        contactclick.fillupdata()
        contactclick.alertcheck()

        successMessge = contactclick.verifyContactusmessage()
        assert "Success! Your details have been submitted successfully." in successMessge

        homeUrl = contactclick.homepagereturn()
        assert 'https://automationexercise.com/' == homeUrl


