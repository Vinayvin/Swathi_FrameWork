from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp","loginSetup")
class Test_SearchBox(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp,loginSetup):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)


    @pytest.mark.usefixtures("searchProd")
    def test_verifySearch(self):
        SeleniumDriver(self.driver).getName(self.__class__.__name__)
        print("Validating Search")




