from allure import title, description, suite, parent_suite
from pages.api import asserts
from data import AUTH_CREATE, API_USERS_CREATE, API_POST_METHOD_NOT_ALLOWED, API_BAD_REQUEST_EMPTY_FIELDS, \
    AUTH_DATA_FAIL_EMPTY_FIELDS, AUTH_DATA_CREATE_FAIL_LENGTH_TOKEN, API_BAD_REQUEST_LENGTH_TOKEN, \
    AUTH_DATA_CREATE_FAIL_LENGTH_LOGIN, API_AUTH_BAD_REQUEST_LENGTH_LOGIN, AUTH_DATA_CREATE_FAIL_LENGTH_PASSWORD, \
    API_AUTH_BAD_REQUEST_LENGTH_PASSWORD, AUTH_DATA_CREATE_FAIL_LENGTH_EMAIL, API_BAD_REQUEST_LENGTH_EMAIL, \
    AUTH_DATA_CREATE_FAIL_NOT_FOUND_TOKEN, API_AUTH_NOT_FOUND_TOKEN, API_BAD_RIGHTS, \
    AUTH_CREATE_FAIL_BAD_EMAIL, API_BAD_REQUEST_BAD_EMAIL, AUTH_DATA_CREATE_FAIL_PASSWORD, \
    API_BAD_REQUEST_BAD_PASSWORD, API_BAD_REQUEST_BAD_BUSY_EMAIL_LOGIN, AUTH_DATA_CREATE_FAIL_BUSY_EMAIL_LOGIN, \
    API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_BAD_ID, API_NOT_ENOUGHT_RIGHTS, \
    AUTH_DATA_FAIL_NOT_FOUND_ID, AUTH_DATA_FAIL_BAD_TOKEN


