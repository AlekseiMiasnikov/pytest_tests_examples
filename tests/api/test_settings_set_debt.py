from allure import title, description, suite, parent_suite

from data import API_SET_DEBT_OFF, API_SET_DEBT_ON, API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    API_BAD_REQUEST_SETTINGS_BAD_ACTIVE, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_SET_DEBT_ALLREDY_OFF, \
    API_SET_DEBT_ALLREDY_ON, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Settings. Метод: set-debt')
@parent_suite('[PYTHON][API]')
class TestApiSettingsSetDebt:
    @title('set-debt-off')
    @description('Проверка корректной работы set-debt с выключением долга на конец года')
    def test_set_debt_off(self, create_admin, settings, active_settings):
        asserts(
            assert_data=settings.set_debt({
                'token': create_admin['token'],
                'active': 0,
                'user_id': create_admin['id']
            }),
            data=API_SET_DEBT_OFF
        )

    @title('set-debt-on')
    @description('Проверка корректной работы set-debt с включением долга на конец года')
    def test_set_debt_on(self, create_admin, settings, disable_settings):
        asserts(
            assert_data=settings.set_debt({
                'token': create_admin['token'],
                'active': 1,
                'user_id': create_admin['id']
            }),
            data=API_SET_DEBT_ON
        )

    @title('set-debt-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для set-debt')
    def test_set_debt_method_not_allowed(self, settings):
        asserts(
            assert_data=settings.set_debt_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('set-debt-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для set-debt')
    def test_set_debt_bad_request_empty_token(self, settings):
        asserts(
            assert_data=settings.set_debt({
                'token': '',
                'active': 0,
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('set-debt-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для set-debt')
    def test_set_debt_bad_request_length_token(self, settings):
        asserts(
            assert_data=settings.set_debt({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'active': 0,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('set-debt-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id для set-debt с отрицательным числом в идентификаторе пользователя')
    def test_set_debt_bad_request_user_id_minus(self, settings):
        asserts(
            assert_data=settings.set_debt({
                'token': 1,
                'active': 0,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('set-debt-fail-bad-request-user-id-varchar')
    @description(
        'Проверка ошибки Bad Request user id для set-debt с символами в идентификаторе пользователя')
    def test_set_debt_bad_request_user_id_varchar(self, settings):
        asserts(
            assert_data=settings.set_debt({
                'token': 1,
                'active': 0,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('set-debt-fail-bad-request-bad-active')
    @description('Проверка ошибки Bad Request bad active для set-debt')
    def test_set_debt_bad_request_bad_active(self, settings):
        asserts(
            assert_data=settings.set_debt({
                'token': 1,
                'active': 2,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_SETTINGS_BAD_ACTIVE
        )

    @title('set-debt-fail-not-found-token')
    @description('Проверка ошибки Not Found token для set-debt')
    def test_set_debt_not_found_token(self, settings):
        asserts(
            assert_data=settings.set_debt({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'active': 0,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('set-debt-fail-bad-request-allredy-off')
    @description('Проверка ошибки Bad Request allredy off для set-debt')
    def test_set_debt_allredy_off(self, create_admin, settings, disable_settings):
        asserts(
            assert_data=settings.set_debt({
                'token': create_admin['token'],
                'active': 0,
                'user_id': create_admin['id']
            }),
            data=API_SET_DEBT_ALLREDY_OFF
        )

    @title('set-debt-fail-bad-request-allredy-on')
    @description('Проверка ошибки Bad Request allredy on для set-debt')
    def test_set_debt_allredy_on(self, create_admin, settings, active_settings):
        asserts(
            assert_data=settings.set_debt({
                'token': create_admin['token'],
                'active': 1,
                'user_id': create_admin['id']
            }),
            data=API_SET_DEBT_ALLREDY_ON
        )

    @title('set-debt-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для set-debt')
    def test_set_debt_bad_request_bad_rights(self, create_login_delete_user, settings, disable_settings):
        asserts(
            assert_data=settings.set_debt({
                'token': create_login_delete_user['token'],
                'active': 1,
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
