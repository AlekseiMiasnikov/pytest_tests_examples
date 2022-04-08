from allure import title, description, suite, parent_suite

from data import API_HISTORY_OPERATION_CREATE, DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1, \
    DATA_HISTORY_OPERATION_SUM_RANDOM, AUTH_DATA_FAIL_BAD_TOKEN, \
    DATA_PAYMENTS_TIMESTAMP, API_POST_METHOD_NOT_ALLOWED, API_AUTH_TOKEN_EMPTY, AUTH_DATA_LENGTH_TOKEN, \
    API_BAD_REQUEST_LENGTH_TOKEN, API_COMMENT_EMPTY, API_COMMENT_LENGTH, DATA_HISTORY_OPERATION_COMMENT_LENGTH, \
    AUTH_DATA_FAIL_BAD_ID, API_BAD_REQUEST_BAD_ID, API_BAD_REQUEST_AMOUNT, \
    API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD, API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD_VOLUME, \
    API_BAD_REQUEST_AMOUNT_VOLUME
from pages.api import asserts
from pytest import mark


@mark.dev
@suite('Контроллер: HistoryOperation. Метод: create')
@parent_suite('[PYTHON][API]')
class TestApiHistoryOperationCreate:
    @title('create')
    @description('Проверка корректной работы create без загрузки файла')
    def test_create_no_file(self, history_operation, create_admin, create_vendors_remove,
                            create_material_type_materials_remove, create_objects_remove, remove_history_operation):
        comment = AUTH_DATA_FAIL_BAD_TOKEN
        asserts(
            assert_data=history_operation.create({
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': comment,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_HISTORY_OPERATION_CREATE
        )
        remove_history_operation(comment)

    # @title('create')
    # @description('Проверка корректной работы create с загрузкой файла')
    # def test_create_no_file(self, history_operation, create_admin, create_vendors_remove,
    #                         create_material_type_materials_remove, create_objects_remove):
    #     asserts(
    #         assert_data=history_operation.create({
    #             'token': create_admin['token'],
    #             'user_id': create_admin['id'],
    #             'vendor_id': create_vendors_remove,
    #             'material_id': create_material_type_materials_remove,
    #             'object_id': create_objects_remove,
    #             'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
    #             'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
    #             'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
    #             'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
    #             'comment': AUTH_DATA_FAIL_BAD_TOKEN,
    #             'created_at': DATA_PAYMENTS_TIMESTAMP,
    #             'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
    #             'file': '',
    #         }),
    #         data=API_HISTORY_OPERATION_CREATE
    #     )

    @title('create-fail-method-not-allowed')
    @description('Проверка ошибки Method Not Allowed для create')
    def test_create_method_not_allowed(self, history_operation):
        asserts(
            assert_data=history_operation.create_method_not_allowed(),
            data=API_POST_METHOD_NOT_ALLOWED
        )

    @title('create-fail-bad-requst-empty-token')
    @description('Проверка ошибки Bad Request empty token для create')
    def test_create_bad_request_empty_token(self, history_operation, create_vendors_remove,
                                            create_material_type_materials_remove, create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': '',
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_AUTH_TOKEN_EMPTY
        )

    @title('create-fail-bad-requst-length-token')
    @description('Проверка ошибки Bad Request length token для create')
    def test_create_bad_request_length_token(self, history_operation, create_vendors_remove,
                                             create_material_type_materials_remove, create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': AUTH_DATA_LENGTH_TOKEN,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_LENGTH_TOKEN
        )

    @title('create-fail-bad-requst-comment-empty')
    @description('Проверка ошибки Bad Request comment empty для create')
    def test_create_bad_request_comment_empty(self, history_operation, create_vendors_remove,
                                              create_material_type_materials_remove, create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': '',
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_COMMENT_EMPTY
        )

    @title('create-fail-bad-requst-comment-length')
    @description('Проверка ошибки Bad Request length empty для create')
    def test_create_bad_request_comment_length(self, create_admin, history_operation, create_vendors_remove,
                                               create_material_type_materials_remove, create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': DATA_HISTORY_OPERATION_COMMENT_LENGTH,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_COMMENT_LENGTH
        )

    @title('create-fail-bad-requst-user-id-minus')
    @description('Проверка ошибки Bad Request user id для create с отрицательным идентификатором пользователя')
    def test_create_bad_request_user_id_minus(self, history_operation, create_vendors_remove,
                                              create_material_type_materials_remove, create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': AUTH_DATA_FAIL_BAD_ID,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-user-id-varchar')
    @description('Проверка ошибки Bad Request user id для create с символами в идентификаторе пользователя')
    def test_create_bad_request_user_id_varchar(self, history_operation, create_vendors_remove,
                                                create_material_type_materials_remove, create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 'text',
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-object-id-minus')
    @description('Проверка ошибки Bad Request object id для create с отрицательным идентификатором объекта')
    def test_create_bad_request_object_id_minus(self, history_operation, create_vendors_remove,
                                                create_material_type_materials_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': AUTH_DATA_FAIL_BAD_ID,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-object-id-varchar')
    @description('Проверка ошибки Bad Request object id для create с символами в идентификаторе объекта')
    def test_create_bad_request_object_id_varchar(self, history_operation, create_vendors_remove,
                                                  create_material_type_materials_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': 'text',
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-vendor-id-minus')
    @description('Проверка ошибки Bad Request vendor id для create с отрицательным идентификатором поставщика')
    def test_create_bad_request_vendor_id_minus(self, history_operation, create_material_type_materials_remove,
                                                create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': AUTH_DATA_FAIL_BAD_ID,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-vendor-id-varchar')
    @description('Проверка ошибки Bad Request vendor id для create с символами в идентификаторе поставщика')
    def test_create_bad_request_vendor_id_varchar(self, history_operation, create_material_type_materials_remove,
                                                  create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': 'text',
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-material-id-minus')
    @description('Проверка ошибки Bad Request material id для create с отрицательным идентификатором материала')
    def test_create_bad_request_material_id_minus(self, history_operation, create_vendors_remove,
                                                  create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': AUTH_DATA_FAIL_BAD_ID,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-material-id-varchar')
    @description('Проверка ошибки Bad Request material id для create с символами в идентификаторе материала')
    def test_create_bad_request_material_id_varchar(self, history_operation, create_vendors_remove,
                                                    create_objects_remove):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': 'text',
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_BAD_ID
        )

    @title('create-fail-bad-requst-price-minus')
    @description('Проверка ошибки Bad Request price для create с отрицательной стоимостью')
    def test_create_bad_request_price_minus(self, history_operation, create_vendors_remove,
                                            create_material_type_materials_remove, create_objects_remove,
                                            remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': AUTH_DATA_FAIL_BAD_ID,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-price-zero')
    @description('Проверка ошибки Bad Request price для create с нулевым значением в стоимости')
    def test_create_bad_request_price_zero(self, history_operation, create_vendors_remove, create_admin,
                                           create_material_type_materials_remove, create_objects_remove,
                                           remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': 0,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': 0,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-total-minus')
    @description('Проверка ошибки Bad Request price для create с отрицательной итоговой стоимостью')
    def test_create_bad_request_total_minus(self, history_operation, create_vendors_remove,
                                            create_material_type_materials_remove, create_objects_remove,
                                            remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': AUTH_DATA_FAIL_BAD_ID,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-total-varchar')
    @description('Проверка ошибки Bad Request price для create с нулевым значением в итоговой стоимости')
    def test_create_bad_request_total_varchar(self, history_operation, create_vendors_remove,
                                              create_material_type_materials_remove, create_objects_remove,
                                              remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': 0,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUNT
        )

    @title('create-fail-bad-requst-total-length')
    @description('Проверка ошибки Bad Request total length для create')
    def test_create_bad_request_total_length(self, history_operation, create_vendors_remove,
                                             create_material_type_materials_remove, create_objects_remove,
                                             remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': 1000000000,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD
        )

    @title('create-fail-bad-requst-price-length')
    @description('Проверка ошибки Bad Request price length для create')
    def test_create_bad_request_price_length(self, history_operation, create_vendors_remove,
                                             create_material_type_materials_remove, create_objects_remove,
                                             remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'price': 1000000000,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD
        )

    @title('create-fail-bad-requst-volume-length')
    @description('Проверка ошибки Bad Request volume length для create')
    def test_create_bad_request_volume_length(self, history_operation, create_vendors_remove,
                                              create_material_type_materials_remove, create_objects_remove,
                                              remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': 1000000000,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD_VOLUME
        )

    @title('create-fail-bad-requst-volume-minus')
    @description('Проверка ошибки Bad Request volume для create с отрицательным значением в объеме')
    def test_create_bad_request_volume_minus(self, history_operation, create_vendors_remove,
                                             create_material_type_materials_remove, create_objects_remove,
                                             remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': 1,
                'user_id': 1,
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'volume': AUTH_DATA_FAIL_BAD_ID,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUNT_VOLUME
        )

    @title('create-fail-bad-requst-volume-zero')
    @description('Проверка ошибки Bad Request volume для create с нулевым значением в объеме')
    def test_create_bad_request_volume_zero(self, history_operation, create_vendors_remove, create_admin,
                                            create_material_type_materials_remove, create_objects_remove,
                                            remove_history_operation):
        asserts(
            assert_data=history_operation.create({
                'token': create_admin['token'],
                'user_id': create_admin['id'],
                'vendor_id': create_vendors_remove,
                'material_id': create_material_type_materials_remove,
                'object_id': create_objects_remove,
                'is_debt': 0,
                'volume': 0,
                'price': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'total': DATA_HISTORY_OPERATION_SUM_RANDOM,
                'comment': AUTH_DATA_FAIL_BAD_TOKEN,
                'created_at': DATA_PAYMENTS_TIMESTAMP,
                'confirmed_data': DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1,
                'file': '',
            }),
            data=API_BAD_REQUEST_AMOUNT_VOLUME
        )

    # DEBT_ON_OR_OFF
