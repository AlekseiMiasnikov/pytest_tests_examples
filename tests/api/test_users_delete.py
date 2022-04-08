from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_DELETE, API_DELETE_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, \
    AUTH_DATA_FAIL_EMPTY_TOKEN, AUTH_DATA_FAIL_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, \
    API_AUTH_NOT_FOUND_TOKEN, API_BAD_RIGHTS, AUTH_DATA_FAIL_BAD_TOKEN, API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_ID, API_BAD_REQUEST_ADMIN


@suite('Контроллер: Users. Метод: delete')
@parent_suite('[PYTHON][API]')
class TestApiUsersDelete:
    @title('delete')
    @description('Проверка корректной работы delete')
    def test_delete(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.delete({
                'id': create_user_token_admin_id_user_delete['id'],
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id'],
            }),
            data=API_USERS_DELETE
        )

    @title('delete-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для delete')
    def test_delete_method_not_allowed(self, users):
        asserts(
            assert_data=users.delete_method_not_allowed(),
            data=API_DELETE_METHOD_NOT_ALLOWED
        )

    @title('delete-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Requst empty token для delete')
    def test_delete_bad_request_empty_token(self, users):
        asserts(
            assert_data=users.delete(AUTH_DATA_FAIL_EMPTY_TOKEN),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('delete-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Requst length token для delete')
    def test_delete_bad_request_length_token(self, users):
        asserts(
            assert_data=users.delete(AUTH_DATA_FAIL_LENGTH_TOKEN),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('delete-fail-bad-request-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для delete с отрицательным числом в индентфикаторе')
    def test_delete_bad_requst_bad_id_minus(self, users, create_admin, create_login_delete_user):
        asserts(
            assert_data=users.delete({
                'id': AUTH_DATA_FAIL_BAD_ID,
                'token': create_admin
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-bad-request-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для delete с символвами в индентфикаторе')
    def test_delete_bad_requst_bad_id_varchar(self, users, create_admin, create_login_delete_user):
        asserts(
            assert_data=users.delete({
                'id': 'text',
                'token': create_admin
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('delete-fail-not-found-token')
    @description('Проверка ошибки Not Found token для delete')
    def test_delete_not_found_token(self, users, create_login_delete_user):
        asserts(
            assert_data=users.delete({
                'id': create_login_delete_user['id'],
                'token': AUTH_DATA_FAIL_BAD_TOKEN,
                'user_id': create_login_delete_user['user_id']
            }),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('delete-fail-not-found-id')
    @description('Проверка ошибки Not Found id для delete')
    def test_delete_not_found_id(self, users, create_admin, create_login_delete_user):
        asserts(
            assert_data=users.delete({
                'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                'token': create_admin['token'],
                'user_id': create_admin['id']
            }),
            data=API_NOT_FOUND_ID
        )

    @title('delete-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для delete')
    def test_delete_bad_requst_bad_rights(self, users, create_login_delete_user):
        asserts(
            assert_data=users.delete({
                'id': create_login_delete_user['id'],
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['user_id'],
            }),
            data=API_BAD_RIGHTS
        )

    @title('delete-fail-bad-request-admin')
    @description('Проверка ошибки Bad Request admin для delete')
    def test_delete_bad_request_admin(self, users, create_admin, create_login_delete_user):
        asserts(
            assert_data=users.delete({
                'id': 1,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_ADMIN
        )
