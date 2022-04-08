from allure import title, description, suite, parent_suite

from data import API_OBJECTS_DELETE, API_DELETE_METHOD_NOT_ALLOWED, AUTH_DATA_FAIL_EMPTY_TOKEN, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_FAIL_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, \
    AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_OBJECTS, API_BAD_RIGHTS, \
    API_NOT_FOUND_OBJECT_WAS_REMOVED
from pages.api import asserts


@suite('Контроллер: Objects. Метод: delete')
@parent_suite('[PYTHON][API]')
class TestApiObjectsDelete:
    @title('delete')
    @description('Проверка корректной работы delete')
    def test_delete(self, objects, create_admin, create_objects_remove):
        asserts(
            assert_data=objects.delete({
                'id': create_objects_remove,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_OBJECTS_DELETE
        )

    @title('delete-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для delete')
    def test_delete_method_not_allowed(self, objects):
        asserts(
            assert_data=objects.delete_method_not_allowed(),
            data=API_DELETE_METHOD_NOT_ALLOWED
        )

    @title('delete-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Requst empty token для delete')
    def test_delete_bad_request_empty_token(self, objects):
        asserts(
            assert_data=objects.delete(AUTH_DATA_FAIL_EMPTY_TOKEN),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('delete-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Requst length token для delete')
    def test_delete_bad_request_length_token(self, objects):
        asserts(
            assert_data=objects.delete(AUTH_DATA_FAIL_LENGTH_TOKEN),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('delete-fail-not-found-token')
    @description('Проверка ошибки Not Found token для delete')
    def test_delete_not_found_token(self, objects, create_login_delete_user):
        asserts(
            assert_data=objects.delete({
                'id': 1,
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_login_delete_user['user_id']
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('delete-fail-bad-request-id-minus')
    @description('Проверка ошибки Bad Request id minus для delete с отрицательным числом в идентификаторе объекта')
    def test_delete_bad_requst_id_minus(self, objects, create_admin):
        asserts(
            assert_data=objects.delete({
                'id': AUTH_DATA_FAIL_BAD_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-id-varchar')
    @description('Проверка ошибки Bad Request id varchar для delete с символами в идентификаторе объекта')
    def test_delete_bad_requst_id_varchar(self, objects, create_admin):
        asserts(
            assert_data=objects.delete({
                'id': 'text',
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id minus для delete с отрицательным числом в идентификаторе пользователя')
    def test_delete_bad_requst_user_id_minus(self, objects, create_admin):
        asserts(
            assert_data=objects.delete({
                'id': 1,
                'token': create_admin['token'],
                'user_id': AUTH_DATA_FAIL_BAD_ID,
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-user-id-varchar')
    @description('Проверка ошибки Bad Request user id varchar для delete с символами в идентификаторе пользователя')
    def test_delete_bad_requst_user_id_varchar(self, objects, create_admin):
        asserts(
            assert_data=objects.delete({
                'id': 1,
                'token': create_admin['token'],
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-not-found')
    @description('Проверка ошибки Not Found object для delete')
    def test_delete_not_found_objects(self, objects, create_admin):
        asserts(
            assert_data=objects.delete({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_OBJECTS
        )

    @title('delete-fail-not-found-bad-rights')
    @description('Проверка ошибки Not Found bad rights для delete')
    def test_delete_not_found_bad_rights(self, objects, create_login_delete_user, create_objects_remove):
        asserts(
            assert_data=objects.delete({
                'id': create_objects_remove,
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['user_id'],
            }),
            data=API_BAD_RIGHTS
        )

    @title('delete-fail-not-found-objects-was-removed')
    @description('Проверка ошибки Not Found object was removed для delete')
    def test_delete_not_found_objects_was_removed(self, objects, create_admin, create_objects_delete_remove):
        asserts(
            assert_data=objects.delete({
                'id': create_objects_delete_remove,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_OBJECT_WAS_REMOVED
        )
