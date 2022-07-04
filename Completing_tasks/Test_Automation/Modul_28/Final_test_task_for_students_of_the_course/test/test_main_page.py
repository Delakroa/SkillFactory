# pytest -v --tb=line --language=en test_main_page.py
# pytest -v -m login_guest --tb=line --language=en test_main_page.py

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/'
login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_can_see_login_url(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_url()


def test_guest_can_see_login_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_form()


def test_guest_can_see_register_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_cant_see_product_in_basket_opened_from_main_page()


def test_guest_can_message_that_the_basket_is_empty(browser):
    page = BasketPage(browser, link)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_can_message_that_the_basket_is_empty()
