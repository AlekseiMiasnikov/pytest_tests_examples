from allure import title, description, suite, parent_suite

from data import API_GET_DEBT_OFF, API_GET_DEBT_ON, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Settings. Метод: get-debt')
@parent_suite('[PYTHON][API]')
class TestApiSettingsGetDebt:
    @title('get-debt-off')
    @description('Проверка корректной работы get-debt с включенным долгом на конец года')
    def test_get_debt_off(self, create_admin, settings):
        asserts(
            assert_data=settings.get_debt({
                'token': create_admin['token'],
                'user_id': create_admin['id']
            }),
            data=API_GET_DEBT_ON
        )

    @title('get-debt-on')
    @description('Проверка корректной работы get-debt с выключенным долгом на конец года')
    def test_get_debt_on(self, create_admin, settings):
        admin_token = create_admin['token']
        admin_user_id = create_admin['id']
        settings.set_debt({
            'token': admin_token,
            'active': 0,
            'user_id': admin_user_id
        })
        asserts(
            assert_data=settings.get_debt({
                'token': admin_token,
                'user_id': admin_user_id
            }),
            data=API_GET_DEBT_OFF
        )

    @title('get-debt-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-debt')
    def test_get_debt_method_not_allowed(self, settings):
        asserts(
            assert_data=settings.get_debt_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-debt-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-debt')
    def test_get_debt_bad_request_empty_token(self, settings):
        asserts(
            assert_data=settings.get_debt({
                'token': '',
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-debt-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-debt')
    def test_get_debt_bad_request_length_token(self, settings):
        asserts(
            assert_data=settings.get_debt({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-debt-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-debt')
    def test_get_debt_not_found_empty_token(self, settings):
        asserts(
            assert_data=settings.get_debt({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-debt-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-debt')
    def test_get_debt_bad_request_bad_rights(self, create_login_delete_user, settings):
        asserts(
            assert_data=settings.get_debt({
                'token': create_login_delete_user['token'],
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
