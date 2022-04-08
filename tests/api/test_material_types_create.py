from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_MATERIAL_TYPES_CREATE, API_POST_METHOD_NOT_ALLOWED, \
    API_AUTH_TOKEN_EMPTY, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_MATERIAL_TYPES, \
    API_BAD_REQUEST_LENGTH_MATERIAL_TYPES, AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES, API_AUTH_NOT_FOUND_TOKEN, \
    AUTH_DATA_FAIL_BAD_TOKEN, NAME_MATERIAL_TYPES_CREATE, API_BAD_REQUEST_MATERIAL_TYPES_ALLREDY_EXIST, \
    API_BAD_RIGHTS, AUTH_DATA_FAIL_NOT_FOUND_ID, DATA_UNITS_MEASUREMENT_VOLUME_ID, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_ID, API_BAD_UNITS_MEASUREMENT_ID


@suite('Контроллер: MaterialTypes. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiMaterialTypesCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, create_admin, material_types, remove_material_type):
        name = NAME_MATERIAL_TYPES_CREATE()
        asserts(
            assert_data=material_types.create({
                'name': name,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_MATERIAL_TYPES_CREATE
        )
        remove_material_type(name)

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, material_types):
        asserts(
            assert_data=material_types.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': ''
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': AUTH_DATA_LENGTH_TOKEN
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-material-types')
    @description('Проверка ошибки Bad Request empty material types для create')
    def test_create_bad_request_empty_material_types(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': '',
                'token': create_admin['token']
            }),
            data=API_BAD_REQUEST_EMPTY_MATERIAL_TYPES
        )

    @title('create-fail-bad-requst-length-material-types')
    @description('Проверка ошибки Bad Request length material types для create')
    def test_create_bad_request_length_material_types(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES,
                'token': create_admin['token']
            }),
            data=API_BAD_REQUEST_LENGTH_MATERIAL_TYPES
        )

    @title('create-fail-bad-requst-length-bad-id-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором')
    def test_create_bad_request_bad_id_user_id_minus(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': create_admin['token'],
                'user_id': AUTH_DATA_FAIL_BAD_ID,
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-length-bad-id-user-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в идентификаторе')
    def test_create_bad_request_bad_id_user_id_varchar(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': create_admin['token'],
                'user_id': AUTH_DATA_FAIL_BAD_ID,
                'units_measurement_volume_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-length-bad-id-units-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательной величиной объема')
    def test_create_bad_request_bad_id_units_minus(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'units_measurement_volume_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-length-bad-id-units-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в величине объема')
    def test_create_bad_request_bad_id_units_varchar(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'units_measurement_volume_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_not_found_token(self, create_admin, material_types):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_admin['id'],
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-bad-request-material-types-allready-exist')
    @description('Проверка ошибки Bad Request material types allready exist для create')
    def test_create_bad_request_material_types_allready_exist(self, material_types, material_types_name_allready_exist):
        asserts(
            assert_data=material_types.create({
                'name': material_types_name_allready_exist['name'],
                'token': material_types_name_allready_exist['token'],
                'user_id': material_types_name_allready_exist['user_id'],
                'units_measurement_volume_id': material_types_name_allready_exist['units_measurement_volume_id']
            }),
            data=API_BAD_REQUEST_MATERIAL_TYPES_ALLREDY_EXIST
        )

    @title('create-fail-not-found-bad-units')
    @description('Проверка ошибки Bad Request bad units для create')
    def test_create_not_found_bad_units_measurement(self, material_types, create_login_delete_user):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['id'],
                'units_measurement_volume_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_UNITS_MEASUREMENT_ID
        )

    @title('create-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для create')
    def test_create_bad_request_bad_token_and_id(self, material_types, create_login_delete_user):
        asserts(
            assert_data=material_types.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': create_login_delete_user['token'],
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
            }),
            data=API_BAD_RIGHTS
        )