@suite('Контроллер: Users. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiUsersCreate:
    @title('create')
    @description('Проверка корректной работы create')
    def test_create(self, users, create_admin, delete_user):
        response = users.create({
            **AUTH_CREATE(),
            'token': create_admin['token'],
            'user_id': create_admin['id']
        })
        asserts(
            assert_data=response,
            data=API_USERS_CREATE
        )
        delete_user(response['data']['id'])

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, users):
        asserts(
            assert_data=users.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-request-empty-fields')
    @description('Проверка ошибки Bad Request empty fields для create с пустым логином')
    def test_create_method_bad_request_empty_fields_login(self, users):
        asserts(
            assert_data=users.create(data={
                'login': AUTH_DATA_FAIL_EMPTY_FIELDS['login'],
                'email': AUTH_DATA_FAIL_BAD_TOKEN,
                'password': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': 1
            }),
            data=API_BAD_REQUEST_EMPTY_FIELDS
        )

    @title('create-fail-bad-request-empty-fields')
    @description('Проверка ошибки Bad Request empty fields для create с пустым паролем')
    def test_create_method_bad_request_empty_fields_password(self, users):
        asserts(
            assert_data=users.create(data={
                'login': AUTH_DATA_FAIL_BAD_TOKEN,
                'email': AUTH_DATA_FAIL_BAD_TOKEN,
                'password': AUTH_DATA_FAIL_EMPTY_FIELDS['password'],
                'token': 1
            }),
            data=API_BAD_REQUEST_EMPTY_FIELDS
        )

    @title('create-fail-bad-request-empty-fields')
    @description('Проверка ошибки Bad Request empty fields для create с пустой почтой')
    def test_create_method_bad_request_empty_fields_email(self, users):
        asserts(
            assert_data=users.create(data={
                'login': AUTH_DATA_FAIL_BAD_TOKEN,
                'email': AUTH_DATA_FAIL_EMPTY_FIELDS['email'],
                'password': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': 1
            }),
            data=API_BAD_REQUEST_EMPTY_FIELDS
        )

    @title('create-fail-bad-request-empty-fields')
    @description('Проверка ошибки Bad Request empty fields для create с пустым токеном')
    def test_create_method_bad_request_empty_fields_token(self, users):
        asserts(
            assert_data=users.create(data={
                'login': AUTH_DATA_FAIL_BAD_TOKEN,
                'email': AUTH_DATA_FAIL_BAD_TOKEN,
                'password': AUTH_DATA_FAIL_BAD_TOKEN,
                'token': AUTH_DATA_FAIL_EMPTY_FIELDS['token']
            }),
            data=API_BAD_REQUEST_EMPTY_FIELDS
        )

    @title('create-fail-bad-request-empty-fields')
    @description('Проверка ошибки Bad Request empty fields для create со всеми пустыми полями')
    def test_create_method_bad_request_empty_fields_all(self, users):
        asserts(
            assert_data=users.create(data=AUTH_DATA_FAIL_EMPTY_FIELDS),
            data=API_BAD_REQUEST_EMPTY_FIELDS
        )

    @title('create-fail-bad-request-bad-id')
    @description('Проверка ошибки Bad Request bad id для create')
    def test_create_method_bad_request_bad_id(self, users, create_admin):
        asserts(
            assert_data=users.create({
                **AUTH_CREATE(),
                'token': create_admin['token'],
                'user_id': AUTH_DATA_FAIL_BAD_ID
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-request-token-length')
    @description('Проверка ошибки Bad Request token length для create')
    def test_create_method_bad_request_length_token(self, users):
        asserts(
            assert_data=users.create(AUTH_DATA_CREATE_FAIL_LENGTH_TOKEN),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-request-login-length')
    @description('Проверка ошибки Bad Request login length для create')
    def test_create_method_bad_request_length_login(self, users):
        asserts(
            assert_data=users.create(AUTH_DATA_CREATE_FAIL_LENGTH_LOGIN),
            data=API_AUTH_BAD_REQUEST_LENGTH_LOGIN
        )

    @title('create-fail-bad-request-email-length')
    @description('Проверка ошибки Bad Requst email  length для create')
    def test_create_method_bad_request_length_email(self, users):
        asserts(
            assert_data=users.create(AUTH_DATA_CREATE_FAIL_LENGTH_EMAIL),
            data=API_BAD_REQUEST_LENGTH_EMAIL
        )

    @title('create-fail-bad-request-password-length')
    @description('Проверка ошибки Bad Request password length для create')
    def test_create_method_bad_request_length_password(self, users):
        asserts(
            assert_data=users.create(AUTH_DATA_CREATE_FAIL_LENGTH_PASSWORD),
            data=API_AUTH_BAD_REQUEST_LENGTH_PASSWORD
        )

    @title('create-fail-not-found-token')
    @description('Проверка ошибки Not Found token для create')
    def test_create_method_not_found_token(self, users):
        asserts(
            assert_data=users.create(AUTH_DATA_CREATE_FAIL_NOT_FOUND_TOKEN),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('create-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для create')
    def test_create_bad_request_bad_right(self, users, create_login_delete_user):
        asserts(
            assert_data=users.create({
                **AUTH_CREATE(),
                'token': create_login_delete_user['token'],
                'user_id': AUTH_DATA_FAIL_NOT_FOUND_ID,
            }),
            data=API_BAD_RIGHTS
        )

    @title('create-fail-bad-request-not-enought-rights')
    @description('Проверка ошибки Bad Request not enought rights для create')
    def test_create_bad_request_not_enought_rights(self, users, create_login_delete_user):
        asserts(
            assert_data=users.create({
                **AUTH_CREATE(),
                'token': create_login_delete_user['token'],
                'user_id': create_login_delete_user['id'],
            }),
            data=API_NOT_ENOUGHT_RIGHTS
        )

    @title('create-fail-bad-request-bad-email')
    @description('Проверка ошибки Bad Request bad email для create')
    def test_create_method_bad_request_email(self, users, create_admin):
        asserts(
            assert_data=users.create({
                **AUTH_CREATE_FAIL_BAD_EMAIL,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_EMAIL
        )

    @title('create-fail-bad-request-bad-password')
    @description('Проверка ошибки Bad Request bad password для create')
    def test_create_method_bad_request_password(self, users, create_admin):
        asserts(
            assert_data=users.create({
                **AUTH_DATA_CREATE_FAIL_PASSWORD,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_PASSWORD
        )

    @title('create-fail-bad-request-busy-email-login')
    @description('Проверка ошибки Bad Request busy email login для create')
    def test_create_method_bad_request_busy_email_login(self, users, create_admin):
        asserts(
            assert_data=users.create({
                **AUTH_DATA_CREATE_FAIL_BUSY_EMAIL_LOGIN,
                'token': create_admin['token'],
                'user_id': create_admin['id'],
            }),
            data=API_BAD_REQUEST_BAD_BUSY_EMAIL_LOGIN
        )
