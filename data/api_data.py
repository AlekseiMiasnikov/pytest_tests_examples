API_USERS_SUCCESS = {
    'status': "OK",
    'code': 200
}

API_SET_TIMEZONE_SUCCESS = {
    "status": "OK",
    "code": 200,
    "message": "Часовой пояс успешно обновлен"
}

API_GET_DEBT_ON = {
    "status": "OK",
    "code": 200,
    "data": {
        "debt": 'true'
    }
}

API_GET_DEBT_OFF = {
    "status": "OK",
    "code": 200,
    "data": {
        "debt": 'false'
    }
}

API_SET_DEBT_ON = {
    "status": "OK",
    "code": 200,
    "message": "Итог на конец года включен"
}

API_SET_DEBT_OFF = {
    "status": "OK",
    "code": 200,
    "message": "Итог на конец года выключен"
}

API_PAYMENTS_SUCCESS = {
    "code": 201,
    "status": "Created",
    "message": "Новый платеж успешно создан"
}

API_PAYMENTS_DELETE = {
    "status": "OK",
    "code": 200,
    "message": "Платеж успешно удален"
}

API_HISTORY_OPERATION_CREATE = {
    "status": "Created",
    "code": 201,
    "message": "Новая операция успешно добавлена"
}

API_SET_DEBT_ALLREDY_OFF = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Итог на конец года уже отключен'
}

API_SET_DEBT_ALLREDY_ON = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Итог на конец года уже включен'
}

API_GET_METHOD_NOT_ALLOWED = {
    'code': 405,
    'status': 'Method Not Allowed',
    'message': 'Пожалуйста, используйте метод GET для этого запроса'
}

API_AUTH_TOKEN_EMPTY = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, укажите токен пользователя'
}

API_TIMEZONE_EMPTY = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, укажите часовой пояс'
}

API_COMMENT_EMPTY = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, укажите комментарий'
}

API_COMMENT_LENGTH = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина комментария может быть 1000 символов'
}

API_AUTH_NOT_FOUND_TOKEN = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Пользователь с указанным токеном не найден'
}

API_BAD_RIGHTS = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Пользователь с указанным токеном и идентификатором не найден'
}

API_NOT_ENOUGHT_RIGHTS = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Недостаточно прав. Обратитесь к своему администратору'
}

API_BAD_UNITS_MEASUREMENT_ID = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Величина объема с указанным идентификатором не найдена'
}

API_BAD_TIMEZONE_ID = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Часового пояса с указанным идентификатором не найдено'
}

API_BAD_REQUEST_OBJECTS_ALLREDY_EXIST = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Объект с указанным названием уже есть'
}

API_NOT_FOUND_OBJECT_WAS_REMOVED = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Объект с указанным идентификатором уже был удален'
}

API_NOT_FOUND_LEGAL_ENTITIES_WAS_REMOVED = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Юридическое лицо с указанным идентификатором уже было удалено'
}

API_NOT_FOUND_VENDORS_ICONS = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Иконки с указанным идентификатором не найдено'
}

API_NOT_FOUND_VENDORS = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Поставщик с указанным идентификатором не найден'
}

API_NOT_FOUND_LEGAL_ENTITIES_TYPES = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Тип организации с указанным идентификатором не найден'
}

API_NOT_FOUND_LEGAL_ENTITIES = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Организация с указанным идентификатором не найдена'
}

API_NOT_FOUND_PAYMENT_LEGAL_ENTITIES = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Юридическое лицо с указанным идентификатором не найдено'
}

API_NOT_FOUND_VENDOR_WAS_REMOVED = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Поставщик с указанным идентификатором уже был удален'
}

API_USERS_GET_INFO = {
    "code": 200,
    "status": "OK",
}

API_MATERIAL_TYPES_UPDATE = {
    "status": "OK",
    "code": 200,
    "data": {
        "id": 2,
        "name": "alex_two"
    }
}

API_USERS_CREATE = {
    "code": 201,
    "status": "Created",
}

API_MATERIAL_TYPES_CREATE = {
    "code": 201,
    "status": "Created",
    "message": "Новый тип материала успешно создан"
}

API_MATERIAL_CREATE = {
    "status": "Created",
    "code": 201,
    "message": "Новый материал успешно создан"
}

API_OBJECTS_CREATE = {
    "status": "Created",
    "code": 201,
    "message": "Новый объект успешно создан"
}

API_VENDORS_CREATE = {
    "status": "Created",
    "code": 201,
    "message": "Новый поставщик успешно создан"
}

API_LEGAL_ENTITIES_CREATE = {
    "status": "Created",
    "code": 201,
    "message": "Новое юридическое лицо успешно создано"
}

API_USERS_DELETE = {
    'code': 200,
    'status': 'OK',
    'message': 'Пользователь был успешно удален'
}

API_AUTH_LOGIN_POST = {
    'code': 200,
    'status': 'OK'
}

API_AUTH_LOGOUT_POST = {
    'code': 200,
    'status': 'OK',
    'message': 'Пользователь успешно вышел из системы'
}

API_OBJECTS_DELETE = {
    "status": "OK",
    "code": 200,
    "message": "Объект успешно удален"
}

API_VENDORS_DELETE = {
    "status": "OK",
    "code": 200,
    "message": "Поставщик успешно удален"
}

API_LEGAL_ENTITIES_DELETE = {
    "status": "OK",
    "code": 200,
    "message": "Юридическое лицо успешно удалено"
}

API_CHANGE_PASSWORD = {
    'code': 200,
    'status': 'OK',
    'message': 'Пароль был успешно изменен'
}

