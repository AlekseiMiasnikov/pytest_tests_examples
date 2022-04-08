from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import API_USERS_SUCCESS, AUTH_CREATE, API_PUT_METHOD_NOT_ALLOWED, API_AUTH_BAD_REQUEST, \
    AUTH_DATA_FAIL_EMPTY_FIELDS, API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_UPDATE_INFO_LENGTH_TOKEN, \
    API_AUTH_BAD_REQUEST_LENGTH_LOGIN, AUTH_DATA_UPDATE_INFO_LENGTH_LOGIN, API_BAD_REQUEST_LENGTH_EMAIL, \
    AUTH_DATA_UPDATE_INFO_LENGTH_EMAIL, AUTH_DATA_UPDATE_INFO_LENGTH_PASSWORD, API_AUTH_BAD_REQUEST_LENGTH_PASSWORD, \
    API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_UPDATE_INFO_NOT_FOUND_TOKEN, API_BAD_REQUEST_BAD_ID, \
    AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_ID, API_NOT_FOUND_ID, AUTH_DATA_UPDATE_INFO_NOT_FOUND_ID, \
    API_BAD_REQUEST_BAD_EMAIL, AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_EMAIL, API_BAD_REQUEST_BAD_PASSWORD, \
    AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_PASSWORD, API_BAD_RIGHTS, AUTH_DATA_FAIL_BAD_TOKEN


