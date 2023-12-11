# Test Case 1: Register User


from Utilities.baseClass import baseClass
from testPages.homePagetest import HomePage


class TestOne(baseClass):
    def test_HomePageVisible(self):
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        log = self.getLogger()
        text = self.is_homePage_visible()
        assert "Automation" in text
        homepage = HomePage(self.driver)

        # 4. Click on 'Signup / Login' button
        # 5. Verify 'New User Signup!' is visible
        signupPage = homepage.signupButton()
        verifyText = signupPage.verifySignUpText()
        assert 'New User Signup!' in verifyText
        log.info("New User Signup!")

        # 6. Enter name and email address
        # 7. Click 'Signup' button

        # 13. Click 'Create Account button'
        # 14. Verify that 'ACCOUNT CREATED!' is visible
        newUserSignup = signupPage.newUserSignUp()

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        accountInfoText = newUserSignup.accountInformationText()
        assert "ENTER ACCOUNT INFORMATION" in accountInfoText, "No enter account information"
        log.info("ENTER ACCOUNT INFORMATION")

        # 9. Fill details: Title, Name, Email, Password, Date of birth
        # 10. Select checkbox 'Sign up for our newsletter!'
        # 11. Select checkbox 'Receive special offers from our partners!'
        # 12. Fill details: First name,
        # Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        newUserSignup.accountInformationPage()
        newUserSignup.addressInformationPage()

        # 13 "Click Create Account button"
        # 14."Verify that 'ACCOUNT CREATED!' is visible''
        signUpText = newUserSignup.VerifyAccountCreationPage()
        assert "ACCOUNT CREATED!" in signUpText
        log.info("Account Creation Successful")

        # 15. Click 'Continue' button
        # 16. Verify that 'Logged in as username' is visible
        loginUserText = self.verifyLoginAsUser()
        assert 'Logged in as Nikhil' in loginUserText
        log.info("Logged as Username is successful")

        # 17. Click 'Delete Account' button
        # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        deleteAccountText = self.verifyDeleteAccountSuccessful()
        assert "ACCOUNT DELETED!" in deleteAccountText
        log.info("account delete successful")