from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_SUCCESS, NAME_MATERIAL_TYPES_CREATE, API_PUT_METHOD_NOT_ALLOWED, \
    API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS, AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_ID, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, API_NOT_FOUND_MATERIAL_TYPES_ID, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_RIGHTS, API_NOT_FOUND_MATERIAL_ID


@suite('Контроллер: Materials Метод: update')
@parent_suite('[PYTHON][API]')
class TestApiMaterialTypesUpdate:
    @title('update')
    @description('Проверка корректной работы update')
    def test_update(self, materials, create_admin, create_and_remove_material_type,
                    create_material_type_materials_remove):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id']
            }),
            data=API_USERS_SUCCESS
        )

    @title('update-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для update')
    def test_update_method_not_allowed(self, materials):
        asserts(
            assert_data=materials.update_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для update')
    def test_update_bad_request_empty_token(self, materials, create_material_type_materials_remove,
                                            create_and_remove_material_type):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": create_and_remove_material_type,
                "token": '',
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('update-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для update')
    def test_update_bad_request_length_token(self, materials, create_and_remove_material_type,
                                             create_material_type_materials_remove):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": create_and_remove_material_type,
                "token": AUTH_DATA_LENGTH_TOKEN,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('update-fail-bad-requst-length-name')
    @description('Проверка ошибки Bad Request length name для update')
    def test_update_bad_request_length_name(self, materials, create_and_remove_material_type,
                                            create_material_type_materials_remove):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": create_and_remove_material_type,
                "token": 1,
                "name": AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES,
                "user_id": 1
            }),
            data=API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS
        )

    @title('update-fail-bad-requst-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для update с отрицательным идентификатором')
    def test_update_bad_request_length_bad_id_minus(self, materials):
        asserts(
            assert_data=materials.update({
                "id": AUTH_DATA_FAIL_BAD_ID,
                "type_id": 1,
                "token": 1,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для update с символами в идентификаторе')
    def test_update_bad_request_length_bad_id_varchar(self, materials):
        asserts(
            assert_data=materials.update({
                "id": 'text',
                "type_id": 1,
                "token": 1,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-type-id-minus')
    @description('Проверка ошибки Bad Request bad id для update с отрицательным идентификатором в типе материала')
    def test_update_bad_request_length_bad_id_type_id_minus(self, materials):
        asserts(
            assert_data=materials.update({
                "id": 1,
                "type_id": AUTH_DATA_FAIL_BAD_ID,
                "token": 1,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-bad-requst-bad-id-type-id-varchar')
    @description('Проверка ошибки Bad Request bad id для update с символами в идентификаторе типа материала')
    def test_update_bad_request_length_bad_id_type_id_varchar(self, materials):
        asserts(
            assert_data=materials.update({
                "id": 1,
                "type_id": 'text',
                "token": 1,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update')
    def test_update_not_found_token(self, materials, create_and_remove_material_type,
                                    create_material_type_materials_remove):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": create_and_remove_material_type,
                "token": AUTH_DATA_FAIL_BAD_TOKEN,
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": 1
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-fail-not-found-material-types-id')
    @description('Проверка ошибки Not Found material types id для update')
    def test_update_not_found_material_types_id(self, materials, create_admin, create_material_type_materials_remove):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id']
            }),
            data=API_NOT_FOUND_MATERIAL_TYPES_ID
        )

    @title('update-fail-not-found-material-id')
    @description('Проверка ошибки Not Found material id для update')
    def test_update_not_found_material_id(self, materials, create_admin, create_and_remove_material_type):
        asserts(
            assert_data=materials.update({
                "id": AUTH_DATA_FAIL_NOT_FOUND_ID,
                "type_id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": create_admin['id']
            }),
            data=API_NOT_FOUND_MATERIAL_ID
        )

    @title('update-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad token and id для update')
    def test_update_bad_request_bad_token_and_id(self, materials, create_admin, create_and_remove_material_type,
                                                 create_material_type_materials_remove):
        asserts(
            assert_data=materials.update({
                "id": create_material_type_materials_remove,
                "type_id": create_and_remove_material_type,
                "token": create_admin['token'],
                "name": NAME_MATERIAL_TYPES_CREATE(),
                "user_id": AUTH_DATA_FAIL_NOT_FOUND_ID
            }),
            data=API_BAD_RIGHTS
        )
