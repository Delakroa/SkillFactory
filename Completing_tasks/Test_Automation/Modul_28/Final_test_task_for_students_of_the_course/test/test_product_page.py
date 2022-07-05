# python -m pytest -v --driver Chrome --driver-path D:\Python library\SkillFactory\Completing_tasks\Test_Automation\
# Modul_28\Final_test_task_for_students_of_the_course\chromedriver.exe

import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
OFFER_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

offer_list = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]


@pytest.mark.login
class TestUser:
    """Тестовый пользователь добавляет в корзину со страницы товаров"""

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        """Авторизационные данные"""
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        self.register_page = LoginPage(browser, LOGIN_LINK)
        self.register_page.open()
        self.register_page.register_new_user(email, password, browser)
        self.register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """тестовый пользователь может добавить товар в корзину"""
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.guest_can_add_product_to_basket()
        product_page.product_name_in_the_message_compare_the_added_product()
        product_page.compare_the_price_of_the_product_with_the_added()


@pytest.mark.need_review
@pytest.mark.parametrize('number_offer', offer_list)
def test_guest_can_add_product_to_basket(browser, number_offer):
    """Тестовый гость может добавить товар в корзину"""
    offer_link_param = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_offer}'
    product_page = ProductPage(browser, offer_link_param)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_in_the_message_compare_the_added_product()
    product_page.compare_the_price_of_the_product_with_the_added()


@pytest.mark.xfail(reason='test should fall because guest can see success message after adding product to basket')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.i_cant_see_the_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.guest_cant_see_success_message()


@pytest.mark.xfail(reason='test should fall because success message is not disappeared')
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, OFFER_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = LoginPage(browser, OFFER_LINK)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, PRODUCT_LINK)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_cant_see_product_in_basket()


def test_guest_can_message_that_the_basket_is_empty(browser):
    page = BasketPage(browser, PRODUCT_LINK)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_can_message_that_the_basket_is_empty()
