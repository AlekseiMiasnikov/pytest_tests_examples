from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_SUCCESS, API_PUT_METHOD_NOT_ALLOWED, \
    API_AUTH_TOKEN_EMPTY, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_MATERIAL_TYPES, \
    API_BAD_REQUEST_LENGTH_MATERIAL_TYPES, AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_ID, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_NOT_FOUND_MATERIAL_TYPES_ID, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS, NAME_MATERIAL_TYPES_CREATE, DATA_UNITS_MEASUREMENT_VOLUME_ID, \
    API_BAD_UNITS_MEASUREMENT_ID


@suite('Контроллер: MaterialTypes. Метод: update')
@parent_suite('[PYTHON][API]')
class TestApiMaterialTypesUpdate:
    @title('update')
    @description('Проверка корректной работы update')
    def test_update(self, material_types, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_USERS_SUCCESS
        )

    @title('update-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для update')
    def test_update_method_not_allowed(self, material_types):
        asserts(
            assert_data=material_types.update_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для update')
    def test_update_bad_request_empty_token(self, material_types, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": '',
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('update-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для update')
    def test_update_bad_request_length_token(self, material_types, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('update-fail-bad-requst-empty-material-types')
    @description('Проверка ошибки Bad Request empty material types для update')
    def test_update_bad_request_empty_material_types(
            self, material_types, create_admin, create_and_remove_material_type
    ):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": '',
                "user_id": create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_REQUEST_EMPTY_MATERIAL_TYPES
        )

    @title('update-fail-bad-requst-length-material-types')
    @description('Проверка ошибки Bad Request length material types для update')
    def test_update_bad_request_length_material_types(
            self, material_types, create_admin, create_and_remove_material_type
    ):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES,
                "user_id": create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_REQUEST_LENGTH_MATERIAL_TYPES
        )

    @title('update-fail-bad-requst-bad-id-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для update с отрицательным идентификатором')
    def test_update_bad_request_length_bad_id_user_id_minus(self, material_types, create_admin):
        asserts(
            assert_data=material_types.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": AUTH_DATA_FAIL_BAD_ID,
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-user-id-varchar')
    @description('Проверка ошибки Bad Request bad id для update с символами в идентификаторе')
    def test_update_bad_request_length_bad_id_varchar(self, material_types, create_admin):
        asserts(
            assert_data=material_types.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 'text',
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-units-minus')
    @description('Проверка ошибки Bad Request bad id для update с отрицательным значением в величине объема')
    def test_update_bad_request_length_bad_id_units_minus(self, material_types, create_admin):
        asserts(
            assert_data=material_types.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-units-varchar')
    @description('Проверка ошибки Bad Request bad id для update с символами в величине объема')
    def test_update_bad_request_length_bad_id_units_varchar(self, material_types, create_admin):
        asserts(
            assert_data=material_types.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update')
    def test_update_not_found_token(self, material_types, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-fail-not-found-material-types-id')
    @description('Проверка ошибки Not Found material types id для update')
    def test_update_not_found_material_types_id(self, material_types, create_admin):
        asserts(
            assert_data=material_types.update({
                "id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_NOT_FOUND_MATERIAL_TYPES_ID
        )

    @title('update-fail-not-found-units-measurement-id')
    @description('Проверка ошибки Not Found units measurement id для update')
    def test_update_not_found_units_measurement_id(self, material_types, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id'],
                'units_measurement_volume_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_UNITS_MEASUREMENT_ID
        )

    @title('update-fail-bad-requst-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для update')
    def test_update_bad_request_bad_rights(self, material_types, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=material_types.update({
                "id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_RIGHTS
        )
