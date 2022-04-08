from allure import title, description, suite, parent_suite

from data import API_USERS_SUCCESS, API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, AUTH_DATA_FAIL_BAD_TOKEN, API_AUTH_NOT_FOUND_TOKEN, AUTH_DATA_FAIL_BAD_ID, \
    API_BAD_REQUEST_BAD_ID, AUTH_DATA_FAIL_NOT_FOUND_ID, API_NOT_FOUND_ID, API_BAD_RIGHTS
from pages.api import asserts


@suite('Контроллер: Files. Метод: upload-avatar')
@parent_suite('[PYTHON][API]')
class TestApiFilesUploadAvatar:
    @title('upload-avatar')
    @description('Проверка корректной работы upload-avatar')
    def test_upload_avatar(self, create_admin, files, generate_image):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': create_admin['id'],
                    'token': create_admin['token']
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_USERS_SUCCESS
        )

    @title('upload-avatar-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для upload-avatar')
    def test_upload_avatar_method_not_allowed(self, files):
        asserts(
            assert_data=files.upload_avatar_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('upload-avatar-fail-bad-request-empty-token')
    @description('Проверка ошибки Bad Request empty token для upload-avatar')
    def test_upload_avatar_bad_request_empty_token(self, files, generate_image):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': 1,
                    'token': ''
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('upload-avatar-fail-bad-request-length-token')
    @description('Проверка ошибки Bad Request length token upload-avatar')
    def test_upload_avatar_bad_request_length_token(self, files, generate_image):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': 1,
                    'token': AUTH_DATA_LENGTH_TOKEN
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('upload-avatar-fail-not-found-token')
    @description('Проверка ошибки Not Found token для upload-avatar')
    def test_upload_avatar_not_found_token(self, files, generate_image):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': 1,
                    'token': AUTH_DATA_FAIL_BAD_TOKEN
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_AUTH_NOT_FOUND_TOKEN
        )

    @title('upload-avatar-fail-bad-request-user-id-minus')
    @description(
        'Проверка ошибки Bad Request user id для upload-avatar с отрицательным числом в идентификаторе пользователя')
    def test_upload_avatar_bad_request_user_id_minus(self, files, generate_image, create_admin):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': AUTH_DATA_FAIL_BAD_ID,
                    'token': create_admin['token']
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('upload-avatar-fail-not-found-id')
    @description('Проверка ошибки Not Found id для upload-avatar')
    def test_upload_avatar_not_found_id(self, files, generate_image, create_admin):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': AUTH_DATA_FAIL_NOT_FOUND_ID,
                    'token': create_admin['token']
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_NOT_FOUND_ID
        )

    @title('upload-avatar-fail-bad-request-bad-rights')
    @description('Проверка ошибки Bad Request bad rights для upload-avatar')
    def test_upload_avatar_bad_request_bad_rights(self, files, generate_image, create_admin, create_login_delete_user):
        asserts(
            assert_data=files.upload_avatar(
                data={
                    'id': create_admin['id'],
                    'token': create_login_delete_user['token']
                },
                file={
                    'avatar': open(generate_image, 'rb')
                }
            ),
            data=API_BAD_RIGHTS
        )
