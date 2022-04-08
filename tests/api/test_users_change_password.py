from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_CHANGE_PASSWORD, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_BAD_REQUEST, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_LENGTH_TOKEN, AUTH_DATA_FAIL_LENGTH_PASSWORD_ADMIN, \
    API_AUTH_BAD_REQUEST_LENGTH_PASSWORD, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_FAIL_BAD_ID, API_NOT_FOUND_ID, AUTH_DATA_FAIL_NOT_FOUND_ID, API_BAD_REQUEST_BAD_PASSWORD, \
    AUTH_DATA_FAIL_BAD_PASSWORD, API_BAD_RIGHTS


@suite('Контроллер: Users. Метод: change-password')
@parent_suite('[PYTHON][API]')
class TestApiUsersChangePassword:
    @title('change-password')
    @description('Проверка корректной работы change-password')
    def test_change_password(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': create_user_token_admin_id_user_delete['id'],
                'password': create_user_token_admin_id_user_delete['password'],
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_CHANGE_PASSWORD
        )

    @title('change-password-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для change-password')
    def test_change_password_method_now_allowed(self, users):
        asserts(
            assert_data=users.change_password_mehtod_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('change-password-fail-bad-request-empty-fields-token')
    @description('Проверка ошибки Bad Request empty fields для change-password c пустым токеном')
    def test_change_password_bad_request_empty_fields_token(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password(data={
                'id': create_user_token_admin_id_user_delete['id'],
                'password': create_user_token_admin_id_user_delete['password'],
                'token': '',
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('change-password-fail-bad-request-empty-fields-password')
    @description('Проверка ошибки Bad Request empty fields для change-password с пустым паролем')
    def test_change_password_bad_request_empty_fields_password(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password(data={
                'id': create_user_token_admin_id_user_delete['id'],
                'password': '',
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('change-password-fail-bad-request-empty-fields-all')
    @description('Проверка ошибки Bad Request empty fields для change-password со всеми пустыми полями')
    def test_change_password_bad_request_empty_fields_all(self, users):
        asserts(
            assert_data=users.change_password(data={
                'id': '',
                'password': '',
                'token': '',
                'user_id': ''
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('change-password-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token для change-password')
    def test_change_password_bad_request_length_token(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': create_user_token_admin_id_user_delete['id'],
                'password': create_user_token_admin_id_user_delete['password'],
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('change-password-fail-bad-request-length-password')
    @description('Проверка ошибки Bad Request length password для change-password')
    def test_change_password_bad_request_length_password(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': create_user_token_admin_id_user_delete['id'],
                'password': AUTH_DATA_FAIL_LENGTH_PASSWORD_ADMIN['password'],
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_AUTH_BAD_REQUEST_LENGTH_PASSWORD
        )

    @title('change-password-bad-request-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для change-password с отрицательным индентификатором')
    def test_change_password_bad_request_bad_id_minus(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': AUTH_DATA_FAIL_BAD_ID,
                'password': create_user_token_admin_id_user_delete['password'],
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('change-password-bad-request-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для change-password с символвами в индетификаторе')
    def test_change_password_bad_request_bad_id_varchar(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': 'text',
                'password': create_user_token_admin_id_user_delete['password'],
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('change-password-fail-not-found_token')
    @description('Проверка ошибки Bad Not Found token для change-password')
    def test_change_password_not_found_token(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': create_user_token_admin_id_user_delete['id'],
                'password': create_user_token_admin_id_user_delete['password'],
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('change-password-not-found-id')
    @description('Проверка ошибки Not Found id для change-password')
    def test_change_password_not_found_id(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'password': create_user_token_admin_id_user_delete['password'],
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_NOT_FOUND_ID
        )

    @title('change-password-bad-request-bad-password')
    @description('Проверка ошибки Bad Request bad password для change-password')
    def test_change_password_bad_request_bad_password(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.change_password({
                'id': create_user_token_admin_id_user_delete['id'],
                'password': AUTH_DATA_FAIL_BAD_PASSWORD,
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id']
            }),
            data=API_BAD_REQUEST_BAD_PASSWORD
        )

    @title('change-password-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для change-password')
    def test_change_password_bad_request_bad_rights(self, users, create_login_delete_user):
        asserts(
            assert_data=users.change_password({
                'id': create_login_delete_user['id'],
                'password': create_login_delete_user['password'],
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['user_id']
            }),
            data=API_BAD_RIGHTS
        )
