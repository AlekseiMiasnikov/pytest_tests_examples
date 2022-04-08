from selene import have
from allure import step
from selenium.webdriver.common.keys import Keys

from components.selectors import LOGIN, PASSWORD, AUTH_LOGIN_SYSTEM
from pages.BasePage import BasePage


class LoginPage(BasePage):
    @step('Заполнение формы авторизации')
    def field_inputs(self, fields):
        self.element(LOGIN).send_keys(fields['login'])
        self.element(PASSWORD).send_keys(fields['password']).send_keys(Keys.ENTER)

    @step('Проверка авторизованного пользователя - {login}')
    def check_login_user(self, login):
        self.element(AUTH_LOGIN_SYSTEM).should(have.text(login))
