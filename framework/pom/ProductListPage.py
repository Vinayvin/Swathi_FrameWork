from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select
import time


class ProductListPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _shopby_category_in_automotive = "//div[@class='a-section acs_tile__content']"
    # _total_result_count = "//span[@id='s-result-count']"
    # _result_count_per_page = "//li[contains(@id,'result_')]"
    _wait_for_prod_title = "//div[@id='fst-hybrid-dynamic-h1']"
    _nextpage = "//span[text()='Next Page']"
    _scroll_till_ele = "sx-hms-title"
    _current_page_num = "//div[@id='pagn']/span[@class='pagnCur']"
    _firstproduct = "//h2"
    _sortby = "sort"
    _prod_name_text = "//a[@id='bcKwText']//span"
    _search_prod_text = "//span[@id='s-result-count']//span[@class='a-color-state a-text-bold']"
    _prod_price = "//div[@class='s-item-container']" \
                  "//div/div[@class='a-fixed-left-grid-inner']" \
                  "/div[2]/div[@class='a-row']/div[@class='a-column a-span7']" \
                  "/div[@class='a-row a-spacing-none']/a/span[@class='a-color-base sx-zero-spacing']" \
                  "//span[@class='sx-price-whole']"

    _wait_for_ele = "//div[@id='leftNavContainer']/h3[text()='Show results for']"
    _brand_filter = "//div[@class='a-checkbox s-ref-link-cursor a-spacing-none']" \
                    "//span[@class='a-label a-checkbox-label']/span[text()='RAVPower']"
    _brand_names = "//div[@class='a-row a-spacing-none']/span[2]"
    _avg_review = "//a[@class='a-link-normal s-ref-text-link']//span[text()='4 Stars & Up']"
    _prod_names_based_on_review = "//li[contains(@id,'result_')]" \
                                  "/div/div/div/div[2]/div[3]/div[2]/div[1]/span/span/a/i[1]/span"

    asc_prices = []
    bname=""


    """ This method is used to select the product in product list page"""
    def select_product(self):
        #self._firstproduct = self._firstproduct + "["+str(prod_num)+"]"
        self.waitForElement(self._firstproduct,"5",0.5)
        self.elementClick(self._firstproduct,"xpath")

    def select_subshopByCategory(self):
        self.elementClick(self._shopby_category_in_automotive,"xpath")

    """ Method which returns the searched product text"""
    def check_search_box(self):
        self.waitForElement(self._wait_for_ele,"xpath",10,0.5)
        return self.getElement(self._search_prod_text,"xpath").text

    """ Method to validate sort price by Low to High"""
    def verify_sort_prod_in_asc(self):
        sortOption = self.getElement(self._sortby,"id")
        sel = Select(sortOption)
        sel.select_by_value("price-asc-rank")
        self.waitForElement(self._wait_for_ele,"xpath",10,0.5)
        prices = self.driver.find_elements_by_xpath(self._prod_price)
        asc_prices = [int(p.text.replace(',','')) for p in prices]
        print("Asc prices:",asc_prices)
        sorted_prices = sorted(asc_prices)
        return sorted_prices

    """ Method which returns the brand name selected"""
    def get_brand_name(self):
        bname = self.getElement(self._brand_filter, "xpath").text
        return bname

    """ Method to verify brand filter"""
    def filter_verify_brand_name(self):
        self.elementClick(self._brand_filter,"xpath")
        self.waitForElement(self._wait_for_ele,"xpath",5,0.5)
        names = self.driver.find_elements_by_xpath(self._brand_names)
        brand_names=[i.text for i in names]
        return brand_names
      
    # def get_total_result_count(self):
    #     words = self.getElement(self._total_result_count,"xpath").text.split()
    #     count = 0
    #     for word in words:
    #         if word.isdigit():
    #             count = int(word)
    #     return count
    #
    # def get_result_count_each_page(self):
    #     self.waitForElement(self._wait_for_prod_title,"xpath",3,0.5)
    #     allItemsInOnePage = self.driver.find_elements_by_xpath(self._result_count_per_page)
    #     return len(allItemsInOnePage)

    def get_current_page_number(self):
        self.scroll_to_element(self._scroll_till_ele, "id")
        return self.getElement(self._current_page_num,"xpath").text

    def goToNextPage(self):
        if self.getElement(self._nextpage,"xpath").is_enabled():
            print("There is next page option to navigate to multipage result")
            self.waitForElement(self._nextpage,"xpath",3,0.5)
            self.elementClick(self._nextpage,"xpath")
        else:
            print("Not able to find option to navigate to next page")

    def filter_by_Customer_Review(self):
        self.elementClick(self._avg_review, "xpath")
        self.waitForElement(self._wait_for_ele, "xpath", 5, 0.5)

    def get_All_Filtered_Reviews(self):
        time.sleep(5)
        names = self.driver.find_elements_by_xpath(self._prod_names_based_on_review)
        reviews = []
        for name in names:
            reviews.append(name.text[:1])
            #prodnames.append(name.text)
            #print(name.text)
        return reviews










