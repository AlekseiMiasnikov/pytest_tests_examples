from allure import title, description, suite, parent_suite

from data import API_USERS_SUCCESS, DATA_TIMEZONE_RANDOM, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TINEZONE, AUTH_DATA_FAIL_BAD_ID, \
    API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_TIMEZONE_EMPTY, \
    API_NOT_FOUND_TIMEZONE, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Time. Метод: get-timezone')
@parent_suite('[PYTHON][API]')
class TestApiTimeGetTimezone:
    @title('get-timezone')
    @description('Проверка корректной работы get-timezone')
    def test_get_timezone(self, create_admin, time):
        asserts(
            assert_data=time.get_timezone({
                'token': create_admin['token'],
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': create_admin['id']
            }),
            data=API_USERS_SUCCESS
        )

    @title('get-timezone-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-timezone')
    def test_get_timezone_method_not_allowed(self, time):
        asserts(
            assert_data=time.get_timezone_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-timezone-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-timezone')
    def test_get_timezone_bad_request_empty_token(self, time):
        asserts(
            assert_data=time.get_timezone({
                'token': '',
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-timezone-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-timezone')
    def test_get_timezone_bad_request_length_token(self, time):
        asserts(
            assert_data=time.get_timezone({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-timezone-fail-bad-request-length-timezone')
    @description('Проверка ошибки Bad Request length timezone для get-timezone')
    def test_get_timezone_bad_request_length_timezone(self, time, create_admin):
        asserts(
            assert_data=time.get_timezone({
                'token': create_admin['token'],
                'timezone_name': AUTH_DATA_LENGTH_TOKEN,
                'user_id': create_admin['id']
            }),
            data=API_BAD_REQUEST_LENGTH_TINEZONE
        )

    @title('get-timezone-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id для get-timezone с отрицательным числом в идентификаторе пользователя')
    def test_get_timezone_bad_request_user_id_minus(self, time):
        asserts(
            assert_data=time.get_timezone({
                'token': 1,
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-timezone-fail-bad-request-user-id-varchar')
    @description(
        'Проверка ошибки Bad Request user id для get-timezone с символами в идентификаторе пользователя')
    def test_get_timezone_bad_request_user_id_varchar(self, time):
        asserts(
            assert_data=time.get_timezone({
                'token': 1,
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-timezone-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-timezone')
    def test_get_timezone_not_found_empty_token(self, time):
        asserts(
            assert_data=time.get_timezone({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-timezone-fail-bad-request-empty-timezone')
    @description('Проверка ошибки Bad Request empty timezone для get-timezone')
    def test_get_timezone_bad_request_empty_timezone(self, time, create_admin):
        asserts(
            assert_data=time.get_timezone({
                'token': create_admin['token'],
                'timezone_name': '',
                'user_id': create_admin['id']
            }),
            data=API_TIMEZONE_EMPTY
        )

    @title('get-timezone-fail-not-found-timezone')
    @description('Проверка ошибки Not Found timezone для get-timezone')
    def test_get_timezone_not_found_timezone(self, time, create_admin):
        asserts(
            assert_data=time.get_timezone({
                'token': create_admin['token'],
                'timezone_name': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_admin['id']
            }),
            data=API_NOT_FOUND_TIMEZONE
        )

    @title('get-timezone-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-timezone')
    def test_get_timezone_bad_request_bad_rights(self, create_login_delete_user, time):
        asserts(
            assert_data=time.get_timezone({
                'token': create_login_delete_user['token'],
                'timezone_name': DATA_TIMEZONE_RANDOM['timezone_name'],
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
