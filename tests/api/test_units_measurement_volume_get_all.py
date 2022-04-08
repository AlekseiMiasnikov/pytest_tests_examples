from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import DATA_UNITS_MEASUREMENT_VOLUME_GET_ALL, API_GET_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS


@suite('Контроллер: UnitsMeasurementVolume. Метод: get-all')
@parent_suite('[PYTHON][API]')
class TestApiUnitsMeasurementVolumeGetAll:
    @title('get-all')
    @description('Проверка корректной работы get-all')
    def test_get_all(self, create_admin, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': create_admin['token'],
                'user_id': create_admin['id']
            }),
            data=DATA_UNITS_MEASUREMENT_VOLUME_GET_ALL
        )

    @title('get-all-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для get-all')
    def test_get_all_method_not_allowed(self, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all_method_not_allowed(),
            data=API_GET_METHOD_NOT_ALLOWED
        )

    @title('get-all-fail-bad-request-token-empty')
    @description('Проверка ошибки Bad Request empty token для get-all')
    def test_get_all_bad_request_empty_token(self, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': '',
                'user_id': 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('get-all-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для get-all')
    def test_get_all_bad_request_length_token(self, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('get-all-fail-bad-request-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для get-all с отрицательным числом для идентификатора')
    def test_get_all_bad_request_bad_id_minus(self, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-bad-request-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для get-all с символами в идентификаторе')
    def test_get_all_bad_request_bad_id_varchar(self, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': 1,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('get-all-fail-not-found-user-bad-token')
    @description('Проверка ошибки Not Found user bad token для get-all')
    def test_get_all_not_found_empty_token(self, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('get-all-fail-bad_request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для get-all')
    def test_get_all_bad_request_bad_rights(self, create_login_delete_user, units_measurement_volume):
        asserts(
            assert_data=units_measurement_volume.get_all({
                'token': create_login_delete_user['token'],
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
