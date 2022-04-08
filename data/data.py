import random
import secrets
from datetime import datetime
from uuid import uuid4

from data.api_data import API_TIMEZONES

DATA_PAYMENTS_TIMESTAMP = datetime.timestamp(datetime.now())

DATA_AMOUNT_PAYMENTS_SUCCESS = random.randint(1, 999999999)

DATA_AMOUNT_PAYMENTS_BAD = random.randint(1000000000, 5000000000)

DATA_TIMEZONE_RANDOM = random.choices(API_TIMEZONES['data'], k=1)[0]

DATA_TIMEZONE_RANDOM_NUM = random.randint(1, 348)


def AUTH_DATA():
    name = str(secrets.token_hex(random.randint(8, 30)))
    return {
        'login': name,
        'password': name,
        'email': f'{name}@it-paradise.com',
    }


def AUTH_CREATE():
    return {
        'login': str(uuid4()),
        'email': str(uuid4()) + '@it-paradise.com',
        'password': str(uuid4()),
    }


def NAME_MATERIAL_TYPES_CREATE():
    return str(uuid4())


AUTH_DATA_ADMIN = {
    'login': 'admin',
    'password': 'admin'
}

AUTH_DATA_FAIL_LENGTH_LOGIN_ADMIN = {
    'login': str(uuid4()) * 7,
    'password': 'admin'
}

AUTH_DATA_FAIL_LENGTH_PASSWORD_ADMIN = {
    'login': 'admin',
    'password': str(uuid4()) * 7
}

AUTH_DATA_FAIL_LOGIN_PASSWORD_ERROR = {
    'login': 'admin',
    'password': str(uuid4())
}

AUTH_DATA_LENGTH_TOKEN = str(uuid4()) * 7

AUTH_DATA_FAIL_BAD_ID = random.uniform(-1, -10)

DATA_UNITS_MEASUREMENT_VOLUME_ID = random.randint(1, 18)

AUTH_DATA_FAIL_BAD_TOKEN = str(uuid4())

AUTH_DATA_FAIL_NOT_FOUND_ID = random.randint(1000000, 9999999)

AUTH_DATA_FAIL_BAD_PASSWORD = str(random.randrange(1, 9999))

AUTH_DATA_FAIL_LENGTH_MATERIAL_TYPES = str(uuid4()) * 7

DATA_VENDORS_RANDOM_NAME_1_TO_30 = str(random.randint(1, 999999999999999999999999999999))

DATA_LEGAL_ENTITIES_TYPES_RANDOM = random.randint(1, 6)

DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20 = str(random.randint(1, 99999999999999999999))

DATA_HISTORY_OPERATION_DEBT_CONFIRMED_RANDOM_0_TO_1 = random.randint(0, 1)

DATA_HISTORY_OPERATION_SUM_RANDOM = float(random.randint(1, 999999999))

DATA_HISTORY_OPERATION_COMMENT_LENGTH = str(uuid4()) * 28

AUTH_DATA_FAIL_EMPTY_FIELDS = {
    'login': '',
    'email': '',
    'password': '',
    'token': ''
}

AUTH_DATA_FAIL_EMPTY_TOKEN = {
    'login': 'admin',
    'password': 'admin',
    'token': ''
}

AUTH_DATA_FAIL_LENGTH_TOKEN = {
    'login': 'admin',
    'password': 'admin',
    'token': str(uuid4()) * 7
}

AUTH_DATA_FAIL_NOT_FOUND_TOKEN = {
    'login': 'admin',
    'password': 'admin',
    'token': str(uuid4())
}

AUTH_DATA_CREATE_FAIL_LENGTH_TOKEN = {
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()) * 7,
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_CREATE_FAIL_LENGTH_LOGIN = {
    'login': str(uuid4()) * 7,
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_CREATE_FAIL_LENGTH_PASSWORD = {
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()) * 7,
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_CREATE_FAIL_LENGTH_EMAIL = {
    'login': str(uuid4()),
    'email': str(uuid4()) * 7 + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_CREATE_FAIL_NOT_FOUND_TOKEN = {
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_UPDATE_INFO_LENGTH_TOKEN = {
    'id': 1,
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()) * 7,
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_UPDATE_INFO_LENGTH_LOGIN = {
    'id': 1,
    'login': str(uuid4()) * 7,
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_UPDATE_INFO_LENGTH_EMAIL = {
    'id': 1,
    'login': str(uuid4()),
    'email': str(uuid4()) * 7 + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_UPDATE_INFO_LENGTH_PASSWORD = {
    'id': 1,
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()) * 7,
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_UPDATE_INFO_NOT_FOUND_TOKEN = {
    'id': 1,
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': random.randint(1000000, 9999999)
}

AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_ID = {
    'id': random.uniform(-1, -10),
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'token': 1,
    'user_id': 1
}

AUTH_DATA_UPDATE_INFO_NOT_FOUND_ID = {
    'id': random.randint(100000000, 999999999),
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(uuid4()),
    'user_id': 1
}

AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_EMAIL = {
    'id': 1,
    'login': str(uuid4()),
    'email': str(random.randint(1, 100)),
    'password': str(uuid4()),
    'token': str(uuid4()),
    'user_id': 1
}

AUTH_DATA_UPDATE_INFO_BAD_REQUEST_BAD_PASSWORD = {
    'id': 1,
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(random.randint(1, 1000)),
}

AUTH_CREATE_FAIL_BAD_EMAIL = {
    'login': str(uuid4()),
    'email': str(uuid4()),
    'password': str(uuid4()),
}

AUTH_DATA_CREATE_FAIL_PASSWORD = {
    'login': str(uuid4()),
    'email': str(uuid4()) + '@it-paradise.com',
    'password': str(random.randrange(0, 9999)),
}

AUTH_DATA_CREATE_FAIL_BUSY_EMAIL_LOGIN = {
    'login': 'admin',
    'email': 'admin@it-paradise.ru',
    'password': str(uuid4()),
}

DATA_UNITS_MEASUREMENT_VOLUME_GET_ALL = {
    "status": "OK",
    "code": 200,
    "data": [
        {
            "id": 1,
            "name": "Метр"
        },
        {
            "id": 2,
            "name": "Километр"
        },
        {
            "id": 3,
            "name": "Дюйм"
        },
        {
            "id": 4,
            "name": "Квадратный крилометр"
        },
        {
            "id": 5,
            "name": "Ар"
        },
        {
            "id": 6,
            "name": "Гектар"
        },
        {
            "id": 7,
            "name": "Квадратный метр"
        },
        {
            "id": 8,
            "name": "Квадратный дециметр"
        },
        {
            "id": 9,
            "name": "Квадратный сантиметр"
        },
        {
            "id": 10,
            "name": "Квадратный дюйм"
        },
        {
            "id": 11,
            "name": "Кубический метр"
        },
        {
            "id": 12,
            "name": "Кубический дециметр"
        },
        {
            "id": 13,
            "name": "Гектолитр"
        },
        {
            "id": 14,
            "name": "Тонна"
        },
        {
            "id": 15,
            "name": "Килограмм"
        },
        {
            "id": 16,
            "name": "Грамм"
        },
        {
            "id": 17,
            "name": "Килловат-час"
        },
        {
            "id": 18,
            "name": "Килловат"
        }
    ]
}
