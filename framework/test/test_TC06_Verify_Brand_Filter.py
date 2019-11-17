from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.PDP_Page import PDP_Page
from framework.pom.CartPage import CartPage
import time

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_BrandFilter(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)


    @pytest.mark.run(order=1)
    def test_verify_brand(self):
        self.hp.search_product("power bank")
        brands = self.plp.filter_verify_brand_name()
        print(brands)
        brand_name = self.plp.get_brand_name()
        #print(bname)
        for brand in brands:
            assert brand_name == brand,"Brand does not match"
            print("Brand filter validated")