from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_VENDORS_RESTORE, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, AUTH_DATA_FAIL_BAD_TOKEN, \
    API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_VENDORS, \
    API_BAD_REQUEST_VENDORS_WAS_RESTORED, API_BAD_RIGHTS


@suite('Контроллер: Vendors. Метод: restore')
@parent_suite('[PYTHON][API]')
class TestApiVendorsRestore:
    @title('restore')
    @description('Проверка корректной работы update')
    def test_restore(self, vendors, create_admin, create_vendors_delete_remove):
        asserts(
            assert_data=vendors.restore({
                "id": create_vendors_delete_remove,
                "token": create_admin['token'],
                "user_id": create_admin['id']
            }),
            data=API_VENDORS_RESTORE
        )

    @title('restore-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для restore')
    def test_restore_method_not_allowed(self, vendors):
        asserts(
            assert_data=vendors.restore_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('restore-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для restore')
    def test_restore_bad_request_empty_token(self, vendors):
        asserts(
            assert_data=vendors.restore({
                "id": 1,
                "token": '',
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('restore-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для restore')
    def test_restore_bad_request_length_token(self, vendors):
        asserts(
            assert_data=vendors.restore({
                "id": 1,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('restore-fail-bad-requst-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для restore с отрицательным идентификатором поставщика')
    def test_restore_bad_request_bad_id_minus(self, vendors, create_admin):
        asserts(
            assert_data=vendors.restore({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": create_admin['token'],
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-bad-requst-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для restore с символами в идентификаторе поставщика')
    def test_restore_bad_request_bad_id_varchar(self, vendors, create_admin):
        asserts(
            assert_data=vendors.restore({
                "id": 'text',
                "token": create_admin['token'],
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-bad-requst-bad-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для restore с отрицательным идентификатором пользователя')
    def test_restore_bad_request_bad_user_id_minus(self, vendors, create_admin):
        asserts(
            assert_data=vendors.restore({
                "id": 1,
                "token": create_admin['token'],
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-bad-requst-bad-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для restore с символами в идентификаторе пользователя')
    def test_restore_bad_request_bad_user_id_varchar(self, vendors, create_admin):
        asserts(
            assert_data=vendors.restore({
                "id": 1,
                "token": create_admin['token'],
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('restore-fail-not-found-token')
    @description('Проверка ошибки Not Found token для restore')
    def test_restore_not_found_token(self, vendors):
        asserts(
            assert_data=vendors.restore({
                "id": 1,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('restore-fail-not-found-vendors')
    @description('Проверка ошибки Not Found vendors для restore')
    def test_restore_not_found_vendors(self, vendors, create_admin):
        asserts(
            assert_data=vendors.restore({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_VENDORS
        )

    @title('restore-fail-bad-requst-vendor-was-restored')
    @description('Проверка ошибки Bad Request vendor was restored для restore')
    def test_restore_bad_request_vendor_was_restored(self, vendors, create_admin, create_vendors_remove):
        asserts(
            assert_data=vendors.restore({
                "id": create_vendors_remove,
                "token": create_admin['token'],
                "user_id": create_admin['id']
            }),
            data=API_BAD_REQUEST_VENDORS_WAS_RESTORED
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для restore')
    def test_restore_bad_request_bad_token_and_id(self, vendors, create_admin, create_vendors_delete_remove):
        asserts(
            assert_data=vendors.restore({
                "id": create_vendors_delete_remove,
                "token": create_admin['token'],
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
