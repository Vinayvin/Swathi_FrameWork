from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import json

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _signin_mouse_over = "nav-link-accountList"
    _logout_mouse_over = "//a[@id='nav-link-accountList']/span[2]"


    _departments = "//a[@id='nav-link-shopall']//span[@class='nav-line-2']"
    _beauty_prod = "//div[@id='nav-flyout-shopAll']//span[text()='Beauty & Personal Care']"
    _automotive_prod = "//div[@id='nav-flyout-shopAll']//span[text()='Automotive']"
    _searchbox = "twotabsearchtextbox"
    _searchBtn = "//input[@type='submit' and @value='Go']"
    _cart_count = "nav-cart-count"
    _cart_icon = "nav-cart"
   # _allmenus = "//div[@class='fsdDeptBox']/h2 | //div[@class='fsdDeptBox']//a"
    _allmenus_in_dept = "//div[@id='nav-flyout-shopAll']//span"
    _signin_icon = "nav-link-accountList"
    _signin_btn = "//div[@id='nav-flyout-ya-signin']/a/span[text()='Sign in']"
    _logout = "//a[@id='nav-item-signout']/span[text()='Sign Out']"

    def goTologinPage(self):
        # actions =ActionChains(self.driver)
        # actions.move_to_element(self.getElement(self._signin_mouse_over,"id")).perform()
        self.ElementMouseOver(self._signin_mouse_over,"id")
        self.driver.implicitly_wait(5)
        self.elementClick(self._signin_btn, "xpath")
        return True

    def verifyLogin(self):
        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.getElement(self._logout_mouse_over, "xpath")).perform()
        self.ElementMouseOver(self._logout_mouse_over,"xpath")
        # wait = WebDriverWait(self.driver,5)
        # wait.until(expected_conditions.visibility_of_element_located())
        self.waitForElement(self._logout, "xpath", 5, 0.5)
        assert self.getElement(self._logout,"xpath"),"Login is not SuccessFull"


    def logout(self):
        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.getElement(self._logout_mouse_over, "xpath")).perform()
        self.ElementMouseOver(self._logout_mouse_over,"xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._logout, "xpath")
        return True

    def mouseOverOnSignIn(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.getElement(self._signin_icon,"id")).perform()

    def toClickOnSignIn(self):
        self.elementClick(self._signin_btn,"xpath")


    """  This method is used to mouse over on Departments Menu In Home Page """
    def mouseOverOnCategory(self):
        dept = self.getElement(self._departments, "xpath")
        action = ActionChains(self.driver)
        action.move_to_element(dept).perform()
        time.sleep(2)

    """ This method is used to select a category under Departments Menu """
    def select_category(self,prod):
        self.mouseOverOnCategory()
        if prod == 'Beauty':
            self.elementClick(self._beauty_prod,"xpath")
        elif prod == 'Automotive':
            self.elementClick(self._automotive_prod,"xpath")

    """ This method is used to enter the product into searchbox and search """
    def search_product(self,prod_name):
        self.sendKeys(prod_name,self._searchbox,"id")
        self.elementClick(self._searchBtn,"xpath")

    """ Method which returns the cart count """
    def get_cart_count(self):
        cart_num = self.getElement(self._cart_count,"id").text
        return cart_num

    """ Method used to click on the cart icon"""
    def click_cart_icon(self):
        self.elementClick(self._cart_icon,"id")

    """ Method which returns all the menus present under Departments menu"""
    def get_all_menus(self):
        menus = self.driver.find_elements_by_xpath(self._allmenus_in_dept)
        menuslist= []
        for menu in menus:
            menuslist.append(menu.text)
        return menuslist

    """ Method which returns the data from the file """
    def getDataFromFile(self,filepath):
        f=open(filepath,"r")
        return f.readline().replace("\n","")


    def getDataFromJsonFile(self,filepath,key):
        f=json.loads(open(filepath,"r").read())
        return f[key]







