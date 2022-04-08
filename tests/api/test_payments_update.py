from allure import title, description, suite, parent_suite

from data import API_USERS_SUCCESS, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_BAD_REQUEST_AMOUNT, \
    DATA_AMOUNT_PAYMENTS_BAD, API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD, API_AUTH_NOT_FOUND_TOKEN, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_NOT_FOUND_VENDORS, AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_PAYMENT, \
    API_BAD_RIGHTS, API_NOT_FOUND_PAYMENT_LEGAL_ENTITIES
from pages.api import asserts


@suite('Контроллер: Payments. Метод: update')
@parent_suite('[PYTHON][API]')
class TestApiPaymentsUpdate:
    @title('update')
    @description('Проверка корректной работы update')
    def test_update(self, payments, create_admin, create_vendor_legal_entity_payment_remove):
        payment_id = create_vendor_legal_entity_payment_remove['id']
        payment_amount = create_vendor_legal_entity_payment_remove['amount']
        payment_vendor_id = create_vendor_legal_entity_payment_remove['vendor_id']
        payment_legal_entity_id = create_vendor_legal_entity_payment_remove['legal_entity_id']
        payment_created_at = create_vendor_legal_entity_payment_remove['created_at']
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": payment_vendor_id,
                "id": payment_id,
                "legal_entity_id": payment_legal_entity_id,
                "amount": payment_amount,
                "created_at": payment_created_at,
                "user_id": create_admin['id']
            }),
            data={
                **API_USERS_SUCCESS,
                "data": {
                    "id": payment_id,
                    "vendor_id": payment_vendor_id,
                    "legal_entity_id": payment_legal_entity_id,
                    "amount": payment_amount,
                    "created_at": payment_created_at
                }
            }
        )

    @title('update-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для update')
    def test_update_method_not_allowed(self, payments):
        asserts(
            assert_data=payments.update_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для update')
    def test_update_bad_request_empty_token(self, payments):
        asserts(
            assert_data=payments.update({
                "token": '',
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('update-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для update')
    def test_update_bad_request_length_token(self, payments):
        asserts(
            assert_data=payments.update({
                "token": AUTH_DATA_LENGTH_TOKEN,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('update-fail-bad-requst-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для update с отрицательным идентификатором платежа')
    def test_update_bad_request_id_minus(self, payments, create_admin):
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": 1,
                "id": AUTH_DATA_FAIL_BAD_ID,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": create_admin['id']
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для update с символами в идентификаторе платежа')
    def test_update_bad_request_id_varchar(self, payments, create_admin):
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": 1,
                "id": 'text',
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": create_admin['id']
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request user id для update с отрицательным идентификатором пользователя')
    def test_update_bad_request_user_id_minus(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request user id для update с символами в идентификаторе пользователя')
    def test_update_bad_request_user_id_varchar(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-vendor-id-minus')
    @description('Проверка ошибки Bad Request vendor id для update с отрицательным идентификатором поставщика')
    def test_update_bad_request_vendor_id_minus(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": AUTH_DATA_FAIL_BAD_ID,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-vendor-id-varchar')
    @description('Проверка ошибки Bad Request vendor id для update с символами в идентификаторе поставщика')
    def test_update_bad_request_vendor_id_varchar(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 'text',
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-legal-entity-id-minus')
    @description(
        'Проверка ошибки Bad Request legal entity id для update с отрицательным идентификатором юридического лица')
    def test_update_bad_request_legal_entity_id_minus(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": AUTH_DATA_FAIL_BAD_ID,
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-legal-entity-id-varchar')
    @description(
        'Проверка ошибки Bad Request legal entity id для update с символами в идентификаторе юридического лица')
    def test_update_bad_request_legal_entity_id_varchar(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 'text',
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-amount-minus')
    @description(
        'Проверка ошибки Bad Request amount для update с отрицательным значением в сумме платежа')
    def test_update_bad_request_amount_minus(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": AUTH_DATA_FAIL_BAD_ID,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('update-fail-bad-requst-amount-varchar')
    @description(
        'Проверка ошибки Bad Request amount для update с символами в сумме платежа')
    def test_update_bad_request_amount_varchar(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 'text',
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('update-fail-bad-requst-amount-zero')
    @description(
        'Проверка ошибки Bad Request amount для update с нулевым значением в сумме платежа')
    def test_update_bad_request_amount_zero(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 0,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('update-fail-bad-requst-amount-length')
    @description('Проверка ошибки Bad Request amount length для update')
    def test_update_bad_request_amount_length(self, payments):
        asserts(
            assert_data=payments.update({
                "token": 1,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": DATA_AMOUNT_PAYMENTS_BAD,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD
        )

    @title('update-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update')
    def test_update_not_found_token(self, payments):
        asserts(
            assert_data=payments.update({
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "vendor_id": 1,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-fail-not-found-vendor')
    @description('Проверка ошибки Not Found vendor для update')
    def test_update_not_found_vendor(self, payments, create_admin):
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "id": 1,
                "legal_entity_id": 1,
                "amount": 1,
                "created_at": 1,
                "user_id": create_admin['id']
            }),
            data=API_NOT_FOUND_VENDORS
        )

    @title('update-fail-not-found-legal-entity')
    @description('Проверка ошибки Not Found legal entity для update')
    def test_update_not_found_legal_entity(self, payments, create_admin, create_vendors_remove):
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": create_vendors_remove,
                "id": 1,
                "legal_entity_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "amount": 1,
                "created_at": 1,
                "user_id": create_admin['id']
            }),
            data=API_NOT_FOUND_PAYMENT_LEGAL_ENTITIES
        )

    @title('update-fail-not-found-payment')
    @description('Проверка ошибки Not Found payment для update')
    def test_update_not_found_payment(self, payments, create_admin, create_vendors_remove,
                                      create_legal_entities_remove):
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": create_vendors_remove,
                "id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "legal_entity_id": create_legal_entities_remove,
                "amount": 1,
                "created_at": 1,
                "user_id": create_admin['id']
            }),
            data=API_NOT_FOUND_PAYMENT
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для update')
    def test_update_bad_request_bad_token_and_id(self, payments, create_admin, create_payment_remove,
                                                 create_vendors_remove, create_legal_entities_remove):
        asserts(
            assert_data=payments.update({
                "token": create_admin['token'],
                "vendor_id": create_vendors_remove,
                "id": create_payment_remove,
                "legal_entity_id": create_legal_entities_remove,
                "amount": 1,
                "created_at": 1,
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
