from framework.base.Selenium_driver import SeleniumDriver

class SignUpPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username = "ap_email"
    _password = "ap_password"
    _signinBtn = "signInSubmit"

    def login(self,email,pwd):
        self.sendKeys(email,self._username,"id")
        self.sendKeys(pwd,self._password,"id")
        self.elementClick(self._signinBtn,"id")


