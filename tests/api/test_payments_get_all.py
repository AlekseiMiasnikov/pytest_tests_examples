from json import dumps

from allure import title, description, suite, parent_suite

from data import API_USERS_SUCCESS, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, API_BAD_REQUEST_LENGTH_TOKEN, \
    AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_BAD_REQUEST_BAD_LIMIT, \
    API_BAD_REQUEST_BAD_OFFSET, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, \
    API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Payments. Метод: get-all')
@parent_suite('[PYTHON][API]')
class TestApiPaymentsGetAll:
    @title('get-all')
    @description('Проверка корректной работы get-all')
    def test_get_all(self, create_admin, payments):
        asserts(
            assert_data=payments.get_all({
                'token': create_admin['token'],
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': create_admin['id']
            }),
            data=API_USERS_SUCCESS
        )

    @title('get-all-with-vendor-and-legal-entity')
    @description('Проверка корректной работы get-all с поставщиком, юридическим лицом и оплатой')
    def test_get_all_with_vendor_legal_entity_payment(self, create_admin, payments,
                                                      create_vendor_legal_entity_payment_remove):
        asserts(
            assert_data=payments.get_all({
                'token': create_admin['token'],
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': create_admin['id']
            }),
            data={
                **API_USERS_SUCCESS,
                "data": {
                    "payments": {
                        "ООО legal_entity": [
                            {
                                "vendor_id": create_vendor_legal_entity_payment_remove['vendor_id'],
                                "vendor": create_vendor_legal_entity_payment_remove['vendor'],
                                "amount": create_vendor_legal_entity_payment_remove['amount'],
                                "created_at": create_vendor_legal_entity_payment_remove['created_at'],
                                "legal_entity_id": create_vendor_legal_entity_payment_remove['legal_entity_id'],
                                "legal_entity": create_vendor_legal_entity_payment_remove['legal_entity'],
                                "legal_entity_type": create_vendor_legal_entity_payment_remove['legal_entity_type'],
                                "legal_entities_type_id": create_vendor_legal_entity_payment_remove[
                                    'legal_entities_type_id']
                            }
                        ]
                    }
                }
            }
        )

    @title('get-all-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-all')
    def test_get_all_method_not_allowed(self, payments):
        asserts(
            assert_data=payments.get_all_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-all-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-all')
    def test_get_all_bad_request_empty_token(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': '',
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-all-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-all')
    def test_get_all_bad_request_length_token(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-all-fail-bad-request-id-minus')
    @description(
        'Проверка ошибки Bad Request id для get-all с отрицательным числом в идентификаторе пользователя')
    def test_get_all_bad_request_id_minus(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': 1,
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-id-varchar')
    @description('Проверка ошибки Bad Request id для get-all с символами в идентификаторе пользователя')
    def test_get_all_bad_request_id_varchar(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': 1,
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-bad-limit')
    @description('Проверка ошибки Bad Request bad limit для get-all')
    def test_get_all_bad_request_bad_limit(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': 1,
                'limit': AUTH_DATA_FAIL_BAD_ID,
                'offset': dumps({"1": 0}),
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_LIMIT
        )

    @title('get-all-fail-bad-request-bad-offset')
    @description('Проверка ошибки Bad Request bad offset для get-all')
    def test_get_all_bad_request_bad_offset(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': 1,
                'limit': 1,
                'offset': dumps({"1": AUTH_DATA_FAIL_BAD_ID}),
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_OFFSET
        )

    @title('get-all-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-all')
    def test_get_all_not_found_empty_token(self, payments):
        asserts(
            assert_data=payments.get_all({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-all-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-all')
    def test_get_all_bad_request_bad_rights(self, create_login_delete_user, payments):
        asserts(
            assert_data=payments.get_all({
                'token': create_login_delete_user['token'],
                'limit': 1,
                'offset': dumps({"1": 0}),
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
