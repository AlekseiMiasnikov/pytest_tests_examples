from allure import title, description, suite, parent_suite

from data import API_OBJECTS_CREATE, AUTH_DATA_FAIL_BAD_TOKEN, API_POST_METHOD_NOT_ALLOWED, \
    API_AUTH_TOKEN_EMPTY, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_OBJECTS, \
    API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, \
    API_AUTH_NOT_FOUND_TOKEN, API_BAD_REQUEST_OBJECTS_ALLREDY_EXIST, API_BAD_RIGHTS, AUTH_DATA_FAIL_NOT_FOUND_ID
from pages.api import asserts


@suite('Контроллер: Objects. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiObjectsCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, create_admin, objects, remove_objects):
        name = AUTH_DATA_FAIL_BAD_TOKEN
        asserts(
            assert_data=objects.create({
                'token': create_admin['token'],
                'name': name,
                'user_id': create_admin['id']
            }),
            data=API_OBJECTS_CREATE
        )
        remove_objects(name)

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, objects):
        asserts(
            assert_data=objects.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, objects):
        asserts(
            assert_data=objects.create({
                'token': '',
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, objects):
        asserts(
            assert_data=objects.create({
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-objects')
    @description('Проверка ошибки Bad Request empty objects для create')
    def test_create_bad_request_empty_objects(self, objects):
        asserts(
            assert_data=objects.create({
                'name': '',
                'token': 1,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_EMPTY_OBJECTS
        )

    @title('create-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для create')
    def test_create_bad_request_length_name(self, objects):
        asserts(
            assert_data=objects.create({
                'name': AUTH_DATA_LENGTH_TOKEN,
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS
        )

    @title('create-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request user id для create с отрицательным идентификатором пользователя')
    def test_create_bad_request_user_id_minus(self, objects):
        asserts(
            assert_data=objects.create({
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request user id для create с символами в идентификаторе пользователя')
    def test_create_bad_request_user_id_varchar(self, objects):
        asserts(
            assert_data=objects.create({
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': 1,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_not_found_token(self, objects):
        asserts(
            assert_data=objects.create({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-bad-request-allredy-exist')
    @description('Проверка ошибки Bad Request allredy exist для create')
    def test_create_bad_request_allredy_exist(self, objects, create_admin, objects_name_allready_exist):
        asserts(
            assert_data=objects.create({
                'token': objects_name_allready_exist['token'],
                'name': objects_name_allready_exist['name'],
                'user_id': objects_name_allready_exist['user_id']
            }),
            data=API_BAD_REQUEST_OBJECTS_ALLREDY_EXIST
        )

    @title('create-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для create')
    def test_create_bad_request_bad_token_and_id(self, objects, create_admin):
        asserts(
            assert_data=objects.create({
                'token': create_admin['token'],
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
