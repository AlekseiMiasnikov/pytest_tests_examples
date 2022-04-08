from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_LEGAL_ENTITIES_TYPES_OK, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS


@suite('Контроллер: LegalEntitiesTypes. Метод: get-all')
@parent_suite('[PYTHON][API]')
class TestApiLegalEntitiesTypesGetAll:
    @title('get-all')
    @description('Проверка корректной работы get-all')
    def test_get_all(self, legal_entities_types, create_admin):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': create_admin['token'],
                'user_id': create_admin['id']
            }),
            data=API_LEGAL_ENTITIES_TYPES_OK
        )

    @title('get-all-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-all')
    def test_get_all_method_not_allowed(self, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-all-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-all')
    def test_get_all_bad_request_empty_token(self, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': '',
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-all-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-all')
    def test_get_all_bad_request_length_token(self, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'limit': 1,
                'offset': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-all-fail-bad-request-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для get-all с отрицательным индентификатором')
    def test_get_all_bad_request_bad_id_minus(self, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': 1,
                'limit': 1,
                'offset': 0,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для get-all с символами в индентификаторе')
    def test_get_all_bad_request_bad_id_varchar(self, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': 1,
                'limit': 1,
                'offset': 0,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-all')
    def test_get_all_not_found_empty_token(self, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'limit': 1,
                'offset': 0,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-all-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-all')
    def test_get_all_bad_request_bad_rights(self, create_login_delete_user, legal_entities_types):
        asserts(
            assert_data=legal_entities_types.get_all({
                'token': create_login_delete_user['token'],
                'limit': 1,
                'offset': 0,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
