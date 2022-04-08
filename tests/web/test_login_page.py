from allure import suite, parent_suite, title

from data import AUTH_DATA_ADMIN


@suite('Авторизация')
@parent_suite('[PYTHON][UI]')
class TestLoginPage:
    @title('Проверка успешной авторизации в системе')
    def test_login(self, login_page):
        login_page.open()
        login_page.check_title('Авторизация')
        login_page.field_inputs({**AUTH_DATA_ADMIN})
        login_page.check_login_user(AUTH_DATA_ADMIN['login'])
