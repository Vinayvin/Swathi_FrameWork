from framework.base.Selenium_driver import SeleniumDriver

class PDP_Page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _stock = "//div[@id='dp-container']/div[@id='actionPanelContainer']/div[@id='actionPanelWrapper']" \
            "/div[@id='actionPanel']/div[@class='a-row'][1]/div[@id='availability_feature_div']" \
            "/div[@id='availability-brief']/span[@id='availability']"

    _add_to_cartBtn = "add-to-cart-button"


    """ Method which is used to verify whether product is in stck or out of stock"""
    def verifystock(self):
        self.waitForElement(self._stock,"xpath",20,0.5)
        check_availabilty=self.getElement(self._stock,"xpath").text

        stock_text=check_availabilty.replace(" ","")
        print(stock_text)
        return stock_text

    """Method to Add the product to Cart"""
    def clickAddToCart(self):
        self.waitForElement(self._add_to_cartBtn,"5",0.5)
        self.elementClick(self._add_to_cartBtn,"id")