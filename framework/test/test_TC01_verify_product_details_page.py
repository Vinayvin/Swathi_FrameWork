from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.PDP_Page import PDP_Page

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_StockAvailabilty(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)
        self.pdp = PDP_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_stock_availability(self):
        self.hp.select_category("Beauty")
        self.plp.select_product()
        assert "InStock" in self.pdp.verifystock(), "Product not available"
        print("Product in stock")



