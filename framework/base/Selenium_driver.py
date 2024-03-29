from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from framework.utilties.custom_logger import customLogger
import logging
from selenium.webdriver.common.action_chains import ActionChains
import os.path


class SeleniumDriver():

    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getName(self,name):
        global method_name
        method_name = name

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def scroll_to_element(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            y = element.location.get('y')
            #print(y)
            #The below line of code will scroll to the bottom of the page
            #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.execute_script("window.scrollTo(0,"+y+")")
            self.log.info("Scrolled to element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot scroll to the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def ElementMouseOver(self,locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            self.log.info("Mouse Overed on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot mouse over to the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()


    def screenshot(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        screenshot_path = os.path.join(my_path,"../Screenshots/"+method_name)
        self.driver.get_screenshot_as_file(screenshot_path+".png")



   
