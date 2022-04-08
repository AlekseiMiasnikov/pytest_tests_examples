from allure import title, description, suite, parent_suite

from data import API_LEGAL_ENTITIES_RESTORE, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_LEGAL_ENTITIES, \
    API_BAD_RIGHTS, API_BAD_REQUEST_LEGAL_ENTITIES_WAS_RESTORED
from pages.api import asserts


@suite('Контроллер: LegalEntities. Метод: restore')
@parent_suite('[PYTHON][API]')
class TestApiLegalEntitiesRestore:
    @title('restore')
    @description('Проверка корректной работы restore')
    def test_restore(self, legal_entities, create_admin, create_legal_entities_delete_remove):
        asserts(
            assert_data=legal_entities.restore({
                "id": create_legal_entities_delete_remove,
                "token": create_admin['token'],
                "user_id": create_admin['id']
            }),
            data=API_LEGAL_ENTITIES_RESTORE
        )

    @title('restore-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для restore')
    def test_restore_method_not_allowed(self, legal_entities):
        asserts(
            assert_data=legal_entities.restore_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('restore-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для restore')
    def test_restore_bad_request_empty_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.restore({
                "id": 1,
                "token": '',
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('restore-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для restore')
    def test_restore_bad_request_length_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.restore({
                "id": 1,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('restore-fail-bad-requst-id-minus')
    @description('Проверка ошибки Bad Request id для restore с отрицательным идентификатором юридического лица')
    def test_restore_bad_request_id_minus(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.restore({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": create_admin['token'],
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-bad-requst-id-varchar')
    @description('Проверка ошибки Bad Request bad id для restore с символами в идентификаторе юридического лица')
    def test_restore_bad_request_id_varchar(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.restore({
                "id": 'text',
                "token": create_admin['token'],
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для restore с отрицательным идентификатором пользователя')
    def test_restore_bad_request_user_id_minus(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.restore({
                "id": 1,
                "token": create_admin['token'],
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для restore с символами в идентификаторе пользователя')
    def test_restore_bad_request_user_id_varchar(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.restore({
                "id": 1,
                "token": create_admin['token'],
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-not-found-token')
    @description('Проверка ошибки Not Found token для restore')
    def test_restore_not_found_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.restore({
                "id": 1,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('restore-fail-not-found-legal-entities')
    @description('Проверка ошибки Not Found legal entities для restore')
    def test_restore_not_found_legal_entities(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.restore({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_LEGAL_ENTITIES
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для restore')
    def test_restore_bad_request_bad_token_and_id(self, legal_entities, create_admin,
                                                  create_legal_entities_delete_remove):
        asserts(
            assert_data=legal_entities.restore({
                "id": create_legal_entities_delete_remove,
                "token": create_admin['token'],
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )

    @title('restore-fail-bad-requst-legal-entities-was-restored')
    @description('Проверка ошибки Bad Request legal entities was restored для restore')
    def test_restore_bad_request_legal_entities_was_restored(self, legal_entities, create_admin,
                                                             create_legal_entities_remove):
        asserts(
            assert_data=legal_entities.restore({
                "id": create_legal_entities_remove,
                "token": create_admin['token'],
                "user_id": create_admin['id']
            }),
            data=API_BAD_REQUEST_LEGAL_ENTITIES_WAS_RESTORED
        )
