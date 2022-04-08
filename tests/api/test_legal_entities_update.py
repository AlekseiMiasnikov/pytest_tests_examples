from allure import title, description, suite, parent_suite

from data import DATA_LEGAL_ENTITIES_TYPES_RANDOM, DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20, API_USERS_SUCCESS, \
    API_PUT_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_BAD_REQUEST_EMPTY_LEGAL_ENTITIES, API_BAD_REQUEST_LEGAL_ENTITIES_NAME_LENGTH, \
    AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, \
    API_NOT_FOUND_LEGAL_ENTITIES_TYPES, API_NOT_FOUND_LEGAL_ENTITIES, \
    API_BAD_REQUEST_LEGAL_ENTITIES_ACTIVE_CANNOT_DELETE, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: LegalEntities. Метод: update')
@parent_suite('[PYTHON][API]')
class TestApiLegalEntitiesUpdate:
    @title('update')
    @description('Проверка корректной работы update')
    def test_update(self, legal_entities, create_admin, create_legal_entities_remove):
        data_id = create_legal_entities_remove
        data_name = DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20
        data_legal_entities_type_id = DATA_LEGAL_ENTITIES_TYPES_RANDOM
        asserts(
            assert_data=legal_entities.update({
                "id": data_id,
                "token": create_admin['token'],
                "name": data_name,
                "legal_entities_type_id": data_legal_entities_type_id,
                "user_id": create_admin['id']
            }),
            data={
                **API_USERS_SUCCESS,
                "data": {
                    "id": data_id,
                    "name": data_name,
                    "legal_entities_type_id": data_legal_entities_type_id
                }})

    @title('update-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для update')
    def test_update_method_not_allowed(self, legal_entities):
        asserts(
            assert_data=legal_entities.update_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для update')
    def test_update_bad_request_empty_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": '',
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('update-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для update')
    def test_update_bad_request_length_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-legal-entities')
    @description('Проверка ошибки Bad Request empty objects для create')
    def test_update_bad_request_empty_legal_entities(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'name': '',
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_EMPTY_LEGAL_ENTITIES
        )

    @title('update-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для update')
    def test_update_bad_request_length_name(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LEGAL_ENTITIES_NAME_LENGTH
        )

    @title('update-fail-bad-requst-id-minus')
    @description('Проверка ошибки Bad Request id для update с отрицательным идентификатором юридического лица')
    def test_update_bad_request_id_minus(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": 1,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-legal-entities-type-id-minus')
    @description('Проверка ошибки Bad Request legal entities type id для update с отрицательным идентификатором \
    типа юридического лица')
    def test_update_bad_request_legal_entities_type_id_minus(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": 1,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": AUTH_DATA_FAIL_BAD_ID,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request user id для update с отрицательным идентификатором пользователя')
    def test_update_bad_request_user_id_minus(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": 1,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-id-varchar')
    @description('Проверка ошибки Bad Request id для update с символами в идентификаторе юридического лица')
    def test_update_bad_request_id_varchar(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 'text',
                "token": 1,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-legal-entities-type-id-varchar')
    @description('Проверка ошибки Bad Request legal entities type id для update с символами в идентификаторе \
    типа юридического лица')
    def test_update_bad_request_legal_entities_type_id_varchar(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": 1,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": 'text',
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request user id для update с символами в идентификаторе пользователя')
    def test_update_bad_request_user_id_varchar(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": 1,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update')
    def test_update_not_found_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.update({
                "id": 1,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-fail-not-found')
    @description('Проверка ошибки Not Found legal entities для update')
    def test_update_not_found_legal_entities_types(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.update({
                'id': 1,
                'token': create_admin['token'],
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_LEGAL_ENTITIES_TYPES
        )

    @title('update-fail-not-found')
    @description('Проверка ошибки Not Found legal entities для update')
    def test_update_not_found_legal_entities(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.update({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_LEGAL_ENTITIES
        )

    @title('update-fail-bad-requst-active-legal-entities')
    @description('Проверка ошибки Bad Request active objects для update')
    def test_update_bad_request_active_legal_entities(self, legal_entities, create_admin,
                                                      create_legal_entities_delete_remove):
        asserts(
            assert_data=legal_entities.update({
                'id': create_legal_entities_delete_remove,
                'token': create_admin['token'],
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_LEGAL_ENTITIES_ACTIVE_CANNOT_DELETE
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для update')
    def test_update_bad_request_bad_token_and_id(self, legal_entities, create_admin, create_legal_entities_remove):
        asserts(
            assert_data=legal_entities.update({
                "id": create_legal_entities_remove,
                "token": create_admin['token'],
                "name": DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
