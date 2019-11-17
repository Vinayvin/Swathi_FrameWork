from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.PDP_Page import PDP_Page
import time

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_CartItemCount(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)
        self.pdp = PDP_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_cart_ItemCount(self):
        self.hp.search_product("bags")
        self.plp.select_product()
        self.pdp.clickAddToCart()

        cartcount1 = int(self.hp.get_cart_count())
        print("BeforeCount:",cartcount1)

        self.hp.select_category()
        self.plp.select_product()
        self.pdp.clickAddToCart()

        #time.sleep(2)

        cartcount2 = int(self.hp.get_cart_count())
        print("AfterCount:",cartcount2)

        cartcount1=cartcount1+ 1

        assert cartcount2==cartcount1,"Cart count not incrementing"
        print("Cart Count incremented by one")
