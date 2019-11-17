from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class CartPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    #_cartBtn = "hlb-view-cart-announce"
    _subtotal_price = "(//span[@class='a-size-medium a-text-bold'])[1]/span[2]"
    _delete_prod = "(//span[@class='a-size-small sc-action-delete'])[1]"
    _removed_prod_price = "//div[@class='sc-list-item-content']/div/div[@class='a-column a-span2 a-text-left']/p/span"
    _quantity = "quantity"
    _all_prod_prices = "//p[@class='a-spacing-small']/span"
    _proceed_to_checkout = "proceedToCheckout"



    # def checkcartBtnPresent(self):
    #     cartele = self.elementPresenceCheck(self._cartBtn,"id")
    #     return cartele
    """" Method to get the subtotal amount in Cart Page"""
    def get_subtotal(self):
        self.waitForElement(self._subtotal_price,3,0.5)
        price=self.getElement(self._subtotal_price,"xpath").text
        return price[1:].replace("$",'')

    """" This method used to remove the product from the cart"""
    def remove_product(self):
        self.elementClick(self._delete_prod,"xpath")

    """Method to get the price of the removed product"""
    def get_remove_prod_price(self):
        price = self.getElement(self._removed_prod_price,"xpath").text
        return price.replace(" ","").replace("$",'')

    """Method to change the quantity of the product in Cart Page"""
    def change_Quantity(self,qty):
        sel = Select(self.getElement(self._quantity,"name"))
        sel.select_by_value(qty)

    """Method to get each product price present in cart page"""
    def get_prod_price(self):
        prices = self.driver.find_elements_by_xpath(self._all_prod_prices)
        allprices=[]
        for price in prices:
            allprices.append(float((price.text).replace('$',"")))
        return allprices

    def clickProceedToCheckOut(self):
        self.elementClick(self._proceed_to_checkout,"name")








