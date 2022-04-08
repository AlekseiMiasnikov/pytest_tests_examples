from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_VENDORS_CREATE, DATA_VENDORS_RANDOM_NAME_1_TO_30, API_POST_METHOD_NOT_ALLOWED, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, \
    API_BAD_REQUEST_EMPTY_VENDORS, API_BAD_REQUEST_VENDORS_NAME_LENGTH, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    API_AUTH_NOT_FOUND_TOKEN, API_NOT_FOUND_VENDORS_ICONS, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS


@suite('Контроллер: Vendors. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiVendorsCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, create_admin, vendors, remove_vendors):
        name = DATA_VENDORS_RANDOM_NAME_1_TO_30
        asserts(
            assert_data=vendors.create({
                'token': create_admin['token'],
                'name': name,
                'icon_id': 1,
                'user_id': create_admin['id']
            }),
            data=API_VENDORS_CREATE
        )
        remove_vendors(name)

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, vendors):
        asserts(
            assert_data=vendors.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': '',
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 1,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 1,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-vendors')
    @description('Проверка ошибки Bad Request empty vendors для create')
    def test_create_bad_request_empty_objects(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': 1,
                'name': '',
                'icon_id': 1,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_EMPTY_VENDORS
        )

    @title('create-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для create')
    def test_create_bad_request_length_name(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': 1,
                'name': AUTH_DATA_FAIL_BAD_TOKEN,
                'icon_id': 1,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_VENDORS_NAME_LENGTH
        )

    @title('create-fail-bad-requst-bad-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором пользоваетеля')
    def test_create_bad_request_bad_user_id_minus(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': 1,
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-user-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с cимволами в идентификаторе пользоваетеля')
    def test_create_bad_request_bad_user_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': 1,
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 1,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-icon-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором иконки')
    def test_create_bad_request_bad_icon_id_minus(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': 1,
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': AUTH_DATA_FAIL_BAD_ID,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-icon-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с cимволами в идентификаторе иконки')
    def test_create_bad_request_bad_icon_id_varchar(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': 1,
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 'text',
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_not_found_token(self, vendors):
        asserts(
            assert_data=vendors.create({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 1,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-not-found-vendors-icons')
    @description('Проверка ошибки Not Found vendors icons для create')
    def test_create_not_found_vendors_icons(self, vendors, create_admin):
        asserts(
            assert_data=vendors.create({
                'token': create_admin['token'],
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'user_id': 1
            }),
            data=API_NOT_FOUND_VENDORS_ICONS
        )

    @title('create-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для create')
    def test_create_bad_request_bad_token_and_id(self, vendors, create_admin):
        asserts(
            assert_data=vendors.create({
                'token': create_admin['token'],
                'name': DATA_VENDORS_RANDOM_NAME_1_TO_30,
                'icon_id': 1,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
