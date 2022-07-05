from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterNewUsersLocators


class LoginPage(BasePage):
    """Класс страница авторизации"""
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """URL для входа"""
        page_url_login = self.browser.current_url
        assert 'login' in page_url_login, 'Нет страницы для входа'

    def should_be_login_form(self):
        """Форма для входа"""
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, '"login_form" не отображается на странице.'

    def should_be_register_form(self):
        """Форма регистрации"""
        login_register = self.is_element_present(*LoginPageLocators.LOGIN_REGISTER)
        assert login_register, '"login_register" не отображается на странице.'

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        input_email = self.browser.find_element(*RegisterNewUsersLocators.EMAIL_REGISTRATION)
        input_email.send_keys(email)

        input_password = self.browser.find_element(*RegisterNewUsersLocators.PASSWORD_REGISTRATION)
        input_password.send_keys(password)

        input_password_confirm = self.browser.find_element(*RegisterNewUsersLocators.PASSWORD_REGISTRATION_CONFIRM)
        input_password_confirm.send_keys(password)

        button_register = self.browser.find_element(*RegisterNewUsersLocators.BUTTON_REGISTER)
        button_register.click()
