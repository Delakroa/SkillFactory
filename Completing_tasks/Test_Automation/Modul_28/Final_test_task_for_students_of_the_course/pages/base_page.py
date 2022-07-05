#!/usr/bin/python3
# -*- encoding=utf8 -*-

import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    """Базовый класс страницы"""

    def __init__(self, browser, url, timeout=10):
        """Инициализация атрибутов класса"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def should_be_authorized_user(self):
        """Проверка на авторизацию пользователя"""
        assert self.is_element_present(*BasePageLocators.USER_ICON)

    def go_to_login_page(self):
        """Страница авторизации"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """Проверка ссылки для входа"""
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), 'Ссылка для входа не представлена'

    def guest_can_go_to_basket_page(self):
        """Корзина для гостя"""
        basket_button = self.browser.find_element(
            *BasePageLocators.BUSKET_BUTTON).click()
        basket_button.click()

    def is_element_present(self, how, what):
        """Элемент присутствует"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Элемент отсутствует"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """Пропал"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def open(self):
        """Открыть страницу"""
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        """Пройти опрос и получить код"""
        alert = self.browser.switch_to.alert
        value_x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(value_x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Ваш код: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('Второе оповещение не представлено')
