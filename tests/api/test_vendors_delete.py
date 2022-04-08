from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_VENDORS_DELETE, API_DELETE_METHOD_NOT_ALLOWED, AUTH_DATA_FAIL_EMPTY_TOKEN, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, \
    API_NOT_FOUND_VENDORS, API_NOT_FOUND_VENDOR_WAS_REMOVED, API_BAD_RIGHTS


@suite('Контроллер: Vendors. Метод: delete')
@parent_suite('[PYTHON][API]')
class TestApiVendorsDelete:
    @title('delete')
    @description('Проверка корректной работы delete')
    def test_delete(self, vendors, create_admin, create_vendors_remove):
        asserts(
            assert_data=vendors.delete({
                'id': create_vendors_remove,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_VENDORS_DELETE
        )

    @title('delete-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для delete')
    def test_delete_method_not_allowed(self, vendors):
        asserts(
            assert_data=vendors.delete_method_not_allowed(),
            data=API_DELETE_METHOD_NOT_ALLOWED
        )

    @title('delete-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Requst empty token для delete')
    def test_delete_bad_request_empty_token(self, vendors):
        asserts(
            assert_data=vendors.delete(AUTH_DATA_FAIL_EMPTY_TOKEN),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('delete-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Requst length token для delete')
    def test_delete_bad_request_length_token(self, vendors):
        asserts(
            assert_data=vendors.delete(AUTH_DATA_FAIL_LENGTH_TOKEN),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('delete-fail-bad-request-id-minus')
    @description('Проверка ошибки Bad Request id minus для delete с отрицательным числом в идентификаторе поставщика')
    def test_delete_bad_requst_id_minus(self, vendors):
        asserts(
            assert_data=vendors.delete({
                'id': AUTH_DATA_FAIL_BAD_ID,
                'token': 1,
                'user_id': 1,
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-id-varchar')
    @description('Проверка ошибки Bad Request id varchar для delete с символами в идентификаторе поставщика')
    def test_delete_bad_requst_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.delete({
                'id': 'text',
                'token': 1,
                'user_id': 1,
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id minus для delete с отрицательным числом в идентификаторе пользователя')
    def test_delete_bad_requst_user_id_minus(self, vendors):
        asserts(
            assert_data=vendors.delete({
                'id': 1,
                'token': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID,
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-user-id-varchar')
    @description('Проверка ошибки Bad Request user id varchar для delete с символами в идентификаторе пользователя')
    def test_delete_bad_requst_user_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.delete({
                'id': 1,
                'token': 1,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-not-found-token')
    @description('Проверка ошибки Not Found token для delete')
    def test_delete_not_found_token(self, vendors, create_login_delete_user):
        asserts(
            assert_data=vendors.delete({
                'id': 1,
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_login_delete_user['user_id']
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('delete-fail-not-found')
    @description('Проверка ошибки Not Found vendors для delete')
    def test_delete_not_found_vendors(self, vendors, create_admin):
        asserts(
            assert_data=vendors.delete({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_VENDORS
        )

    @title('delete-fail-not-found')
    @description('Проверка ошибки Not Found object для delete')
    def test_delete_not_found_objects(self, vendors, create_admin, create_vendors_delete_remove):
        asserts(
            assert_data=vendors.delete({
                'id': create_vendors_delete_remove,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_VENDOR_WAS_REMOVED
        )

    @title('delete-fail-not-found-bad-rights')
    @description('Проверка ошибки Not Found bad rights для delete')
    def test_delete_not_found_bad_rights(self, vendors, create_login_delete_user, create_vendors_remove):
        asserts(
            assert_data=vendors.delete({
                'id': create_vendors_remove,
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['user_id'],
            }),
            data=API_BAD_RIGHTS
        )
