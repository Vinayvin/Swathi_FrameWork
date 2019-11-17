from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.PDP_Page import PDP_Page
from framework.pom.CartPage import CartPage
import time

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_CartChangeQuantity(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)
        self.pdp = PDP_Page(self.driver)
        self.cartpage = CartPage(self.driver)

    @pytest.mark.run(order=1)
    def test_cart_changeqty_priceupdate(self):
        self.hp.search_product("bangles")
        self.plp.select_product()
        self.pdp.clickAddToCart()
        self.hp.click_cart_icon()

        subtotal1 = float(self.cartpage.get_subtotal())
        print("Subtotal price before qty update:",subtotal1)
        cartcount1 = self.hp.get_cart_count()
        print("Cart Count Before:",cartcount1)
        price = self.cartpage.get_prod_price()
        price_of_prod = price[0]

        self.cartpage.change_Quantity("2")
        time.sleep(3)
        subtotal2 = float(self.cartpage.get_subtotal())
        print("SubTotal price After quantity update:",subtotal2)
        cartcount2 = self.hp.get_cart_count()
        print("Cart Count After:",cartcount2)

        assert cartcount2 == str(int(cartcount1) + 1),"cart count not incremented"
        print("Cart count is incremented by one")

        assert subtotal2 == price_of_prod * 2,"Subtotal price not updated"
        print("Subtotal price in cart page is updated")





