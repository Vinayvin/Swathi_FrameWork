import pytest
from framework.base.Extended_Webdriver import Extended_Webdriver
from framework.pom.HomePage import HomePage
from framework.pom.SignUpPage import SignUpPage
from framework.pom.ProductListPage import ProductListPage
from framework.base.Selenium_driver import SeleniumDriver
import time
import json

@pytest.fixture()
def setUp(request):
    print("Running method level setUp")
    yield
    SW=SeleniumDriver(request.cls.driver)
    SW.screenshot()
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    EW = Extended_Webdriver(browser)
    driver = EW.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


@pytest.fixture(scope="class")
def loginSetup(request):
    hp = HomePage(request.cls.driver)
    hp.goTologinPage()
    sp = SignUpPage(request.cls.driver)
    sp.login("swathiambale@gmail.com","MithunaAmazon@123")
    yield
    hp.logout()
    print("Logout Successful")

@pytest.fixture(scope="function")
def searchProd(request):
    hp = HomePage(request.cls.driver)
    plp = ProductListPage(request.cls.driver)
    prodname = hp.getDataFromJsonFile("ReadProductName.json", "bang")
    hp.search_product(prodname)
    yield
    assert prodname in plp.check_search_box(), "Search not working"
    print("Searchbox validated")