API_OBJECTS_RESTORE = {
    "code": 200,
    "status": "OK",
    "message": "Объект успешно восстановлен"
}

API_VENDORS_RESTORE = {
    "code": 200,
    "status": "OK",
    "message": "Поставщик успешно восстановлен"
}

API_LEGAL_ENTITIES_RESTORE = {
    "code": 200,
    "status": "OK",
    "message": "Юридическое лицо успешно восстановлено"
}

API_AUTH_BAD_REQUEST = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, убедитесь, что все необходимые поля заполнены правильно'
}

API_AUTH_BAD_REQUEST_LENGTH_LOGIN = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина логина может быть 100 символов'
}

API_AUTH_BAD_REQUEST_LENGTH_PASSWORD = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина пароля может быть 100 символов'
}

API_BAD_REQUEST_LENGTH_EMAIL = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина электронной почты может быть 100 символов'
}

API_BAD_REQUEST_LENGTH_TOKEN = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина токена может быть 100 символов'
}

API_BAD_REQUEST_LENGTH_TINEZONE = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина часового пояса может быть 100 символов'
}

API_AUTH_NOT_FOUND_USER = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Такого пользователя не существует'
}

API_AUTH_BAD_REQUEST_LOGIN_PASSWORD_ERROR = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Неверный логин или пароль'
}

API_POST_METHOD_NOT_ALLOWED = {
    'code': 405,
    'status': 'Method Not Allowed',
    'message': 'Пожалуйста, используйте метод POST для этого запроса'
}

API_DELETE_METHOD_NOT_ALLOWED = {
    'code': 405,
    'status': 'Method Not Allowed',
    'message': 'Пожалуйста, используйте метод DELETE для этого запроса'
}

API_PUT_METHOD_NOT_ALLOWED = {
    'code': 405,
    'status': 'Method Not Allowed',
    'message': 'Пожалуйста, используйте метод PUT для этого запроса'
}

API_BAD_REQUEST_EMPTY_FIELDS = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, убедитесь, что все необходимые поля заполнены правильно'
}

API_BAD_REQUEST_EMPTY_OBJECTS = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, укажите название объекта'
}

API_BAD_REQUEST_EMPTY_VENDORS = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, укажите название поставщика'
}

API_BAD_REQUEST_EMPTY_LEGAL_ENTITIES = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пожалуйста, укажите наименование юридического лица'
}

API_BAD_REQUEST_VENDORS_NAME_LENGTH = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина названия может быть 30 символов'
}

API_BAD_REQUEST_LEGAL_ENTITIES_NAME_LENGTH = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Максимальная длина названия юридического лица может быть 20 символов'
}

API_BAD_REQUEST_BAD_EMAIL = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Неверный адрес электронной почты. Пожалуйста, проверьте правильность адреса электронной почты'
}

API_BAD_REQUEST_BAD_PASSWORD = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Пароль должен содержать не менее 5 символов'
}

API_BAD_REQUEST_BAD_BUSY_EMAIL_LOGIN = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Указанным адрес электронной почты или логин уже занят'
}

API_BAD_REQUEST_BAD_ID = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Идентификатор должен быть целым числом и должен быть больше нуля'
}

API_NOT_FOUND_ID = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Пользователь с указанным идентификатором не найден'
}

API_NOT_FOUND_OBJECTS = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Объект с указанным идентификатором не найден'
}

API_NOT_FOUND_PAYMENT = {
    'code': 404,
    'status': 'Not Found',
    'message': 'Платежа с указанным идентификатором не найдено'
}

API_BAD_REQUEST_ADMIN = {
    'code': 400,
    'status': 'Bad Request',
    'message': 'Вы не можете удалить администратора'
}

API_BAD_REQUEST_EMPTY_MATERIAL_TYPES = {
    "status": "Bad Request",
    "code": 400,
    "message": "Пожалуйста, укажите название типа материала"
}

API_BAD_REQUEST_EMPTY_MATERIALS = {
    "status": "Bad Request",
    "code": 400,
    "message": "Пожалуйста, укажите название материала"
}

API_BAD_REQUEST_LENGTH_MATERIAL_TYPES = {
    "status": "Bad Request",
    "code": 400,
    "message": "Максимальная длина названия типа материала может быть 100 символов"
}

API_BAD_REQUEST_LENGTH_MATERIALS = {
    "status": "Bad Request",
    "code": 400,
    "message": "Максимальная длина названия материала может быть 100 символов"
}

API_BAD_REQUEST_LENGTH_MATERIALS_100_CHARACTERS = {
    "status": "Bad Request",
    "code": 400,
    "message": "Максимальная длина названия может быть 100 символов"
}

API_BAD_REQUEST_BAD_LIMIT = {
    'status': 'Bad Request',
    'code': 400,
    'message': 'Лимит должен быть больше нуля'
}

API_BAD_REQUEST_BAD_OFFSET = {
    'status': 'Bad Request',
    'code': 400,
    'message': 'Смещение должно быть больше нуля'
}

API_NOT_FOUND_MATERIAL_TYPES_ID = {
    'status': 'Not Found',
    'code': 404,
    'message': 'Тип материала с указанным идентификатором не найден'
}

API_BAD_REQUEST_MATERIAL_TYPES_ALLREDY_EXIST = {
    "status": "Bad Request",
    "code": 400,
    "message": "Тип материала с указанным названием уже существует"
}

API_NOT_FOUND_MATERIAL_ID = {
    "status": "Not Found",
    "code": 404,
    "message": "Материал с указанным идентификатором не найден"
}

