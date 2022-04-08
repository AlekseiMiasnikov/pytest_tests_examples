from allure import title, description, suite, parent_suite

from data import API_SET_TIMEZONE_SUCCESS, DATA_TIMEZONE_RANDOM_NUM, API_POST_METHOD_NOT_ALLOWED, \
    API_AUTH_TOKEN_EMPTY, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, \
    API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_BAD_TIMEZONE_ID, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Time. Метод: set-timezone')
@parent_suite('[PYTHON][API]')
class TestApiTimeSetTimezone:
    @title('set-timezone')
    @description('Проверка корректной работы set-timezone')
    def test_set_timezone(self, create_admin, time):
        asserts(
            assert_data=time.set_timezone({
                'token': create_admin['token'],
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': create_admin['id']
            }),
            data=API_SET_TIMEZONE_SUCCESS
        )

    @title('set-timezone-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для set-timezone')
    def test_set_timezone_method_not_allowed(self, time):
        asserts(
            assert_data=time.set_timezone_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('set-timezone-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для set-timezone')
    def test_set_timezone_bad_request_empty_token(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': '',
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('set-timezone-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для set-timezone')
    def test_set_timezone_bad_request_length_token(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('set-timezone-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id для set-timezone с отрицательным числом в идентификаторе пользователя')
    def test_set_timezone_bad_request_user_id_minus(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': 1,
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('set-timezone-fail-bad-request-user-id-varchar')
    @description(
        'Проверка ошибки Bad Request user id для set-timezone с символами в идентификаторе пользователя')
    def test_set_timezone_bad_request_user_id_varchar(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': 1,
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('set-timezone-fail-bad-request-timezone-minus')
    @description(
        'Проверка ошибки Bad Request timezone для set-timezone с отрицательным числом в идентификаторе часового пояса')
    def test_set_timezone_bad_request_timezone_minus(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': 1,
                'timezone_id': AUTH_DATA_FAIL_BAD_ID,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('set-timezone-fail-bad-request-timezone-varchar')
    @description(
        'Проверка ошибки Bad Request timezone для set-timezone с символами в идентификаторе часового пояса')
    def test_set_timezone_bad_request_timezone_varchar(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': 1,
                'timezone_id': 'text',
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('set-timezone-fail-not-found-empty-token')
    @description('Проверка ошибки Not Found empty token для set-timezone')
    def test_set_timezone_not_found_empty_token(self, time):
        asserts(
            assert_data=time.set_timezone({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('set-timezone-fail-not-found-timezone-id')
    @description('Проверка ошибки Not Found timezone id для set-timezone')
    def test_set_timezone_not_found_timezone_id(self, time, create_admin):
        asserts(
            assert_data=time.set_timezone({
                'token': create_admin['token'],
                'timezone_id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'user_id': create_admin['id']
            }),
            data=API_BAD_TIMEZONE_ID
        )

    @title('set-timezone-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для set-timezone')
    def test_set_timezone_bad_request_bad_rights(self, create_login_delete_user, time):
        asserts(
            assert_data=time.set_timezone({
                'token': create_login_delete_user['token'],
                'timezone_id': DATA_TIMEZONE_RANDOM_NUM,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
