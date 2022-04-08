from allure import title, description, suite, parent_suite
from data import API_AUTH_LOGOUT_POST, API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN
from pages.api import asserts


@suite('Контроллер: Auth. Метод: logout')
@parent_suite('[PYTHON][API]')
class TestApiAuthLogout:
    @title('auth-logout')
    @description('Проверка корректной работы auth-logout')
    def test_auth_logout(self, auth_login, create_admin):
        asserts(
            assert_data=auth_login.logout({
                'token': create_admin['token'],
                'user_id': create_admin['id']
            }),
            data=API_AUTH_LOGOUT_POST
        )

    @title('auth-logout-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для auth-logout')
    def test_auth_logout_not_allowed(self, auth_login):
        asserts(
            assert_data=auth_login.logout_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('auth-logout-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Requst empty token для auth-logout')
    def test_auth_logout_bad_request_empty_token(self, auth_login):
        asserts(
            assert_data=auth_login.logout({'token': ''}),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('auth-logout-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Requst length token для auth-logout')
    def test_auth_logout_bad_request_length_token(self, auth_login):
        asserts(
            assert_data=auth_login.logout({'token': AUTH_DATA_LENGTH_TOKEN}),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('auth-logout-fail-not-found-token')
    @description('Проверка ошибки Not Found token для auth-logout')
    def test_auth_logout_not_found_token(self, auth_login):
        asserts(
            assert_data=auth_login.logout({'token': AUTH_DATA_FAIL_BAD_TOKEN}),
            data=API_AUTH_NOT_FOUND_TOKEN
        )
