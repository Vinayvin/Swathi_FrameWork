from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
import time

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_PageNavigation(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)

    @pytest.mark.run(order=1)
    def test_nextpage_option(self):
        self.hp.select_category("Automotive")
        self.plp.select_subshopByCategory()
        page_num_before=self.plp.get_current_page_number()
        time.sleep(2)
        print(page_num_before)
        self.plp.goToNextPage()
        time.sleep(5)
        page_num_after = self.plp.get_current_page_number()
        print(page_num_after)
        time.sleep(5)
        assert page_num_after == str(int(page_num_before) + 1),"Page is not navigated to next page"
        print("Page Navigation is working")