API_NOT_FOUND_TIMEZONE = {
    "status": "Not Found",
    "code": 404,
    "message": "Указанного часового пояса не найдено"
}

API_BAD_REQUEST_MATERIAL_ALLREDY_EXIST = {
    "status": "Bad Request",
    "code": 400,
    "message": "Материал с указанным названием уже существует"
}

API_BAD_REQUEST_MATERIAL_ALLREDY_EXIST = {
    "status": "Bad Request",
    "code": 400,
    "message": "Материал с указанным названием уже существует"
}

API_BAD_REQUEST_OBJECTS_ARCHIVE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Объекты могут быть либо активные - 0, либо архивные 1"
}

API_BAD_REQUEST_VENDORS_ARCHIVE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Поставщики могут быть либо активные - 0, либо архивные 1"
}

API_BAD_REQUEST_LEGAL_ENTITIES_ARCHIVE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Юридические лица могут быть либо активные - 0, либо архивные 1"
}

API_BAD_REQUEST_OBJECTS_ACTIVE_CANNOT_DELETE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Обновлять можно только активные объекты"
}

API_BAD_REQUEST_VENDORS_ACTIVE_CANNOT_DELETE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Обновлять можно только активных поставщиков"
}

API_BAD_REQUEST_LEGAL_ENTITIES_ACTIVE_CANNOT_DELETE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Обновлять можно только активные юридические лица"
}

API_BAD_REQUEST_OBJECTS_WAS_RESTORED = {
    "status": "Bad Request",
    "code": 400,
    "message": "Объект с указанным идентификатором уже был восстановлен"
}

API_BAD_REQUEST_VENDORS_WAS_RESTORED = {
    "status": "Bad Request",
    "code": 400,
    "message": "Поставщик с указанным идентификатором уже был восстановлен"
}

API_BAD_REQUEST_LEGAL_ENTITIES_WAS_RESTORED = {
    "status": "Bad Request",
    "code": 400,
    "message": "Юридическое лицо с указанным идентификатором уже было восстановлено"
}

API_BAD_REQUEST_SETTINGS_BAD_ACTIVE = {
    "status": "Bad Request",
    "code": 400,
    "message": "Итог на конец года может быть либо активным - 1, либо выключенным 0"
}

API_BAD_REQUEST_AMOUNT = {
    "status": "Bad Request",
    "code": 400,
    "message": "Сумма должна быть целым числом и должна быть больше нуля"
}

API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD = {
    "status": "Bad Request",
    "code": 400,
    "message": "Сумма должна быть меньше 1 000 000 000 рублей"
}

API_BAD_REQUEST_AMOUT_LESS_THAT_ONE_MILLIARD_VOLUME = {
    "status": "Bad Request",
    "code": 400,
    "message": "Объем должен быть меньше 1 000 000 000"
}

API_BAD_REQUEST_AMOUNT_VOLUME = {
    "status": "Bad Request",
    "code": 400,
    "message": "Объем должен быть целым числом и должен быть больше нуля"
}

API_LEGAL_ENTITIES_TYPES_OK = {
    "status": "OK",
    "code": 200,
    "data": [
        {
            "id": 1,
            "name": "ООО",
            "full_name": "Общество с ограниченной ответственностью"
        },
        {
            "id": 2,
            "name": "ОАО",
            "full_name": "Открытое акционерное общество"
        },
        {
            "id": 3,
            "name": "ЗАО",
            "full_name": "Закрытое акционерное общество"
        },
        {
            "id": 4,
            "name": "ПАО",
            "full_name": "Публичное акционерное общество"
        },
        {
            "id": 5,
            "name": "АО",
            "full_name": "Акционерное общество"
        },
        {
            "id": 6,
            "name": "ИП",
            "full_name": "Индивидуальный предприниматель"
        }
    ]
}

API_ICONS_OK = {
    "status": "OK",
    "code": 200,
    "data": {
        "icons": [
            {
                "id": 1,
                "prefix": "fab",
                "name": "500px"
            }
        ],
        "count": "1607"
    }
}

