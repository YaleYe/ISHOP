# /Users/yaleye/Documents/GitHub/YihongYe/TestingFile
from selenium import webdriver
import unittest
from django.contrib.auth.models import User
from core.models import Product, Profile, Address, orderItem, Order
from django.test import RequestFactory, TestCase
from django.core.files.storage import FileSystemStorage
import os

# mac chromedriver path
path = "../chromedriver"


# win chromedriver path
# path = "../winchromedriver.exe"

class modelTest(unittest.TestCase):

    def setUp(self) -> None:
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.filter(username="test")[0]
        self.profileInstance = Profile.objects.filter(user=self.user)[0]
        self.addressInstance = Address.objects.filter(user=self.user)[0]
        self.productInstance = Product.objects.filter(title="test")[0]
        self.orderItemInstance = orderItem.objects.filter(buyer=self.user)[0]

    def test_user_model_testing(self):
        assert self.user.username == "test"
        print("user model testing passed")

    def test_address_model_testing(self):
        assert self.addressInstance.address == "test"
        assert self.addressInstance.address2 == "test"
        assert self.addressInstance.state == "PA"
        assert self.addressInstance.city == "test"
        assert self.addressInstance.country == "US"
        assert self.addressInstance.zip == 404
        print("address model testing passed")

    def test_profile_model_testing(self):
        assert self.profileInstance.bio == "test"
        assert self.profileInstance.phone == "404"
        assert self.profileInstance.email == "test@test.com"
        print("profile model testing passed")

    def test_product_model_testing(self):
        assert self.productInstance.title == "test"
        assert self.productInstance.price == 1.0
        assert self.productInstance.description == "test"
        assert self.productInstance.stocking == 1
        assert self.productInstance.coupon == 1.0
        assert self.productInstance.seller == self.user
        assert self.productInstance.category == "Fresh"
        print("product model testing passed")

    def test_orderItem_model_testing(self):
        assert self.orderItemInstance.quantity == 1
        assert self.orderItemInstance.buyer == self.user
        print("orderItem model testing passed")



if __name__ == "__main__":
    unittest.main()
