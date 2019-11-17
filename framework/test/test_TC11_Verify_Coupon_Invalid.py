from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.PDP_Page import PDP_Page
from framework.pom.CartPage import CartPage
from framework.pom.SignUpPage import SignUpPage
from framework.pom.DeliveryAddressPage import DeliveryAddressPage
from framework.pom.ShipmentPage import ShipmentPage
from framework.pom.PlaceOrderPage import PlaceOrderPage
from framework.pom.PaymentMethodPage import PaymentMethodPage

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ReviewFilter(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp = ProductListPage(self.driver)
        self.pdp = PDP_Page(self.driver)
        self.cartpage = CartPage(self.driver)
        self.sign_up = SignUpPage(self.driver)
        self.address = DeliveryAddressPage(self.driver)
        self.shipment = ShipmentPage(self.driver)
        self.payment = PaymentMethodPage(self.driver)
        self.order = PlaceOrderPage(self.driver)



    @pytest.mark.run(order=1)
    def test_verify_invalid_couponcode(self):
        self.hp.mouseOverOnSignIn()
        self.hp.toClickOnSignIn()
        self.sign_up.set_username(self.hp.getDataFromJsonFile("UserCredential.json", "username"))
        self.sign_up.set_password(self.hp.getDataFromJsonFile("UserCredential.json", "password"))
        self.sign_up.click_signIn()
        #self.hp.search_product(self.hp.getDataFromJsonFile("ReadProductName.json","b"))
        self.hp.select_category("Beauty")
        # self.plp.select_subshopByCategory()
        self.plp.select_product()
        self.pdp.clickAddToCart()
        self.hp.click_cart_icon()
        self.cartpage.clickProceedToCheckOut()
        self.sign_up.set_username(self.hp.getDataFromJsonFile("UserCredential.json","username"))
        self.sign_up.set_password(self.hp.getDataFromJsonFile("UserCredential.json","password"))
        self.sign_up.click_signIn()
        self.address.clickAddressBtn()
        self.shipment.clickContinueBtn()
        self.payment.clickToContinue()
        self.order.enterCouponCode("GETAPAY10")
        self.order.applyCouponCode()
        # msg = self.order.getMessageForInvalidCoupon()
        # print(msg)
        assert 'not valid' in self.order.getMessageForInvalidCoupon(),"Coupon code is valid Test case failed"
        print("Coupon invalid and it is not accepted,Test passed")
