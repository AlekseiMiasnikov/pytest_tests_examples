from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_MATERIAL_CREATE, NAME_MATERIAL_TYPES_CREATE, API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, API_BAD_REQUEST_EMPTY_MATERIALS, \
    AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES, API_BAD_REQUEST_LENGTH_MATERIALS, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_ID, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_NOT_FOUND_MATERIAL_TYPES_ID, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS, API_BAD_REQUEST_MATERIAL_ALLREDY_EXIST


@suite('Контроллер: Materials. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiMaterialCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, create_admin, materials, create_and_remove_material_type, remove_materials):
        name = NAME_MATERIAL_TYPES_CREATE()
        asserts(
            assert_data=materials.create({
                'token': create_admin['token'],
                'type_id': create_and_remove_material_type,
                'name': name,
                'user_id': create_admin['id']
            }),
            data=API_MATERIAL_CREATE
        )
        remove_materials(name)

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, materials):
        asserts(
            assert_data=materials.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, materials):
        asserts(
            assert_data=materials.create({
                'token': '',
                'name': NAME_MATERIAL_TYPES_CREATE()
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, materials):
        asserts(
            assert_data=materials.create({
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'token': AUTH_DATA_LENGTH_TOKEN
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-empty-materials')
    @description('Проверка ошибки Bad Request empty materials для create')
    def test_create_bad_request_empty_materials(self, materials):
        asserts(
            assert_data=materials.create({
                'name': '',
                'token': 1
            }),
            data=API_BAD_REQUEST_EMPTY_MATERIALS
        )

    @title('create-fail-bad-requst-length-materials')
    @description('Проверка ошибки Bad Request length materials для create')
    def test_create_bad_request_length_materials(self, materials):
        asserts(
            assert_data=materials.create({
                'name': AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES,
                'token': 1
            }),
            data=API_BAD_REQUEST_LENGTH_MATERIALS
        )

    @title('create-fail-bad-requst-bad-id-user-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором пользователя')
    def test_create_bad_request_bad_id_user_id_minus(self, materials):
        asserts(
            assert_data=materials.create({
                'token': 1,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'type_id': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-id-user-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в идентификаторе пользователя')
    def test_create_bad_request_bad_id_user_id_varchar(self, materials):
        asserts(
            assert_data=materials.create({
                'token': 1,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'type_id': 1,
                'user_id': 'text'
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-id-type-id-minus')
    @description('Проверка ошибки Bad Request bad id для create с отрицательным идентификатором типа материала')
    def test_create_bad_request_bad_id_type_id_minus(self, materials):
        asserts(
            assert_data=materials.create({
                'token': 1,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'type_id': AUTH_DATA_FAIL_BAD_ID,
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-bad-id-type-id-varchar')
    @description('Проверка ошибки Bad Request bad id для create с символами в идентификаторе типа материала')
    def test_create_bad_request_bad_id_type_id_varchar(self, materials):
        asserts(
            assert_data=materials.create({
                'token': 1,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'type_id': 'text',
                'user_id': 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_not_found_token(self, materials, create_and_remove_material_type):
        asserts(
            assert_data=materials.create({
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'type_id': create_and_remove_material_type,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'user_id': 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-not-found-material-types')
    @description('Проверка ошибки Not Found material types для create')
    def test_create_not_found_material_types(self, create_admin, materials):
        asserts(
            assert_data=materials.create({
                'token': create_admin['token'],
                'type_id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'user_id': create_admin['id']
            }),
            data=API_NOT_FOUND_MATERIAL_TYPES_ID
        )

    @title('create-fail-bad-request-allredy-exist')
    @description('Проверка ошибки Bad Request allredy exist для create')
    def test_create_bad_request_allredy_exist(self, materials, materials_name_allready_exist):
        asserts(
            assert_data=materials.create({
                'token': materials_name_allready_exist['token'],
                'type_id': materials_name_allready_exist['type_id'],
                'name': materials_name_allready_exist['name'],
                'user_id': materials_name_allready_exist['user_id']
            }),
            data=API_BAD_REQUEST_MATERIAL_ALLREDY_EXIST
        )

    @title('create-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для create')
    def test_create_bad_request_bad_token_and_id(self, materials, create_and_remove_material_type,
                                                 create_login_delete_user):
        asserts(
            assert_data=materials.create({
                'token': create_login_delete_user['token'],
                'type_id': create_and_remove_material_type,
                'name': NAME_MATERIAL_TYPES_CREATE(),
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
