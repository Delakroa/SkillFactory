#!/usr/bin/python3
# -*- encoding=utf8 -*-

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Создание класса с корзиной"""
    def guest_go_basket_page(self):
        """Гостевая корзина"""
        self.guest_can_go_to_basket_page()
        self.guest_cant_see_product_in_basket()

    def guest_cant_see_product_in_basket(self):
        """Гость не видит товар в корзине, открытой с главной страницы"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'Корзина не пуста'

    def guest_can_message_that_the_basket_is_empty(self):
        """Гость может сообщить, что корзина пуста"""
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), 'Нет сообщения о том, что корзина пуста'
