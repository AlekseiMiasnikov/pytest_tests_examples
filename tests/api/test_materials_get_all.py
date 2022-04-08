from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_SUCCESS, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_BAD_REQUEST_BAD_LIMIT, \
    API_BAD_REQUEST_BAD_OFFSET, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_BAD_RIGHTS


@suite('Контроллер: Materials. Метод: get-all')
@parent_suite('[PYTHON][API]')
class TestApiMaterialGetAll:
    @title('get-all')
    @description('Проверка корректной работы get-all')
    def test_get_all(self, create_admin, materials):
        asserts(
            assert_data=materials.get_all({
                'token': create_admin['token'],
                'limit': 1,
                'offset': 0,
                'user_id': create_admin['id']
            }),
            data=API_USERS_SUCCESS
        )

    @title('get-all-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-all')
    def test_get_all_method_not_allowed(self, materials):
        asserts(
            assert_data=materials.get_all_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-all-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Request empty token для get-all')
    def test_get_all_bad_request_empty_token(self, materials):
        asserts(
            assert_data=materials.get_all({
                'token': '',
                'limit': 1,
                'offset': 0,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-all-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-all')
    def test_get_all_bad_request_length_token(self, materials):
        asserts(
            assert_data=materials.get_all({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'limit': 1,
                'offset': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-all-fail-bad-request-bad-id')
    @description('Проверка ошибки Bad Request bad id для get-all')
    def test_get_all_bad_request_bad_id(self, materials):
        asserts(
            assert_data=materials.get_all({
                'token': 1,
                'limit': AUTH_DATA_FAIL_BAD_ID,
                'offset': 0,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-bad-limit')
    @description('Проверка ошибки Bad Request bad limit для get-all')
    def test_get_all_bad_request_bad_limit(self, materials):
        asserts(
            assert_data=materials.get_all({
                'token': 1,
                'limit': AUTH_DATA_FAIL_BAD_ID,
                'offset': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_LIMIT
        )

    @title('get-all-fail-bad-request-bad-offset')
    @description('Проверка ошибки Bad Request bad offset для get-all')
    def test_get_all_bad_request_bad_offset(self, materials):
        asserts(
            assert_data=materials.get_all({
                'token': 1,
                'limit': 1,
                'offset': AUTH_DATA_FAIL_BAD_ID,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_OFFSET
        )

    @title('get-all-fail-not-found-token')
    @description('Проверка ошки Not Found token для get-all')
    def test_get_all_not_found_token(self, materials):
        asserts(
            assert_data=materials.get_all({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'limit': 1,
                'offset': 0,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-all-fail-bad-request-bad-rights')
    @description('Проверка ошки Bad Request bad rights для get-all')
    def test_get_all_bad_request_bad_rights(self, create_login_delete_user, materials):
        asserts(
            assert_data=materials.get_all({
                'token': create_login_delete_user['token'],
                'limit': 1,
                'offset': 0,
                'user_id': 1
            }),
            data=API_BAD_RIGHTS
        )
