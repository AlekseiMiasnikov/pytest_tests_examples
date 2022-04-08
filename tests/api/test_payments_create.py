from allure import title, description, suite, parent_suite

from data import API_PAYMENTS_SUCCESS, DATA_AMOUNT_PAYMENTS_SUCCESS, DATA_PAYMENTS_TIMESTAMP, \
    API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_FAIL_NOT_FOUND_ID, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_AMOUNT, \
    DATA_AMOUNT_PAYMENTS_BAD, API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD, AUTH_DATA_FAIL_BAD_TOKEN, \
    API_AUTH_NOT_FOUND_TOKEN, API_NOT_FOUND_VENDORS
from pages.api import asserts


@suite('Контроллер: Payments. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiPaymentsCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, create_admin, payments, create_vendors_remove, create_legal_entities_remove, remove_payments):
        vendor_id = create_vendors_remove
        asserts(
            assert_data=payments.create({
                "token": create_admin['token'],
                "vendor_id": vendor_id,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": create_admin['id']
            }),
            data=API_PAYMENTS_SUCCESS
        )
        remove_payments(vendor_id)

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, payments):
        asserts(
            assert_data=payments.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, payments, create_legal_entities_remove, remove_payments):
        asserts(
            assert_data=payments.create({
                "token": '',
                "vendor_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, payments, create_vendors_remove, create_legal_entities_remove):
        asserts(
            assert_data=payments.create({
                "token": AUTH_DATA_LENGTH_TOKEN,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-bad-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором пользоваетеля')
    def test_create_bad_request_bad_user_id_minus(self, payments, create_vendors_remove, create_legal_entities_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-user-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в идентификаторе пользоваетеля')
    def test_create_bad_request_bad_user_id_varchar(self, payments, create_vendors_remove,
                                                    create_legal_entities_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-vendor-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором поставщика')
    def test_create_bad_request_bad_vendor_id_minus(self, payments, create_legal_entities_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": AUTH_DATA_FAIL_BAD_ID,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-vendor-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в идентификаторе поставщика')
    def test_create_bad_request_bad_vendor_id_varchar(self, payments, create_legal_entities_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": 'text',
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-legal-entity-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором юридического лица')
    def test_create_bad_request_bad_legal_entity_id_minus(self, payments, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": AUTH_DATA_FAIL_BAD_ID,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-legal-entity-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в идентификаторе юридического лица')
    def test_create_bad_request_bad_legal_entity_id_varchar(self, payments, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": 'text',
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-amount-varchar')
    @description('Проверка ошибки Bad Request amount для create c символами в сумме платежа')
    def test_create_bad_request_amount_varchar(self, payments, create_legal_entities_remove, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": 'text',
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-amount-minus')
    @description('Проверка ошибки Bad Request amount для create с отрицательным значением в сумме платежа')
    def test_create_bad_request_amount_minus(self, payments, create_legal_entities_remove, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": AUTH_DATA_FAIL_BAD_ID,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-amount-zero')
    @description('Проверка ошибки Bad Request amount для create с нулевым значением в сумме платежа')
    def test_create_bad_request_amount_zero(self, payments, create_legal_entities_remove, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": 0,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-amount-length')
    @description('Проверка ошибки Bad Request amount length для create')
    def test_create_bad_request_amount_length(self, payments, create_legal_entities_remove, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": 1,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_BAD,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_not_found_token(self, payments, create_legal_entities_remove, create_vendors_remove):
        asserts(
            assert_data=payments.create({
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "vendor_id": create_vendors_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-not-found-vendor')
    @description('Проверка ошибки Not Found vendor для create')
    def test_create_not_found_vendor(self, payments, create_admin, create_legal_entities_remove):
        asserts(
            assert_data=payments.create({
                "token": create_admin['token'],
                "vendor_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "legal_entity_id": create_legal_entities_remove,
                "amount": DATA_AMOUNT_PAYMENTS_SUCCESS,
                "created_at": DATA_PAYMENTS_TIMESTAMP,
                "user_id": create_admin['id']
            }),
            data=API_NOT_FOUND_VENDORS
        )