API_TIMEZONES = {
    "data": [
        {
            "id": 1,
            "timezone_name": "Europe/Moscow"
        },
        {
            "id": 2,
            "timezone_name": "Africa/Accra"
        },
        {
            "id": 3,
            "timezone_name": "Europe/Gibraltar"
        },
        {
            "id": 4,
            "timezone_name": "America/Godthab"
        },
        {
            "id": 5,
            "timezone_name": "America/Danmarkshavn"
        },
        {
            "id": 6,
            "timezone_name": "America/Scoresbysund"
        },
        {
            "id": 7,
            "timezone_name": "Africa/Bissau"
        },
        {
            "id": 8,
            "timezone_name": "America/Guyana"
        },
        {
            "id": 9,
            "timezone_name": "Asia/Hong_Kong"
        },
        {
            "id": 10,
            "timezone_name": "America/Tegucigalpa"
        },
        {
            "id": 11,
            "timezone_name": "America/Port-au-Prince"
        },
        {
            "id": 12,
            "timezone_name": "America/Argentina/Buenos_Aires"
        },
        {
            "id": 13,
            "timezone_name": "America/Argentina/Cordoba"
        },
        {
            "id": 14,
            "timezone_name": "America/Argentina/Salta"
        },
        {
            "id": 15,
            "timezone_name": "America/Argentina/Jujuy"
        },
        {
            "id": 16,
            "timezone_name": "America/Argentina/Tucuman"
        },
        {
            "id": 17,
            "timezone_name": "America/Argentina/Catamarca"
        },
        {
            "id": 18,
            "timezone_name": "America/Argentina/La_Rioja"
        },
        {
            "id": 19,
            "timezone_name": "America/Argentina/San_Juan"
        },
        {
            "id": 20,
            "timezone_name": "America/Argentina/Mendoza"
        },
        {
            "id": 21,
            "timezone_name": "America/Argentina/San_Luis"
        },
        {
            "id": 22,
            "timezone_name": "America/Argentina/Rio_Gallegos"
        },
        {
            "id": 23,
            "timezone_name": "America/Argentina/Ushuaia"
        },
        {
            "id": 24,
            "timezone_name": "America/Bahia_Banderas"
        },
        {
            "id": 25,
            "timezone_name": "Asia/Kuala_Lumpur"
        },
        {
            "id": 26,
            "timezone_name": "Asia/Kuching"
        },
        {
            "id": 27,
            "timezone_name": "Africa/Maputo"
        },
        {
            "id": 28,
            "timezone_name": "Africa/Windhoek"
        },
        {
            "id": 29,
            "timezone_name": "America/Campo_Grande"
        },
        {
            "id": 30,
            "timezone_name": "America/Cuiaba"
        },
        {
            "id": 31,
            "timezone_name": "America/Santarem"
        },
        {
            "id": 32,
            "timezone_name": "America/Porto_Velho"
        },
        {
            "id": 33,
            "timezone_name": "America/Boa_Vista"
        },
        {
            "id": 34,
            "timezone_name": "America/Curacao"
        },
        {
            "id": 35,
            "timezone_name": "Indian/Christmas"
        },
        {
            "id": 36,
            "timezone_name": "Asia/Nicosia"
        },
        {
            "id": 37,
            "timezone_name": "Asia/Famagusta"
        },
        {
            "id": 38,
            "timezone_name": "Europe/Prague"
        },
        {
            "id": 39,
            "timezone_name": "Europe/Berlin"
        },
        {
            "id": 40,
            "timezone_name": "America/Indiana/Knox"
        },
        {
            "id": 41,
            "timezone_name": "America/Menominee"
        },
        {
            "id": 42,
            "timezone_name": "America/North_Dakota/Center"
        },
        {
            "id": 43,
            "timezone_name": "America/Indiana/Petersburg"
        },
        {
            "id": 44,
            "timezone_name": "America/Indiana/Vevay"
        },
        {
            "id": 45,
            "timezone_name": "America/Chicago"
        },
        {
            "id": 46,
            "timezone_name": "America/Indiana/Tell_City"
        },
        {
            "id": 47,
            "timezone_name": "America/Indiana/Vincennes"
        },
        {
            "id": 48,
            "timezone_name": "America/Indiana/Winamac"
        },
        {
            "id": 49,
            "timezone_name": "America/Indiana/Marengo"
        },
        {
            "id": 50,
            "timezone_name": "America/Inuvik"
        },
        {
            "id": 51,
            "timezone_name": "America/Creston"
        },
        {
            "id": 52,
            "timezone_name": "America/Dawson_Creek"
        },
        {
            "id": 53,
            "timezone_name": "America/Fort_Nelson"
        },
        {
            "id": 54,
            "timezone_name": "America/Vancouver"
        },
        {
            "id": 55,
            "timezone_name": "America/Kentucky/Louisville"
        },
        {
            "id": 56,
            "timezone_name": "America/Kentucky/Monticello"
        },
        {
            "id": 57,
            "timezone_name": "America/Indiana/Indianapolis"
        },
        {
            "id": 58,
            "timezone_name": "America/Lima"
        },
        {
            "id": 59,
            "timezone_name": "Pacific/Tahiti"
        },
        {
            "id": 60,
            "timezone_name": "Pacific/Marquesas"
        },
        {
            "id": 61,
            "timezone_name": "Pacific/Gambier"
        },
        {
            "id": 62,
            "timezone_name": "Pacific/Port_Moresby"
        },
        {
            "id": 63,
            "timezone_name": "America/Manaus"
        },
        {
            "id": 64,
            "timezone_name": "America/Eirunepe"
        },
        {
            "id": 65,
            "timezone_name": "America/Rio_Branco"
        },
        {
            "id": 66,
            "timezone_name": "America/Nassau"
        },
        {
            "id": 67,
            "timezone_name": "Asia/Thimphu"
        },
        {
            "id": 68,
            "timezone_name": "America/Mazatlan"
        },
        {
            "id": 69,
            "timezone_name": "America/Chihuahua"
        },
        {
            "id": 70,
            "timezone_name": "America/Ojinaga"
        },
        {
            "id": 71,
            "timezone_name": "America/Hermosillo"
        },
        {
            "id": 72,
            "timezone_name": "America/Tijuana"
        },
        {
            "id": 73,
            "timezone_name": "America/Metlakatla"
        },
        {
            "id": 74,
            "timezone_name": "America/Yakutat"
        },
        {
            "id": 75,
            "timezone_name": "America/Nome"
        },
        {
            "id": 76,
            "timezone_name": "America/Adak"
        },
        {
            "id": 77,
            "timezone_name": "Pacific/Honolulu"
        },
        {
            "id": 78,
            "timezone_name": "America/Mexico_City"
        },
        {
            "id": 79,
            "timezone_name": "America/Cancun"
        },
        {
            "id": 80,
            "timezone_name": "America/Merida"
        },
        {
            "id": 81,
            "timezone_name": "America/Monterrey"
        },
        {
            "id": 82,
            "timezone_name": "America/Matamoros"
        },
        {
            "id": 83,
            "timezone_name": "America/Moncton"
        },
        {
            "id": 84,
            "timezone_name": "America/Goose_Bay"
        },
        {
            "id": 85,
            "timezone_name": "America/Blanc-Sablon"
        },
        {
            "id": 86,
            "timezone_name": "America/Toronto"
        },
        {
            "id": 87,
            "timezone_name": "America/Nipigon"
        },
        {
            "id": 88,
            "timezone_name": "America/Montevideo"
        },
        {
            "id": 89,
            "timezone_name": "Asia/Samarkand"
        },
        {
            "id": 90,
            "timezone_name": "Asia/Tashkent"
        },
        {
            "id": 91,
            "timezone_name": "America/Caracas"
        },
        {
            "id": 92,
            "timezone_name": "Asia/Ho_Chi_Minh"
        },
        {
            "id": 93,
            "timezone_name": "America/North_Dakota/New_Salem"
        },
        {
            "id": 94,
            "timezone_name": "America/North_Dakota/Beulah"
        },
        {
            "id": 95,
            "timezone_name": "America/Denver"
        },
        {
            "id": 96,
            "timezone_name": "America/Boise"
        },
        {
            "id": 97,
            "timezone_name": "America/Phoenix"
        },
        {
            "id": 98,
            "timezone_name": "America/Los_Angeles"
        },
        {
            "id": 99,
            "timezone_name": "America/Anchorage"
        },
        {
            "id": 100,
            "timezone_name": "America/Juneau"
        },
        {
            "id": 101,
            "timezone_name": "America/Sitka"
        },
        {
            "id": 102,
            "timezone_name": "America/Rainy_River"
        },
        {
            "id": 103,
            "timezone_name": "America/Resolute"
        },
        {
            "id": 104,
            "timezone_name": "America/Rankin_Inlet"
        },
        {
            "id": 105,
            "timezone_name": "America/Regina"
        },
        {
            "id": 106,
            "timezone_name": "America/Recife"
        },
        {
            "id": 107,
            "timezone_name": "America/Araguaina"
        },
        {
            "id": 108,
            "timezone_name": "America/Maceio"
        },
        {
            "id": 109,
            "timezone_name": "America/Bahia"
        },
        {
            "id": 110,
            "timezone_name": "America/Sao_Paulo"
        },
        {
            "id": 111,
            "timezone_name": "America/Swift_Current"
        },
        {
            "id": 112,
            "timezone_name": "America/Edmonton"
        },
        {
            "id": 113,
            "timezone_name": "America/Cambridge_Bay"
        },
        {
            "id": 114,
            "timezone_name": "America/Yellowknife"
        },
        {
            "id": 115,
            "timezone_name": "America/Thule"
        },
        {
            "id": 116,
            "timezone_name": "Europe/Athens"
        },
        {
            "id": 117,
            "timezone_name": "Atlantic/South_Georgia"
        },
        {
            "id": 118,
            "timezone_name": "America/Guatemala"
        },
        {
            "id": 119,
            "timezone_name": "Pacific/Guam"
        },
        {
            "id": 120,
            "timezone_name": "America/Thunder_Bay"
        },
        {
            "id": 121,
            "timezone_name": "America/Iqaluit"
        },
        {
            "id": 122,
            "timezone_name": "America/Pangnirtung"
        },
        {
            "id": 123,
            "timezone_name": "America/Atikokan"
        },
        {
            "id": 124,
            "timezone_name": "America/Winnipeg"
        },
        {
            "id": 125,
            "timezone_name": "America/Whitehorse"
        },
        {
            "id": 126,
            "timezone_name": "America/Dawson"
        },
        {
            "id": 127,
            "timezone_name": "Indian/Cocos"
        },
        {
            "id": 128,
            "timezone_name": "Europe/Zurich"
        },
        {
            "id": 129,
            "timezone_name": "Africa/Abidjan"
        },
        {
            "id": 130,
            "timezone_name": "Antarctica/Davis"
        },
        {
            "id": 131,
            "timezone_name": "Antarctica/DumontDUrville"
        },
        {
            "id": 132,
            "timezone_name": "Antarctica/Mawson"
        },
        {
            "id": 133,
            "timezone_name": "Antarctica/Palmer"
        },
        {
            "id": 134,
            "timezone_name": "Antarctica/Rothera"
        },
        {
            "id": 135,
            "timezone_name": "Antarctica/Syowa"
        },
        {
            "id": 136,
            "timezone_name": "Antarctica/Troll"
        },
        {
            "id": 137,
            "timezone_name": "Antarctica/Vostok"
        },
        {
            "id": 138,
            "timezone_name": "Asia/Almaty"
        },
        {
            "id": 139,
            "timezone_name": "Asia/Qyzylorda"
        },
        {
            "id": 140,
            "timezone_name": "Asia/Qostanay"
        },
        {
            "id": 141,
            "timezone_name": "Asia/Aqtobe"
        },
        {
            "id": 142,
            "timezone_name": "Asia/Aqtau"
        },
        {
            "id": 143,
            "timezone_name": "Asia/Atyrau"
        },
        {
            "id": 144,
            "timezone_name": "Asia/Damascus"
        },
        {
            "id": 145,
            "timezone_name": "America/Grand_Turk"
        },
        {
            "id": 146,
            "timezone_name": "Africa/Ndjamena"
        },
        {
            "id": 147,
            "timezone_name": "Indian/Kerguelen"
        },
        {
            "id": 148,
            "timezone_name": "Asia/Bangkok"
        },
        {
            "id": 149,
            "timezone_name": "Asia/Dushanbe"
        },
        {
            "id": 150,
            "timezone_name": "Pacific/Fakaofo"
        },
        {
            "id": 151,
            "timezone_name": "Asia/Dili"
        },
        {
            "id": 152,
            "timezone_name": "Asia/Ashgabat"
        },
        {
            "id": 153,
            "timezone_name": "Africa/Tunis"
        },
        {
            "id": 154,
            "timezone_name": "Pacific/Tongatapu"
        },
        {
            "id": 155,
            "timezone_name": "Asia/Jerusalem"
        },
        {
            "id": 156,
            "timezone_name": "Asia/Kolkata"
        },
        {
            "id": 157,
            "timezone_name": "Indian/Chagos"
        },
        {
            "id": 158,
            "timezone_name": "Asia/Baghdad"
        },
        {
            "id": 159,
            "timezone_name": "Asia/Tehran"
        },
        {
            "id": 160,
            "timezone_name": "Atlantic/Reykjavik"
        },
        {
            "id": 161,
            "timezone_name": "Asia/Kathmandu"
        },
        {
            "id": 162,
            "timezone_name": "Pacific/Nauru"
        },
        {
            "id": 163,
            "timezone_name": "Pacific/Niue"
        },
        {
            "id": 164,
            "timezone_name": "Pacific/Auckland"
        },
        {
            "id": 165,
            "timezone_name": "Pacific/Chatham"
        },
        {
            "id": 166,
            "timezone_name": "America/Panama"
        },
        {
            "id": 167,
            "timezone_name": "Asia/Krasnoyarsk"
        },
        {
            "id": 168,
            "timezone_name": "Asia/Irkutsk"
        },
        {
            "id": 169,
            "timezone_name": "Asia/Chita"
        },
        {
            "id": 170,
            "timezone_name": "Asia/Yakutsk"
        },
        {
            "id": 171,
            "timezone_name": "Asia/Khandyga"
        },
        {
            "id": 172,
            "timezone_name": "Asia/Vladivostok"
        },
        {
            "id": 173,
            "timezone_name": "Asia/Macau"
        },
        {
            "id": 174,
            "timezone_name": "America/Martinique"
        },
        {
            "id": 175,
            "timezone_name": "Europe/Malta"
        },
        {
            "id": 176,
            "timezone_name": "Indian/Mauritius"
        },
        {
            "id": 177,
            "timezone_name": "Indian/Maldives"
        },
        {
            "id": 178,
            "timezone_name": "Asia/Oral"
        },
        {
            "id": 179,
            "timezone_name": "Asia/Beirut"
        },
        {
            "id": 180,
            "timezone_name": "Asia/Colombo"
        },
        {
            "id": 181,
            "timezone_name": "Africa/Monrovia"
        },
        {
            "id": 182,
            "timezone_name": "Europe/Vilnius"
        },
        {
            "id": 183,
            "timezone_name": "Europe/Luxembourg"
        },
        {
            "id": 184,
            "timezone_name": "Asia/Riyadh"
        },
        {
            "id": 185,
            "timezone_name": "Pacific/Guadalcanal"
        },
        {
            "id": 186,
            "timezone_name": "Indian/Mahe"
        },
        {
            "id": 187,
            "timezone_name": "Africa/Khartoum"
        },
        {
            "id": 188,
            "timezone_name": "Europe/Stockholm"
        },
        {
            "id": 189,
            "timezone_name": "Asia/Singapore"
        },
        {
            "id": 190,
            "timezone_name": "America/Paramaribo"
        },
        {
            "id": 191,
            "timezone_name": "Africa/Juba"
        },
        {
            "id": 192,
            "timezone_name": "Africa/Sao_Tome"
        },
        {
            "id": 193,
            "timezone_name": "America/El_Salvador"
        },
        {
            "id": 194,
            "timezone_name": "Asia/Urumqi"
        },
        {
            "id": 195,
            "timezone_name": "America/Bogota"
        },
        {
            "id": 196,
            "timezone_name": "America/Costa_Rica"
        },
        {
            "id": 197,
            "timezone_name": "America/Havana"
        },
        {
            "id": 198,
            "timezone_name": "Atlantic/Cape_Verde"
        },
        {
            "id": 199,
            "timezone_name": "Asia/Ust-Nera"
        },
        {
            "id": 200,
            "timezone_name": "Asia/Magadan"
        },
        {
            "id": 201,
            "timezone_name": "Asia/Sakhalin"
        },
        {
            "id": 202,
            "timezone_name": "Asia/Srednekolymsk"
        },
        {
            "id": 203,
            "timezone_name": "Asia/Kamchatka"
        },
        {
            "id": 204,
            "timezone_name": "Asia/Anadyr"
        },
        {
            "id": 205,
            "timezone_name": "Asia/Yekaterinburg"
        },
        {
            "id": 206,
            "timezone_name": "Asia/Omsk"
        },
        {
            "id": 207,
            "timezone_name": "Asia/Novosibirsk"
        },
        {
            "id": 208,
            "timezone_name": "Asia/Barnaul"
        },
        {
            "id": 209,
            "timezone_name": "Asia/Tomsk"
        },
        {
            "id": 210,
            "timezone_name": "Asia/Novokuznetsk"
        },
        {
            "id": 211,
            "timezone_name": "Atlantic/Azores"
        },
        {
            "id": 212,
            "timezone_name": "Pacific/Palau"
        },
        {
            "id": 213,
            "timezone_name": "America/Asuncion"
        },
        {
            "id": 214,
            "timezone_name": "Asia/Qatar"
        },
        {
            "id": 215,
            "timezone_name": "Indian/Reunion"
        },
        {
            "id": 216,
            "timezone_name": "Europe/Bucharest"
        },
        {
            "id": 217,
            "timezone_name": "Atlantic/Bermuda"
        },
        {
            "id": 218,
            "timezone_name": "Asia/Brunei"
        },
        {
            "id": 219,
            "timezone_name": "America/La_Paz"
        },
        {
            "id": 220,
            "timezone_name": "America/Noronha"
        },
        {
            "id": 221,
            "timezone_name": "America/Belem"
        },
        {
            "id": 222,
            "timezone_name": "America/Fortaleza"
        },
        {
            "id": 223,
            "timezone_name": "Australia/Brisbane"
        },
        {
            "id": 224,
            "timezone_name": "Australia/Lindeman"
        },
        {
            "id": 225,
            "timezone_name": "Australia/Adelaide"
        },
        {
            "id": 226,
            "timezone_name": "Australia/Darwin"
        },
        {
            "id": 227,
            "timezone_name": "Australia/Perth"
        },
        {
            "id": 228,
            "timezone_name": "Australia/Currie"
        },
        {
            "id": 229,
            "timezone_name": "Australia/Melbourne"
        },
        {
            "id": 230,
            "timezone_name": "Australia/Sydney"
        },
        {
            "id": 231,
            "timezone_name": "Australia/Broken_Hill"
        },
        {
            "id": 232,
            "timezone_name": "Australia/Eucla"
        },
        {
            "id": 233,
            "timezone_name": "Asia/Baku"
        },
        {
            "id": 234,
            "timezone_name": "America/Barbados"
        },
        {
            "id": 235,
            "timezone_name": "Asia/Dhaka"
        },
        {
            "id": 236,
            "timezone_name": "Europe/Brussels"
        },
        {
            "id": 237,
            "timezone_name": "Europe/Sofia"
        },
        {
            "id": 238,
            "timezone_name": "Europe/Astrakhan"
        },
        {
            "id": 239,
            "timezone_name": "Europe/Volgograd"
        },
        {
            "id": 240,
            "timezone_name": "Europe/Saratov"
        },
        {
            "id": 241,
            "timezone_name": "Europe/Ulyanovsk"
        },
        {
            "id": 242,
            "timezone_name": "Europe/Samara"
        },
        {
            "id": 243,
            "timezone_name": "Europe/Belgrade"
        },
        {
            "id": 244,
            "timezone_name": "Europe/Kaliningrad"
        },
        {
            "id": 245,
            "timezone_name": "Europe/Simferopol"
        },
        {
            "id": 246,
            "timezone_name": "Europe/Kirov"
        },
        {
            "id": 247,
            "timezone_name": "Europe/Budapest"
        },
        {
            "id": 248,
            "timezone_name": "Asia/Jakarta"
        },
        {
            "id": 249,
            "timezone_name": "Asia/Pontianak"
        },
        {
            "id": 250,
            "timezone_name": "Asia/Makassar"
        },
        {
            "id": 251,
            "timezone_name": "Asia/Jayapura"
        },
        {
            "id": 252,
            "timezone_name": "Europe/Dublin"
        },
        {
            "id": 253,
            "timezone_name": "Europe/Copenhagen"
        },
        {
            "id": 254,
            "timezone_name": "America/Santo_Domingo"
        },
        {
            "id": 255,
            "timezone_name": "Africa/Algiers"
        },
        {
            "id": 256,
            "timezone_name": "America/Guayaquil"
        },
        {
            "id": 257,
            "timezone_name": "Pacific/Galapagos"
        },
        {
            "id": 258,
            "timezone_name": "Europe/Helsinki"
        },
        {
            "id": 259,
            "timezone_name": "Pacific/Fiji"
        },
        {
            "id": 260,
            "timezone_name": "Atlantic/Stanley"
        },
        {
            "id": 261,
            "timezone_name": "Pacific/Chuuk"
        },
        {
            "id": 262,
            "timezone_name": "Pacific/Pohnpei"
        },
        {
            "id": 263,
            "timezone_name": "Europe/Istanbul"
        },
        {
            "id": 264,
            "timezone_name": "America/Port_of_Spain"
        },
        {
            "id": 265,
            "timezone_name": "Pacific/Funafuti"
        },
        {
            "id": 266,
            "timezone_name": "Asia/Taipei"
        },
        {
            "id": 267,
            "timezone_name": "Europe/Kiev"
        },
        {
            "id": 268,
            "timezone_name": "Europe/Minsk"
        },
        {
            "id": 269,
            "timezone_name": "America/Belize"
        },
        {
            "id": 270,
            "timezone_name": "America/St_Johns"
        },
        {
            "id": 271,
            "timezone_name": "America/Halifax"
        },
        {
            "id": 272,
            "timezone_name": "America/Glace_Bay"
        },
        {
            "id": 273,
            "timezone_name": "Europe/Riga"
        },
        {
            "id": 274,
            "timezone_name": "Africa/Tripoli"
        },
        {
            "id": 275,
            "timezone_name": "Africa/Casablanca"
        },
        {
            "id": 276,
            "timezone_name": "Europe/Monaco"
        },
        {
            "id": 277,
            "timezone_name": "Europe/Chisinau"
        },
        {
            "id": 278,
            "timezone_name": "Europe/Rome"
        },
        {
            "id": 279,
            "timezone_name": "America/Jamaica"
        },
        {
            "id": 280,
            "timezone_name": "Asia/Amman"
        },
        {
            "id": 281,
            "timezone_name": "Asia/Tokyo"
        },
        {
            "id": 282,
            "timezone_name": "Africa/Nairobi"
        },
        {
            "id": 283,
            "timezone_name": "Asia/Bishkek"
        },
        {
            "id": 284,
            "timezone_name": "Europe/Tallinn"
        },
        {
            "id": 285,
            "timezone_name": "Africa/Cairo"
        },
        {
            "id": 286,
            "timezone_name": "Africa/El_Aaiun"
        },
        {
            "id": 287,
            "timezone_name": "Europe/Madrid"
        },
        {
            "id": 288,
            "timezone_name": "Africa/Ceuta"
        },
        {
            "id": 289,
            "timezone_name": "Atlantic/Canary"
        },
        {
            "id": 290,
            "timezone_name": "Europe/Uzhgorod"
        },
        {
            "id": 291,
            "timezone_name": "Europe/Zaporozhye"
        },
        {
            "id": 292,
            "timezone_name": "Pacific/Wake"
        },
        {
            "id": 293,
            "timezone_name": "America/New_York"
        },
        {
            "id": 294,
            "timezone_name": "America/Detroit"
        },
        {
            "id": 295,
            "timezone_name": "Pacific/Bougainville"
        },
        {
            "id": 296,
            "timezone_name": "Asia/Manila"
        },
        {
            "id": 297,
            "timezone_name": "Asia/Karachi"
        },
        {
            "id": 298,
            "timezone_name": "Europe/Warsaw"
        },
        {
            "id": 299,
            "timezone_name": "America/Miquelon"
        },
        {
            "id": 300,
            "timezone_name": "Pacific/Efate"
        },
        {
            "id": 301,
            "timezone_name": "Pacific/Wallis"
        },
        {
            "id": 302,
            "timezone_name": "Pacific/Apia"
        },
        {
            "id": 303,
            "timezone_name": "Africa/Johannesburg"
        },
        {
            "id": 304,
            "timezone_name": "Pacific/Kosrae"
        },
        {
            "id": 305,
            "timezone_name": "Atlantic/Faroe"
        },
        {
            "id": 306,
            "timezone_name": "Europe/Paris"
        },
        {
            "id": 307,
            "timezone_name": "Europe/London"
        },
        {
            "id": 308,
            "timezone_name": "Asia/Tbilisi"
        },
        {
            "id": 309,
            "timezone_name": "America/Cayenne"
        },
        {
            "id": 310,
            "timezone_name": "Pacific/Majuro"
        },
        {
            "id": 311,
            "timezone_name": "Pacific/Kwajalein"
        },
        {
            "id": 312,
            "timezone_name": "Asia/Yangon"
        },
        {
            "id": 313,
            "timezone_name": "Asia/Ulaanbaatar"
        },
        {
            "id": 314,
            "timezone_name": "Asia/Hovd"
        },
        {
            "id": 315,
            "timezone_name": "Asia/Choibalsan"
        },
        {
            "id": 316,
            "timezone_name": "Pacific/Noumea"
        },
        {
            "id": 317,
            "timezone_name": "Pacific/Norfolk"
        },
        {
            "id": 318,
            "timezone_name": "Africa/Lagos"
        },
        {
            "id": 319,
            "timezone_name": "America/Managua"
        },
        {
            "id": 320,
            "timezone_name": "Europe/Amsterdam"
        },
        {
            "id": 321,
            "timezone_name": "Europe/Oslo"
        },
        {
            "id": 322,
            "timezone_name": "Pacific/Pago_Pago"
        },
        {
            "id": 323,
            "timezone_name": "Europe/Vienna"
        },
        {
            "id": 324,
            "timezone_name": "Australia/Lord_Howe"
        },
        {
            "id": 325,
            "timezone_name": "Antarctica/Macquarie"
        },
        {
            "id": 326,
            "timezone_name": "Australia/Hobart"
        },
        {
            "id": 327,
            "timezone_name": "Pacific/Pitcairn"
        },
        {
            "id": 328,
            "timezone_name": "America/Puerto_Rico"
        },
        {
            "id": 329,
            "timezone_name": "Asia/Gaza"
        },
        {
            "id": 330,
            "timezone_name": "Asia/Hebron"
        },
        {
            "id": 331,
            "timezone_name": "Europe/Lisbon"
        },
        {
            "id": 332,
            "timezone_name": "Atlantic/Madeira"
        },
        {
            "id": 333,
            "timezone_name": "Pacific/Rarotonga"
        },
        {
            "id": 334,
            "timezone_name": "America/Santiago"
        },
        {
            "id": 335,
            "timezone_name": "America/Punta_Arenas"
        },
        {
            "id": 336,
            "timezone_name": "Pacific/Easter"
        },
        {
            "id": 337,
            "timezone_name": "Asia/Shanghai"
        },
        {
            "id": 338,
            "timezone_name": "Pacific/Tarawa"
        },
        {
            "id": 339,
            "timezone_name": "Pacific/Enderbury"
        },
        {
            "id": 340,
            "timezone_name": "Pacific/Kiritimati"
        },
        {
            "id": 341,
            "timezone_name": "Asia/Pyongyang"
        },
        {
            "id": 342,
            "timezone_name": "Asia/Seoul"
        },
        {
            "id": 343,
            "timezone_name": "Europe/Andorra"
        },
        {
            "id": 344,
            "timezone_name": "Asia/Dubai"
        },
        {
            "id": 345,
            "timezone_name": "Asia/Kabul"
        },
        {
            "id": 346,
            "timezone_name": "Europe/Tirane"
        },
        {
            "id": 347,
            "timezone_name": "Asia/Yerevan"
        },
        {
            "id": 348,
            "timezone_name": "Antarctica/Casey"
        }
    ]
}
