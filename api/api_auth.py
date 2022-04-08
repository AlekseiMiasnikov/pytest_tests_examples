from api.api import API
from allure import step


class ApiAuth(API):
    @step('Авторизация')
    def login(self, data):
        return self.send_post(url='auth/login', data=data)

    @step('Авторизация с неверным методом')
    def login_method_not_allowed(self):
        return self.send_get(url='auth/login')

    @step('Выход из системы')
    def logout(self, data):
        return self.send_post(url='auth/logout', data=data)

    @step('Выход из системы с неверным методом')
    def logout_method_not_allowed(self):
        return self.send_get(url='auth/logout')
