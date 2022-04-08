from allure import title, description, suite, parent_suite

from data import API_LEGAL_ENTITIES_DELETE, API_DELETE_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_FAIL_EMPTY_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, \
    API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_NOT_FOUND_LEGAL_ENTITIES_TYPES, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS, API_NOT_FOUND_LEGAL_ENTITIES_WAS_REMOVED
from pages.api import asserts


@suite('Контроллер: LegalEntities. Метод: delete')
@parent_suite('[PYTHON][API]')
class TestApiLegalEntitiesDelete:
    @title('delete')
    @description('Проверка корректной работы delete')
    def test_delete(self, legal_entities, create_admin, create_legal_entities_remove):
        asserts(
            assert_data=legal_entities.delete({
                'id': create_legal_entities_remove,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_LEGAL_ENTITIES_DELETE
        )

    @title('delete-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для delete')
    def test_delete_method_not_allowed(self, legal_entities):
        asserts(
            assert_data=legal_entities.delete_method_not_allowed(),
            data=API_DELETE_METHOD_NOT_ALLOWED
        )

    @title('delete-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Requst empty token для delete')
    def test_delete_bad_request_empty_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.delete(AUTH_DATA_FAIL_EMPTY_TOKEN),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('delete-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Requst length token для delete')
    def test_delete_bad_request_length_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.delete(AUTH_DATA_FAIL_LENGTH_TOKEN),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('delete-fail-bad-request-id-minus')
    @description(
        'Проверка ошибки Bad Request id minus для delete с отрицательным числом в идентификаторе юридического лица')
    def test_delete_bad_requst_id_minus(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.delete({
                'id': AUTH_DATA_FAIL_BAD_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-id-varchar')
    @description('Проверка ошибки Bad Request id varchar для delete с символами в идентификаторе юридического лица')
    def test_delete_bad_requst_id_varchar(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.delete({
                'id': 'text',
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id minus для delete с отрицательным числом в идентификаторе пользователя')
    def test_delete_bad_requst_user_id_minus(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.delete({
                'id': 1,
                'token': create_admin['token'],
                'user_id': AUTH_DATA_FAIL_BAD_ID,
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-user-id-varchar')
    @description('Проверка ошибки Bad Request user id varchar для delete с символами в идентификаторе пользователя')
    def test_delete_bad_requst_user_id_varchar(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.delete({
                'id': 1,
                'token': create_admin['token'],
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-not-found-token')
    @description('Проверка ошибки Not Found token для delete')
    def test_delete_not_found_token(self, legal_entities, create_login_delete_user):
        asserts(
            assert_data=legal_entities.delete({
                'id': 1,
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_login_delete_user['user_id']
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('delete-fail-not-found')
    @description('Проверка ошибки Not Found object для delete')
    def test_delete_not_found_objects(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.delete({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_LEGAL_ENTITIES_TYPES
        )

    @title('delete-fail-not-found-bad-rights')
    @description('Проверка ошибки Not Found bad rights для delete')
    def test_delete_not_found_bad_rights(self, legal_entities, create_login_delete_user, create_legal_entities_remove):
        asserts(
            assert_data=legal_entities.delete({
                'id': create_legal_entities_remove,
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['user_id'],
            }),
            data=API_BAD_RIGHTS
        )

    @title('delete-fail-not-found-legal-entities-was-removed')
    @description('Проверка ошибки Not Found legal entities was removed для delete')
    def test_delete_not_found_legal_entities_was_removed(self, legal_entities, create_admin,
                                                         create_legal_entities_delete_remove):
        asserts(
            assert_data=legal_entities.delete({
                'id': create_legal_entities_delete_remove,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_LEGAL_ENTITIES_WAS_REMOVED
        )
