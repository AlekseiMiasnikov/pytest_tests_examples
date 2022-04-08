from allure import title, description, suite, parent_suite

from data import DATA_LEGAL_ENTITIES_TYPES_RANDOM, API_LEGAL_ENTITIES_CREATE, \
    DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20, API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_LEGAL_ENTITIES, \
    API_BAD_REQUEST_LEGAL_ENTITIES_NAME_LENGTH, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, \
    API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, API_NOT_FOUND_LEGAL_ENTITIES_TYPES, API_BAD_RIGHTS, \
    AUTH_DATA_FAIL_NOT_FOUND_ID
from pages.api import asserts


@suite('Контроллер: LegalEntities. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiLegalEntitiesCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, create_admin, legal_entities, remove_legal_entities):
        name = DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20
        asserts(
            assert_data=legal_entities.create({
                'token': create_admin['token'],
                'name': name,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': create_admin['id']
            }),
            data=API_LEGAL_ENTITIES_CREATE
        )
        remove_legal_entities(name)

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, legal_entities):
        asserts(
            assert_data=legal_entities.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': '',
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-objects')
    @description('Проверка ошибки Bad Request empty objects для create')
    def test_create_bad_request_empty_objects(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': 1,
                'name': '',
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_EMPTY_LEGAL_ENTITIES
        )

    @title('create-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для create')
    def test_create_bad_request_length_name(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': 1,
                'name': AUTH_DATA_LENGTH_TOKEN,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LEGAL_ENTITIES_NAME_LENGTH
        )

    @title('create-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request user id для create с отрицательным числом в идентификаторе пользователя')
    def test_create_bad_request_user_id_minus(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': 1,
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с cимволами в идентификаторе пользователя')
    def test_create_bad_request_user_id_varchar(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': 1,
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id для create с отрицательным числом в идентификаторе типа юридического лица')
    def test_create_bad_request_legal_entities_type_id_minus(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': 1,
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": AUTH_DATA_FAIL_BAD_ID,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-user-id-varchar')
    @description(
        'Проверка ошибки Bad Request user id для create с символами в идентификаторе типа юридического лица')
    def test_create_bad_request_legal_entities_type_id_varchar(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': 1,
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": 'text',
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_not_found_token(self, legal_entities):
        asserts(
            assert_data=legal_entities.create({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-not-found-legal-entities-types')
    @description('Проверка ошибки Not Found legal entities types для create')
    def test_create_not_found_legal_entities_types(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.create({
                'token': create_admin['token'],
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": 7,
                'user_id': create_admin['id']
            }),
            data=API_NOT_FOUND_LEGAL_ENTITIES_TYPES
        )

    @title('create-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для create')
    def test_create_bad_request_bad_token_and_id(self, legal_entities, create_admin):
        asserts(
            assert_data=legal_entities.create({
                'token': create_admin['token'],
                'name': DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20,
                "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
