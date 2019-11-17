from framework.pom.HomePage import HomePage
import pytest
import unittest




@pytest.mark.usefixtures("oneTimeSetUp","setUp","loginSetup")
class Test_login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp,loginSetup):
        self.hp = HomePage(self.driver)
        print("Logging in")

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.hp.verifyLogin()


