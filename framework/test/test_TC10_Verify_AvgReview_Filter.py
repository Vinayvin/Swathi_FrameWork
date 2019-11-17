from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
import json

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ReviewFilter(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_avg_review_filter(self):
        self.hp.search_product(self.hp.getDataFromJsonFile("ReadProductName.json","Hp"))
        self.plp.filter_by_Customer_Review()
        review_stars = self.plp.get_All_Filtered_Reviews()
        print(review_stars)
        expected_review_stars =['4','4.1','4.2','4.3','4.4','4.4','4.5','4.6','4.7','4.8','4.9','5']
        for star in review_stars:
            assert star in expected_review_stars,"Products are not filtered by stars "
            print("Product displayed according to Avg review filtered")
