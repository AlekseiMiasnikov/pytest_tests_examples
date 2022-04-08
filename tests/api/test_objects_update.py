from allure import title, description, suite, parent_suite

from data import AUTH_DATA_FAIL_BAD_TOKEN, API_USERS_SUCCESS, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_OBJECTS, \
    API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, \
    API_AUTH_NOT_FOUND_TOKEN, API_NOT_FOUND_OBJECTS, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS, \
    API_BAD_REQUEST_OBJECTS_ACTIVE_CANNOT_DELETE
from pages.api import asserts


@suite('Контроллер: Objects. Метод: update')
@parent_suite('[PYTHON][API]')
class TestApiObjectsUpdate:
    @title('update')
    @description('Проверка корректной работы update')
    def test_update(self, objects, create_admin, create_objects_remove):
        data_id = create_objects_remove
        data_name = AUTH_DATA_FAIL_BAD_TOKEN
        asserts(
            assert_data=objects.update({
                "id": data_id,
                "token": create_admin['token'],
                "name": data_name,
                "user_id": create_admin['id']
            }),
            data={
                **API_USERS_SUCCESS,
                "data": {
                    "id": data_id,
                    "name": data_name
                }})

    @title('update-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для update')
    def test_update_method_not_allowed(self, objects):
        asserts(
            assert_data=objects.update_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для update')
    def test_update_bad_request_empty_token(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                "token": '',
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('update-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для update')
    def test_update_bad_request_length_token(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-objects')
    @description('Проверка ошибки Bad Request empty objects для create')
    def test_update_bad_request_empty_objects(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'name': '',
                'user_id': 1
            }),
            data=API_BAD_REQUEST_EMPTY_OBJECTS
        )

    @title('update-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для update')
    def test_update_bad_request_length_name(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_LENGTH_TOKEN,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS
        )

    @title('update-fail-bad-requst-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для update с отрицательным идентификатором объекта')
    def test_update_bad_request_id_minus(self, objects):
        asserts(
            assert_data=objects.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request user id для update с отрицательным идентификатором пользователя')
    def test_update_bad_request_user_id_minus(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-id-minus')
    @description('Проверка ошибки Bad Request id minus для update с символами в идентификаторе объекта')
    def test_update_bad_request_id_varchar(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 'text',
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request user id для update с символами в идентификаторе пользователя')
    def test_update_bad_request_user_id_varchar(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update')
    def test_update_not_found_token(self, objects):
        asserts(
            assert_data=objects.update({
                "id": 1,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-fail-not-found')
    @description('Проверка ошибки Not Found object для update')
    def test_update_not_found_objects(self, objects, create_admin):
        asserts(
            assert_data=objects.update({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_OBJECTS
        )

    @title('update-fail-bad-requst-active-objects')
    @description('Проверка ошибки Bad Request active objects для update')
    def test_update_bad_request_active_objects(self, objects, create_admin, create_objects_delete_remove):
        asserts(
            assert_data=objects.update({
                'id': create_objects_delete_remove,
                'token': create_admin['token'],
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_OBJECTS_ACTIVE_CANNOT_DELETE
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для update')
    def test_update_bad_request_bad_token_and_id(self, objects, create_admin, create_objects_remove):
        asserts(
            assert_data=objects.update({
                "id": create_objects_remove,
                "token": create_admin['token'],
                "name": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
