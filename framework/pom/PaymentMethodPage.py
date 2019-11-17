from framework.base.Selenium_driver import SeleniumDriver

class PaymentMethodPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _continue = "continue-top"

    def clickToContinue(self):
        self.elementClick(self._continue,"id")