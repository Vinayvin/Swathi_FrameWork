from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.PDP_Page import PDP_Page
from framework.pom.CartPage import CartPage
import time

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_CartRemoveItem(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)
        self.pdp = PDP_Page(self.driver)
        self.cartpage = CartPage(self.driver)

    @pytest.mark.run(order=1)
    def test_cart_removeitem_priceupdate(self):
        self.hp.search_product("bangles")
        self.plp.select_product()
        self.pdp.clickAddToCart()

        self.hp.select_category()
        self.plp.select_product()
        self.pdp.clickAddToCart()

        self.hp.click_cart_icon()
        totalprice_before = self.cartpage.get_subtotal()
        print(totalprice_before)

        remove_price=self.cartpage.get_remove_prod_price()

        self.cartpage.remove_product()
        time.sleep(2)
        totalprice_after = self.cartpage.get_subtotal()
        print(totalprice_after)

        result_price = str(float(totalprice_before) - float(remove_price))

        assert totalprice_after in result_price,"Subtotal price not updated"
        print("Subtotal price is updated after removing the product from the cart")



