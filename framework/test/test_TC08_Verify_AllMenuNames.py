from framework.pom.HomePage import HomePage
import time

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_MenusInHomePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_All_Menu_Names(self):
        self.hp.mouseOverOnCategory()
        menunames = self.hp.get_all_menus()
        print(menunames)
        # for menu in menunames:
        #     assert menu in self.hp.all_menu_names,"Menus not matching as expected "
        # print("All menu names validated")
        for i in range(len(menunames)):
            assert self.hp.getDataFromFile("E:/Automation/Selenium_Automation1/framework/MenusList.txt") in menunames,"Menus not matching as expected"
            print("All menus are validated")