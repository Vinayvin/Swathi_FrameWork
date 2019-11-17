from framework.base.Selenium_driver import SeleniumDriver

class ShipmentPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _continueBtn = "//input[@value='Continue']"

    def clickContinueBtn(self):
        self.elementClick(self._continueBtn,"xpath")