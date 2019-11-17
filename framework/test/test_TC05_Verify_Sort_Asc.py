from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage


import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_CartItemCount(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)


    @pytest.mark.run(order=1)
    def test_sort_asc(self):
        self.hp.search_product("laptop")
        sortprices = self.plp.verify_sort_prod_in_asc()
        print("Prices after sort:",sortprices)
        #print("Price in asc:",self.ProdcutListPage.asc_prices)
        # for i,j in zip(sortprices,self.plp.asc_prices):
        #     assert  sortprices[i] == self.plp.asc_prices[j],"Prices are not sorted in ascending order"
        #     print("All prices sorted in ascending order")

