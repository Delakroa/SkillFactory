from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):
        """Добавление товара гостем в корзину"""
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def product_name_in_the_message_compare_the_added_product(self):
        """Сравнение добавленного товара с сообщением"""
        product_name_in_the_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_THE_MESSAGE).text
        product_name_in_the_catalog = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_THE_CATALOG).text
        assert product_name_in_the_message == product_name_in_the_catalog, 'Название продукта в сообщении не'\
                                                                           'соответствует добавленному продукту'

    def compare_the_price_of_the_product_with_the_added(self):
        """Сравнить цену товара в корзине, с добавленным товаром"""
        product_price_in_the_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_THE_MESSAGE).text
        product_price_in_the_catalog = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_THE_CATALOG).text
        assert product_price_in_the_message == product_price_in_the_catalog, 'Цена продукта в сообщении '\
                                                                            'не соответствует дополнительному продукту '

    def i_cant_see_the_success_message(self):
        """Гость не может увидеть сообщение об успешном завершении после добавления товара в корзину"""
        self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented'

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented'

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message does not disappear'
