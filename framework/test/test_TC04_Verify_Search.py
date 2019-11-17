from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
import json

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_SearchBox(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_searchField(self):
        # prod_name = json.loads(open("ReadProductName.json").read())
        # pname = prod_name["product_name"]
        pname = self.hp.getDataFromJsonFile("ReadProductName.json","product_name")
        self.hp.search_product(pname)
        actual_prod_text=self.plp.check_search_box()
        assert pname in actual_prod_text,"Search not working"
        print("Search box passed")


