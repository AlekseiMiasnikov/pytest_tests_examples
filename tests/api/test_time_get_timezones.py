from allure import title, description, suite, parent_suite

from data import API_USERS_SUCCESS, API_TIMEZONES, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_BAD_RIGHTS, AUTH_DATA_FAIL_NOT_FOUND_ID
from pages.api import asserts


@suite('Контроллер: Time. Метод: get-timezones')
@parent_suite('[PYTHON][API]')
class TestApiTimeGetTimezones:
    @title('get-timezones')
    @description('Проверка корректной работы get-timezones')
    def test_get_timezones(self, create_admin, time):
        asserts(
            assert_data=time.get_timezones({
                'token': create_admin['token'],
                'user_id': create_admin['id']
            }),
            data={
                **API_USERS_SUCCESS,
                **API_TIMEZONES
            }
        )

    @title('get-timezones-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-timezones')
    def test_get_timezones_method_not_allowed(self, time):
        asserts(
            assert_data=time.get_timezones_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-timezones-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-timezones')
    def test_get_timezones_bad_request_empty_token(self, time):
        asserts(
            assert_data=time.get_timezones({
                'token': '',
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-timezones-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-timezones')
    def test_get_timezones_bad_request_length_token(self, time):
        asserts(
            assert_data=time.get_timezones({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-timezones-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id для get-timezones с отрицательным числом в идентификаторе пользователя')
    def test_get_timezones_bad_request_user_id_minus(self, time):
        asserts(
            assert_data=time.get_timezones({
                'token': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-timezones-fail-bad-request-user-id-varchar')
    @description(
        'Проверка ошибки Bad Request user id для get-timezones с символами в идентификаторе пользователя')
    def test_get_timezones_bad_request_user_id_varchar(self, time):
        asserts(
            assert_data=time.get_timezones({
                'token': 1,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-timezones-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-timezones')
    def test_get_timezones_not_found_empty_token(self, time):
        asserts(
            assert_data=time.get_timezones({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-timezones-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-timezones')
    def test_get_timezones_bad_request_bad_rights(self, create_login_delete_user, time):
        asserts(
            assert_data=time.get_timezones({
                'token': create_login_delete_user['token'],
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
