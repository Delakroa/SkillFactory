# pytest -v test_product_page.py
# pytest -v --tb=line --language=en -m need_review

import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
offer_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

offer_list = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        self.register_page = LoginPage(browser, login_link)
        self.register_page.open()
        self.register_page.register_new_user(email, password, browser)
        self.register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.guest_can_add_product_to_basket()
        product_page.product_name_in_the_message_compare_the_added_product()
        product_page.product_price_in_the_basket_compare_the_added_product()


@pytest.mark.need_review
@pytest.mark.parametrize('number_offer', offer_list)
def test_guest_can_add_product_to_basket(browser, number_offer):
    offer_link_param = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_offer}'
    product_page = ProductPage(browser, offer_link_param)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_in_the_message_compare_the_added_product()
    product_page.product_price_in_the_basket_compare_the_added_product()


@pytest.mark.xfail(reason='test should fall because guest can see success message after adding product to basket')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_cant_see_success_message()


@pytest.mark.xfail(reason='test should fall because success message is not disappeared')
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, offer_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = LoginPage(browser, offer_link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, product_link)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_cant_see_product_in_basket_opened_from_main_page()


def test_guest_can_message_that_the_basket_is_empty(browser):
    page = BasketPage(browser, product_link)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_can_message_that_the_basket_is_empty()
