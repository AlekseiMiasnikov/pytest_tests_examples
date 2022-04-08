from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_GET_INFO, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, \
    API_AUTH_NOT_FOUND_TOKEN, API_BAD_RIGHTS, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID


@suite('Контроллер: Users. Метод: get-info')
@parent_suite('[PYTHON][API]')
class TestApiUsersGetInfo:
    @title('get-info')
    @description('Проверка корректной работы get-info')
    def test_get_info(self, create_admin, users):
        response = users.get_info({
            'token': create_admin['token'],
            'user_id': create_admin['id'],
        })
        asserts(
            assert_data=response,
            data=API_USERS_GET_INFO
        )
        assert response['data']['login'] == create_admin['user']['login']
        assert response['data']['email'] == create_admin['user']['email']

    @title('get-info-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-info')
    def test_get_info_not_allowed(self, users):
        asserts(
            assert_data=users.get_info_method_not_allowed({
                'token': '',
                'user_id': 1,
            }),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-info-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Request empty token для get-info')
    def test_get_info_bad_request_empty_token(self, users):
        asserts(
            assert_data=users.get_info({
                'token': '',
                'user_id': 1,
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-info-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-info')
    def test_get_info_bad_request_length_token(self, users):
        asserts(
            assert_data=users.get_info({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': 1,
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-info-fail-bad-request-bad-id')
    @description('Проверка ошибки Bad Request bad id для get-info с отрицательным числом')
    def test_get_info_bad_request_bad_id_minus(self, users):
        asserts(
            assert_data=users.get_info({
                'token': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID,
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-info-fail-bad-request-bad-id')
    @description('Проверка ошибки Bad Request bad id для get-info с текстом')
    def test_get_info_bad_request_bad_id_varchar(self, users):
        asserts(
            assert_data=users.get_info({
                'token': 1,
                'user_id': 'text',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-info-fail-not_found-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-info')
    def test_get_info_not_found_user_bad_token(self, users):
        asserts(
            assert_data=users.get_info({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1,
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-info-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-info')
    def test_get_info_bad_request_bad_rights(self, create_login_delete_user, users):
        asserts(
            assert_data=users.get_info({
                'token': create_login_delete_user['token'],
                'user_id': 1,
            }),
            data=API_BAD_RIGHTS
        )
