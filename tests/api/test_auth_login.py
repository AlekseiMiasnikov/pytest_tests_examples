from allure import title, suite, parent_suite
from pages.api import asserts
from data import API_AUTH_LOGIN_POST, API_POST_METHOD_NOT_ALLOWED, API_AUTH_BAD_REQUEST, \
    API_AUTH_BAD_REQUEST_LENGTH_LOGIN, API_AUTH_BAD_REQUEST_LENGTH_PASSWORD, API_AUTH_NOT_FOUND_USER, \
    API_AUTH_BAD_REQUEST_LOGIN_PASSWORD_ERROR, AUTH_DATA_ADMIN, AUTH_DATA_FAIL_LENGTH_LOGIN_ADMIN, \
    AUTH_DATA_FAIL_LENGTH_PASSWORD_ADMIN, AUTH_DATA_FAIL_LOGIN_PASSWORD_ERROR, AUTH_DATA_FAIL_BAD_TOKEN


@suite('Контроллер: Auth. Метод: login')
@parent_suite('[PYTHON][API]')
class TestApiAuthLogin:
    @title('Проверка успешной авторизации')
    def test_auth_login(self, auth_login):
        response = auth_login.login(AUTH_DATA_ADMIN)
        asserts(assert_data=response, data=API_AUTH_LOGIN_POST)
        assert 'token' in response['data']

    @title('Проверка авторизации с использованием запрещенного HTTP метода')
    def test_auth_login_not_allowed(self, auth_login):
        asserts(
            assert_data=auth_login.login_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('Проверка авторизации с пустым логином')
    def test_auth_login_bad_request_empty_fields_login(self, auth_login):
        asserts(
            assert_data=auth_login.login(data={
                'login': '',
                'password': 'admin'
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('Проверка авторизации с пустым паролем')
    def test_auth_login_bad_request_empty_fields_password(self, auth_login):
        asserts(
            assert_data=auth_login.login(data={
                'login': 'admin',
                'password': ''
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('Проверка авторизации с пустым логином и паролем')
    def test_auth_login_bad_request_empty_fields_all(self, auth_login):
        asserts(
            assert_data=auth_login.login(data={
                'login': '',
                'password': ''
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('Проверка авторизации с логином длинной более 100 символов')
    def test_auth_login_bad_request_length_login(self, auth_login):
        asserts(
            assert_data=auth_login.login(AUTH_DATA_FAIL_LENGTH_LOGIN_ADMIN),
            data=API_AUTH_BAD_REQUEST_LENGTH_LOGIN
        )

    @title('Проверка авторизации с паролем длинной более 100 символов')
    def test_auth_login_bad_request_length_password(self, auth_login):
        asserts(
            assert_data=auth_login.login(AUTH_DATA_FAIL_LENGTH_PASSWORD_ADMIN),
            data=API_AUTH_BAD_REQUEST_LENGTH_PASSWORD
        )

    @title('Проверка авторизации с неверными данными')
    def test_auth_login_not_found_user(self, auth_login):
        asserts(
            assert_data=auth_login.login(data={
                'login': AUTH_DATA_FAIL_BAD_TOKEN,
                'password': AUTH_DATA_FAIL_BAD_TOKEN
            }),
            data=API_AUTH_NOT_FOUND_USER
        )

    @title('Проверка авторизации с не верным паролем')
    def test_auth_login_bad_request_login_password_error(self, auth_login):
        asserts(
            assert_data=auth_login.login(AUTH_DATA_FAIL_LOGIN_PASSWORD_ERROR),
            data=API_AUTH_BAD_REQUEST_LOGIN_PASSWORD_ERROR
        )
