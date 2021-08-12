# /Users/yaleye/Documents/GitHub/YihongYe/TestingFile
from selenium import webdriver
import unittest

# requires login with username 1 and password 1

# mac chromedriver path
from selenium.webdriver.common.by import By

path = "../chromedriver"


class test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)

    def test_signuptestingAccountExisted(self):
        """
            stimulation to enter username and password exist

            Args:
                self
        """
        self.driver.get("http://127.0.0.1:8000/signup")
        # input username into testing
        usernameInput = self.driver.find_element_by_id("userName")
        usernameInput.send_keys("1")

        # input password into testing
        passwordInput = self.driver.find_element_by_id("password")
        passwordInput.send_keys("1")

        # input password into testing
        repasswordInput = self.driver.find_element_by_id("repassword")
        repasswordInput.send_keys("1")

        button = self.driver.find_element_by_id("submit")
        button.click()
        # if found "Account Error: Account has been registered" error: test passed
        assert "Account Error: Account has been registered" in self.driver.page_source
        print("test_signuptestingAccountExisted passed")

    def test_signuptestingUnmatchingPassword(self):
        """
            stimulate to enter username and password exist

            Args:
                self
        """
        self.driver.get("http://127.0.0.1:8000/signup")
        # input username into testing
        usernameInput = self.driver.find_element_by_id("userName")
        usernameInput.send_keys("1")

        # input password into testing
        passwordInput = self.driver.find_element_by_id("password")
        passwordInput.send_keys("1")

        # input password into testing
        repasswordInput = self.driver.find_element_by_id("repassword")
        repasswordInput.send_keys("123")

        button = self.driver.find_element_by_id("submit")
        button.click()
        # if found "Account Error: Account has been registered" error: test passed
        assert "password dont match" in self.driver.page_source
        print("test password dont match passed")

    def test_signinNoMatching(self):
        """
            stimulate to enter username and password matches

            Args:
                self: driver
        """
        self.driver.get("http://127.0.0.1:8000/signin")
        # input username into testing
        usernameInput = self.driver.find_element_by_id("username")
        usernameInput.send_keys("1")

        # input password into testing
        passwordInput = self.driver.find_element_by_id("password")
        passwordInput.send_keys("123")

        button = self.driver.find_element_by_id("submit")
        button.click()
        print("test test_signin NoMatching passed")

    def signin(self):
        self.driver.get("http://127.0.0.1:8000/signin")
        # input username into testing
        usernameInput = self.driver.find_element_by_id("username")
        usernameInput.send_keys("1")

        # input password into testing
        passwordInput = self.driver.find_element_by_id("password")
        passwordInput.send_keys("1")

        button = self.driver.find_element_by_id("submit")
        button.click()
        print("user signed in")

    def test_home(self):
        """
            stimulate to check if items are displayed correctly on home

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/")

        # if found product info, description and price
        assert "Product Info:" in self.driver.page_source
        assert "Product Description:" in self.driver.page_source
        assert "Product Price:" in self.driver.page_source
        print("test test_home passed")

    def test_myProduct(self):
        """
            stimulate to check if my product is displayed correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/myProduct/")
        assert "apple" in self.driver.page_source
        print("test myProduct passed")

    def test_UI_buyerPage_home(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/")
        assert "apple" in self.driver.page_source
        assert "arcade" in self.driver.page_source
        assert "bagel" in self.driver.page_source
        assert "belt" in self.driver.page_source
        assert "boba" in self.driver.page_source
        assert "burger" in self.driver.page_source
        assert "chicken" in self.driver.page_source
        assert "Tesla" in self.driver.page_source
        print("test UI buyerPage home passed")

    def test_UI_buyerPage_fresh(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/fresh/")
        assert "apple" in self.driver.page_source
        assert "chicken" in self.driver.page_source
        assert "egg" in self.driver.page_source
        assert "mushroom" in self.driver.page_source
        assert "steak" in self.driver.page_source
        print("test UI buyerPage fresh passed")

    def test_UI_buyerPage_beverage(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/beverage/")
        assert "boba" in self.driver.page_source
        assert "coca-cola" in self.driver.page_source
        assert "milk" in self.driver.page_source
        assert "pepsi" in self.driver.page_source
        print("test UI buyerPage beverage passed")

    def test_UI_buyerPage_bakery(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/bakery/")
        assert "bagel" in self.driver.page_source
        assert "burger" in self.driver.page_source
        assert "donut" in self.driver.page_source
        assert "tiramisu" in self.driver.page_source
        assert "waffle" in self.driver.page_source
        print("test UI buyerPage bakery passed")

    def test_UI_buyerPage_supplement(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/supplement/")
        assert "fishoil" in self.driver.page_source
        assert "vitamin" in self.driver.page_source
        print("test UI buyerPage supplement passed")

    def test_UI_buyerPage_shirt(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/shirt/")
        assert "shirt" in self.driver.page_source
        print("test UI buyerPage shirt passed")

    def test_UI_buyerPage_dress(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/dress/")
        assert "socks" in self.driver.page_source
        print("test UI buyerPage dress passed")

    def test_UI_buyerPage_pants(self):
        """
            stimulate to check if all product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/pants/")
        assert "pants" in self.driver.page_source
        print("test UI buyerPage pants passed")

    def test_UI_buyerPage_shoes(self):
        """
            stimulate to check if all shoes product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/shoes/")
        assert "shoes" in self.driver.page_source
        print("test UI buyerPage shoes passed")

    def test_UI_buyerPage_socks(self):
        """
            stimulate to check if all socks product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/socks/")
        assert "cozy socks" in self.driver.page_source
        print("test UI buyerPage socks passed")

    def test_UI_buyerPage_underwear(self):
        """
            stimulate to check if all underwear product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/underwear/")
        print("test UI buyerPage underwear passed")

    def test_UI_buyerPage_watches(self):
        """
            stimulate to check if all watches product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/socks/")
        assert "watch" in self.driver.page_source
        print("test UI buyerPage socks passed")

    def test_UI_buyerPage_vroom(self):
        """
            stimulate to check if all vroom product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/vroom/")
        assert "Tesla" in self.driver.page_source
        print("test UI buyerPage vroom passed")

    def test_UI_buyerPage_camera(self):
        """
            stimulate to check if all camera product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/Camera/")
        assert "Canon" in self.driver.page_source
        print("test UI buyerPage vroom passed")

    def test_UI_buyerPage_gameConsole(self):
        """
            stimulate to check if all game console product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/GameConsole/")
        assert "arcade" in self.driver.page_source
        assert "lego" in self.driver.page_source
        assert "ps5" in self.driver.page_source
        assert "stadia" in self.driver.page_source
        assert "xbox" in self.driver.page_source
        print("test UI buyerPage vroom passed")

    def test_UI_sellerPage(self):
        """
            stimulate to check if all seller product be displayed

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/myProduct/")
        assert "apple" in self.driver.page_source
        assert "fishoil" in self.driver.page_source
        assert "lego" in self.driver.page_source
        assert "milk" in self.driver.page_source
        assert "mushroom" in self.driver.page_source
        assert "pants" in self.driver.page_source
        assert "pepsi" in self.driver.page_source
        assert "ps5" in self.driver.page_source
        assert "shirt" in self.driver.page_source
        assert "shoes" in self.driver.page_source
        assert "stadia" in self.driver.page_source
        assert "steak" in self.driver.page_source
        assert "tiddybear" in self.driver.page_source
        assert "tiramisu" in self.driver.page_source
        assert "vitamin" in self.driver.page_source
        print("test UI buyerPage vroom passed")

    def test_uploadProduct(self):
        """
            stimulate to see if upload product is displayed correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/uploadProduct/")
        assert "Upload Your Product Info" in self.driver.page_source
        assert "Additional Info" in self.driver.page_source
        assert "Upload your product image" in self.driver.page_source
        print("test uploadProduct passed")

    def test_profile(self):
        """
            stimulate to check if profile is displayed correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/profile/")
        assert "usernameID: 37ce71d2-bd68-4376-9f5d-db7e091e58fa" in self.driver.page_source
        assert "username: 1" in self.driver.page_source
        assert "1@1.com" in self.driver.page_source
        assert "111111111" in self.driver.page_source
        assert "111" in self.driver.page_source
        assert "apt 1" in self.driver.page_source
        assert "PITTSBURGH" in self.driver.page_source
        assert "OH" in self.driver.page_source
        assert "US" in self.driver.page_source
        assert "11111" in self.driver.page_source
        assert "hi,this is 1" in self.driver.page_source

        print("test profile Page passed")

    def test_cart(self):
        """
            stimulate to if cart is displayed correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/cart/")
        assert "Item" in self.driver.page_source
        assert "Price" in self.driver.page_source
        assert "Quantity" in self.driver.page_source
        assert "Subtotal" in self.driver.page_source
        print("test cart passed")

    def test_checkout(self):
        """
            stimulate to if check out will save the order information to the previous order
            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/checkout/")
        assert "Thank You!" in self.driver.page_source
        assert "Your order number is" in self.driver.page_source
        confirmation = self.driver.find_element_by_tag_name('span')
        print(confirmation)
        id = confirmation.text
        self.driver.get("http://127.0.0.1:8000/previousOrder/")
        assert id in self.driver.page_source
        print("test checkout Page passed")

    def test_upload_review(self):
        """
            stimulate to if beast mode display correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/uploadproductreview/")
        assert "Select your product" in self.driver.page_source
        assert "Write" in self.driver.page_source
        assert "Rate" in self.driver.page_source
        assert "arcade" in self.driver.page_source
        print("test upload review passed")

    def test_my_product_review(self):
        """
            stimulate to check if myProduct Review displayed correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/myproductreview/")
        assert "Here is review about your product:" in self.driver.page_source
        assert "apple : ok 3" in self.driver.page_source
        assert "apple : ads 2" in self.driver.page_source
        assert "milk : mily 3" in self.driver.page_source
        assert "milk : milke is good 5" in self.driver.page_source
        assert "cozy socks : das 5" in self.driver.page_source
        print("test my product review passed")

    def test_my_review(self):
        """
            stimulate to check if myProduct Review displayed correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/myreview/")
        assert "123" in self.driver.page_source
        assert "very nice guy" in self.driver.page_source
        print("test my review page passed")

    def test_BeastMode(self):
        """
            stimulate to if beast mode display correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/beastmode/")
        assert "Add to Cart" in self.driver.page_source
        print("Test Beast Mode passed")

    def test_sellerReview(self):
        """
            stimulate to add review to the seller

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/uploadUserReview/")
        assert "Select the User" in self.driver.page_source
        assert "Write your most honest review" in self.driver.page_source
        assert "Rate" in self.driver.page_source
        print("test seller review passed")

    def test_updateProduct(self):
        """
            stimulate to check if update product page display correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/selectProduct/")
        assert "Select the Product" in self.driver.page_source
        assert "apple" in self.driver.page_source
        assert "select" in self.driver.page_source
        print("test updateProduct page passed")

    def test_removeProduct(self):
        """
            stimulate to check if delete product page display correctly

            Args:
                self: driver
        """
        self.signin()
        self.driver.get("http://127.0.0.1:8000/removeProduct/")
        assert "Select the Product" in self.driver.page_source
        assert "apple" in self.driver.page_source
        assert "Remove" in self.driver.page_source
        print("test removeProduct page passed")

    def tearDown(self):
        """
            turn off the chrome driver for testing

            arg:
                self
        """
        self.driver.close()
        print("driver is closed")


if __name__ == "__main__":
    unittest.main()
