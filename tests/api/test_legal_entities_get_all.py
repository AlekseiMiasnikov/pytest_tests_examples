from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_SUCCESS, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_BAD_REQUEST_BAD_LIMIT, \
    API_BAD_REQUEST_BAD_OFFSET, API_BAD_REQUEST_LEGAL_ENTITIES_ARCHIVE, AUTH_DATA_FAIL_BAD_TOKEN, \
    API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS


@suite('Контроллер: LegalEntities. Метод: get-all')
@parent_suite('[PYTHON][API]')
class TestApiLegalEntitiesGetAll:
    @title('get-all')
    @description('Проверка корректной работы get-all c acrhive = 0')
    def test_get_all(self, create_admin, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': create_admin['token'],
                'limit': 1,
                'offset': 0,
                'archive': 0,
                'user_id': create_admin['id']
            }),
            data=API_USERS_SUCCESS
        )

    @title('get-all')
    @description('Проверка корректной работы get-all c acrhive = 1')
    def test_get_all_acrhive_ok(self, create_admin, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': create_admin['token'],
                'limit': 1,
                'offset': 0,
                'archive': 1,
                'user_id': create_admin['id']
            }),
            data=API_USERS_SUCCESS
        )

    @title('get-all-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-all')
    def test_get_all_method_not_allowed(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-all-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-all')
    def test_get_all_bad_request_empty_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': '',
                'limit': 1,
                'offset': 0,
                'archive': 0,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-all-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-all')
    def test_get_all_bad_request_length_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'limit': 1,
                'offset': 0,
                'archive': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-all-fail-bad-request-bad-id-minus')
    @description(
        'Проверка ошибки Bad Request bad id для get-all с отрицательным числом для идентификатора пользователя')
    def test_get_all_bad_request_bad_id_minus(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': 1,
                'limit': 1,
                'offset': 0,
                'archive': 0,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для get-all с символами в идентификаторе пользователя')
    def test_get_all_bad_request_bad_id_varchar(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': 1,
                'limit': 1,
                'offset': 0,
                'archive': 0,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-bad-limit')
    @description('Проверка ошибки Bad Request bad limit для get-all')
    def test_get_all_bad_request_bad_limit(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': 1,
                'limit': AUTH_DATA_FAIL_BAD_ID,
                'offset': 0,
                'archive': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_LIMIT
        )

    @title('get-all-fail-bad-request-bad-offset')
    @description('Проверка ошибки Bad Request bad offset для get-all')
    def test_get_all_bad_request_bad_offset(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': 1,
                'limit': 1,
                'offset': AUTH_DATA_FAIL_BAD_ID,
                'archive': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_OFFSET
        )

    @title('get-all-fail-bad-request-bad-archive')
    @description('Проверка ошибки Bad Request bad archive для get-all')
    def test_get_all_bad_request_bad_archive(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': 1,
                'limit': 1,
                'offset': 0,
                'archive': 2,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LEGAL_ENTITIES_ARCHIVE
        )

    @title('get-all-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-all')
    def test_get_all_not_found_empty_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'limit': 1,
                'offset': 0,
                'archive': 0,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-all-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-all')
    def test_get_all_bad_request_bad_rights(self, create_login_delete_user, legal_entities):
        asserts(
            assert_data=legal_entities.get_all({
                'token': create_login_delete_user['token'],
                'limit': 1,
                'offset': 1,
                'archive': 0,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