@suite('Контроллер: Users. Метод: update-info')
@parent_suite('[PYTHON][API]')
class TestApiUsersUpdateInfo:
    @title('update-info')
    @description('Проверка корректной работы update-info')
    def test_update_info(self, users, create_user_token_admin_id_user_delete):
        data = AUTH_CREATE()
        response = users.update_info({
            **data,
            'id': create_user_token_admin_id_user_delete['id'],
            'token': create_user_token_admin_id_user_delete['token'],
            'user_id': create_user_token_admin_id_user_delete['user_id']
        })
        asserts(
            assert_data=response,
            data=API_USERS_SUCCESS
        )
        assert response['data']['id'] == create_user_token_admin_id_user_delete['id']
        assert response['data']['login'] == data['login']
        assert response['data']['email'] == data['email']

    @title('update-info-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для update-info')
    def test_update_info_method_now_allowed(self, users):
        asserts(
            assert_data=users.update_info_method_not_allowed(),
            data=API_PUT_METHOD_NOT_ALLOWED
        )

    @title('update-info-fail-bad-request-empty-fields-login')
    @description('Проверка ошибки Bad Requst empty fields для update-info c пустым логином')
    def test_update_info_bad_request_empty_fields_login(self, users):
        asserts(
            assert_data=users.update_info(data={
                'login': '',
                'email': AUTH_DATA_FAIL_BAD_TOKEN,
                'password': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': 1,
                'user_id': 1,
                'id': 1
            }),
            data=API_AUTH_BAD_REQUEST
        )

    # @title('update-info-fail-bad-request-empty-fields-password')
    # @description('Проверка ошибки Bad Requst empty fields для update-info с пустым паролем')
    # def test_update_info_bad_request_empty_fields_password(self, users, create_user_token_admin_id_user_delete):
    #     asserts(
    #         assert_data=users.update_info(data={
    #             'login': 'admin',
    #             'email': AUTH_DATA_FAIL_BAD_TOKEN,
    #             'password': '',
    #             'token': create_user_token_admin_id_user_delete['token'],
    #             'user_id': create_user_token_admin_id_user_delete['user_id'],
    #             'id': create_user_token_admin_id_user_delete['id']
    #         }),
    #         data=API_AUTH_BAD_REQUEST
    #     )

    @title('update-info-fail-bad-request-empty-fields-email')
    @description('Проверка ошибки Bad Requst empty fields для update-info c пустой почтой')
    def test_update_info_bad_request_empty_fields_email(self, users):
        asserts(
            assert_data=users.update_info(data={
                'login': AUTH_DATA_FAIL_BAD_TOKEN,
                'email': '',
                'password': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': 1,
                'user_id': 1,
                'id': 1
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('update-info-fail-bad-request-empty-fields-token')
    @description('Проверка ошибки Bad Requst empty fields для update-info с пустым токеном')
    def test_update_info_bad_request_empty_fields_token(self, users):
        asserts(
            assert_data=users.update_info(data={
                'login': AUTH_DATA_FAIL_BAD_TOKEN,
                'email': AUTH_DATA_FAIL_BAD_TOKEN,
                'password': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': '',
                'user_id': 1,
                'id': 1
            }),
            data=API_AUTH_BAD_REQUEST
        )

    @title('update-info-fail-bad-request-empty-fields-all')
    @description('Проверка ошибки Bad Requst empty fields для update-info со всеми пустыми полями')
    def test_update_info_bad_request_empty_fields(self, users):
        asserts(
            assert_data=users.update_info(AUTH_DATA_FAIL_EMPTY_FIELDS),
            data=API_AUTH_BAD_REQUEST
        )

    @title('update-info-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Requst length token для update-info')
    def test_update_info_bad_request_length_token(self, users):
        asserts(
            assert_data=users.update_info(AUTH_DATA_UPDATE_INFO_LENGTH_TOKEN),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('update-info-fail-bad-request-length-login')
    @description('Проверка ошибки Bad Requst length login для update-info')
    def test_update_info_bad_request_length_login(self, users):
        asserts(
            assert_data=users.update_info(AUTH_DATA_UPDATE_INFO_LENGTH_LOGIN),
            data=API_AUTH_BAD_REQUEST_LENGTH_LOGIN
        )

    @title('update-info-fail-bad-request-length-email')
    @description('Проверка ошибки Bad Requst length email для update-info')
    def test_update_info_bad_request_length_email(self, users):
        asserts(
            assert_data=users.update_info(AUTH_DATA_UPDATE_INFO_LENGTH_EMAIL),
            data=API_BAD_REQUEST_LENGTH_EMAIL
        )

    @title('update-info-fail-bad-request-length-password')
    @description('Проверка ошибки Bad Requst length password для update-info')
    def test_update_info_bad_request_length_password(self, users):
        asserts(
            assert_data=users.update_info(AUTH_DATA_UPDATE_INFO_LENGTH_PASSWORD),
            data=API_AUTH_BAD_REQUEST_LENGTH_PASSWORD
        )

    @title('update-info-fail-not-found-token')
    @description('Проверка ошибки Not Found token для update-info')
    def test_update_info_not_found_token(self, users):
        asserts(
            assert_data=users.update_info(AUTH_DATA_UPDATE_INFO_NOT_FOUND_TOKEN),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('update-info-fail-bad-request-bad-id-minus')
    @description('Проверка ошибки Bad Request bad id для update-info с отрицательным индентификатором')
    def test_update_info_bad_request_bad_id_minus(self, users):
        asserts(
            assert_data=users.update_info({
                **AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_ID,

            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-info-fail-bad-request-bad-id-varchar')
    @description('Проверка ошибки Bad Request bad id для update-info с симвовалми в индентификаторе')
    def test_update_info_bad_request_bad_id_varhchar(self, users):
        asserts(
            assert_data=users.update_info(data={
                'id': 'text',
                **AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('update-info-fail-not-id')
    @description('Проверка ошибки Not Found id для update-info')
    def test_update_info_not_found_id(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.update_info({
                **AUTH_DATA_UPDATE_INFO_NOT_FOUND_ID,
                'token': create_user_token_admin_id_user_delete['token']
            }),
            data=API_NOT_FOUND_ID
        )

    @title('update-info-fail-bad-request-bad-email')
    @description('Проверка ошибки Bad Request bad email для update-info')
    def test_update_info_bad_request_bad_email(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.update_info({
                **AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_EMAIL,
                'token': create_user_token_admin_id_user_delete['token']
            }),
            data=API_BAD_REQUEST_BAD_EMAIL
        )

    @title('update-info-fail-bad-request-bad-password')
    @description('Проверка ошибки Bad Request bad password для update-info')
    def test_update_info_bad_request_bad_password(self, users, create_user_token_admin_id_user_delete):
        asserts(
            assert_data=users.update_info({
                **AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_PASSWORD,
                'token': create_user_token_admin_id_user_delete['token'],
                'user_id': create_user_token_admin_id_user_delete['user_id'],
            }),
            data=API_BAD_REQUEST_BAD_PASSWORD
        )

    @title('update-info-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для update-info')
    def test_update_info_bad_request_bad_rights(self, users, create_login_delete_user):
        asserts(
            assert_data=users.update_info({
                **AUTH_CREATE(),
                'id': create_login_delete_user['id'],
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['user_id'],
            }),
            data=API_BAD_RIGHTS
        )
