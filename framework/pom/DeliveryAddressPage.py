from framework.base.Selenium_driver import SeleniumDriver

class DeliveryAddressPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _addressBtn = "//a[contains(text(),'Deliver to this address')]"

    def clickAddressBtn(self):
        self.elementClick(self._addressBtn,"xpath")
    