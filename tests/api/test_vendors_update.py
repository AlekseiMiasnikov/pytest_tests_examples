from allure import title, description, suite, parent_suite

from data import API_USERS_SUCCESS, AUTH_DATA_FAIL_BAD_PASSWORD, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_VENDORS, AUTH_DATA_FAIL_BAD_TOKEN, \
    API_BAD_REQUEST_VENDORS_NAME_LENGTH, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_AUTH_NOT_FOUND_TOKEN, \
    API_NOT_FOUND_VENDORS, AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_VENDORS_ICONS, \
    API_BAD_REQUEST_VENDORS_ACTIVE_CANNOT_DELETE, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Vendors. Метод: update')
@parent_suite('[PYTHON][API]')
class TestApiVendorsUpdate:
    @title('update')
    @description('Проверка корректной работы update')
    def test_update(self, vendors, create_admin, create_vendors_remove):
        data_id = create_vendors_remove
        data_name = AUTH_DATA_FAIL_BAD_PASSWORD
        asserts(
            assert_data=vendors.update({
                "id": data_id,
                "token": create_admin['token'],
                "name": data_name,
                'icon_id': 1,
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
    def test_update_method_not_allowed(self, vendors):
        asserts(
            assert_data=vendors.update_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для update')
    def test_update_bad_request_empty_token(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": '',
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('update-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для update')
    def test_update_bad_request_length_token(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-vendors')
    @description('Проверка ошибки Bad Request empty vendors для create')
    def test_update_bad_request_empty_vendors(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                'token': 1,
                'name': '',
                'icon_id': 1,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_EMPTY_VENDORS
        )

    @title('update-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для update')
    def test_update_bad_request_length_name(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_LENGTH_TOKEN,
                'icon_id': 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_VENDORS_NAME_LENGTH
        )

    @title('update-fail-bad-requst-id-minus')
    @description('Проверка ошибки Bad Request id для update с отрицательным идентификатором поставщика')
    def test_update_bad_request_id_minus(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-id-minus')
    @description('Проверка ошибки Bad Request user id для update с отрицательным идентификатором пользователя')
    def test_update_bad_request_user_id_minus(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-icon-id-minus')
    @description('Проверка ошибки Bad Request icon id для update с отрицательным идентификатором иконки')
    def test_update_bad_request_icon_id_minus(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': AUTH_DATA_FAIL_BAD_ID,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-id-varchar')
    @description('Проверка ошибки Bad Request bad id для update с символами в идентификаторе поставщика')
    def test_update_bad_request_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 'text',
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request id для update с символами в идентификаторе пользователя')
    def test_update_bad_request_user_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-icon-id-varchar')
    @description('Проверка ошибки Bad Request icon id для update с символами в идентификаторе иконки')
    def test_update_bad_request_icon_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": 1,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 'text',
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update')
    def test_update_not_found_token(self, vendors):
        asserts(
            assert_data=vendors.update({
                "id": 1,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-fail-not-found-vendors-id')
    @description('Проверка ошибки Not Found vendors id для update')
    def test_update_not_found_vendors_id(self, vendors, create_admin):
        asserts(
            assert_data=vendors.update({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'name': AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                'user_id': create_admin['id'],
            }),
            data=API_NOT_FOUND_VENDORS
        )

    @title('update-fail-not-found-vendors-icon')
    @description('Проверка ошибки Not Found vendors icon для update')
    def test_update_not_found_vendors_icon(self, vendors, create_admin, create_vendors_remove):
        asserts(
            assert_data=vendors.update({
                'id': create_vendors_remove,
                'token': create_admin['token'],
                'name': AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'user_id': create_admin['id']
            }),
            data=API_NOT_FOUND_VENDORS_ICONS
        )

    @title('update-fail-bad-requst-active-vendors')
    @description('Проверка ошибки Bad Request active vendors для update')
    def test_update_bad_request_active_objects(self, vendors, create_admin, create_vendors_delete_remove):
        asserts(
            assert_data=vendors.update({
                'id': create_vendors_delete_remove,
                'token': create_admin['token'],
                'name': AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_VENDORS_ACTIVE_CANNOT_DELETE
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для update')
    def test_update_bad_request_bad_token_and_id(self, vendors, create_admin, create_vendors_remove):
        asserts(
            assert_data=vendors.update({
                "id": create_vendors_remove,
                "token": create_admin['token'],
                "name": AUTH_DATA_FAIL_BAD_PASSWORD,
                'icon_id': 1,
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
