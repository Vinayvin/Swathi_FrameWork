from framework.base.Selenium_driver import SeleniumDriver

class PlaceOrderPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _coupon_code_apply = "spc-gcpromoinput"
    _applyBtn = "//input[@value='Apply']"
    _coupon_invalid = "//*[@id='addPromo_BadCode']"
    _wait_for_order_page = "//div[contains(text(),'Review your order')]"

    def enterCouponCode(self,coupon):
        self.waitForElement(self._wait_for_order_page,"xpath",10,0.5)
        self.sendKeys(self._coupon_code_apply,"id",coupon)

    def applyCouponCode(self):
        self.elementClick(self._applyBtn,"xpath")
        self.waitForElement(self._coupon_invalid,"xpath",5,0.5)

    def getMessageForInvalidCoupon(self):
         return self.getElement(self._coupon_invalid,"xpath").text



