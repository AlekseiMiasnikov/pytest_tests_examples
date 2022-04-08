import os
from os import getenv

import pytest
from selene import config, browser as driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from api import ApiAuth, ApiUsers, ApiMaterialTypes, ApiMaterial, ApiFiles, ApiLegalEntitiesTypes, ApiIcons, \
    ApiObjects, ApiUnitsMeasurementVolume, ApiVendors, ApiLegalEntities, ApiTime, ApiSettings, ApiPayments, \
    ApiHistoryOperation
from core.helpers import get_settings, remove_user, create_image
from data import AUTH_DATA_ADMIN, AUTH_CREATE, NAME_MATERIAL_TYPES_CREATE
from data.data import AUTH_DATA, DATA_UNITS_MEASUREMENT_VOLUME_ID, AUTH_DATA_FAIL_BAD_TOKEN, \
    AUTH_DATA_FAIL_BAD_PASSWORD, DATA_LEGAL_ENTITIES_TYPES_RANDOM, DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20, \
    DATA_AMOUNT_PAYMENTS_SUCCESS, DATA_PAYMENTS_TIMESTAMP
from models import MaterialTypes, Rights
from models.history_operation import HistoryOperation
from models.legal_entities import LegalEntities
from models.materials import Materials
from models.objects import Objects
from models.payments import Payments
from models.settings import Settings
from models.vendors import Vendors
from pages.LoginPage import LoginPage

admin = {
    'token': None,
    'id': None,
    'data': None
}

settings_config = {}


def pytest_sessionstart(session):
    global admin, settings_config
    settings_config = get_settings(environment=getenv('environment'))
    login_data = ApiAuth(settings_config).login(AUTH_DATA_ADMIN)['data']
    admin = {
        'token': login_data['token'],
        'id': login_data['id']
    }


def pytest_addoption(parser):
    parser.addoption("--remote", action="store", default='local', help="Run tests in selenoid docker")


@pytest.fixture(scope='session')
def browser(request):
    config.browser_name = getenv('browser')
    config.window_width = 1920
    config.window_height = 1080
    config.timeout = settings_config['TIMEOUT']
    if request.config.getoption("--remote") == 'docker':
        capabilities = {
            "browserName": getenv('browser'),
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        config.driver = webdriver.Remote(
            command_executor='http://192.168.0.2:4444/wd/hub/',
            desired_capabilities=capabilities
        )
    else:
        config.driver = webdriver.Chrome(ChromeDriverManager().install())
    config.base_url = settings_config['APPLICATION_URL']
    return driver


@pytest.fixture(scope='session')
def get_environment():
    return getenv('environment')


@pytest.fixture(scope='session')
def users():
    return ApiUsers(settings_config)


@pytest.fixture(scope='session')
def material_types():
    return ApiMaterialTypes(settings_config)


@pytest.fixture(scope='session')
def materials():
    return ApiMaterial(settings_config)


@pytest.fixture(scope='session')
def legal_entities_types():
    return ApiLegalEntitiesTypes(settings_config)


@pytest.fixture(scope='session')
def files():
    return ApiFiles(settings_config)


@pytest.fixture(scope='session')
def icons():
    return ApiIcons(settings_config)


@pytest.fixture(scope='session')
def objects():
    return ApiObjects(settings_config)


@pytest.fixture(scope='session')
def vendors():
    return ApiVendors(settings_config)


@pytest.fixture(scope='session')
def legal_entities():
    return ApiLegalEntities(settings_config)


@pytest.fixture(scope='session')
def time():
    return ApiTime(settings_config)


@pytest.fixture(scope='session')
def settings():
    return ApiSettings(settings_config)


@pytest.fixture(scope='session')
def payments():
    return ApiPayments(settings_config)


@pytest.fixture(scope='session')
def history_operation():
    return ApiHistoryOperation(settings_config)


@pytest.fixture(scope='session')
def units_measurement_volume():
    return ApiUnitsMeasurementVolume(settings_config)


@pytest.fixture(scope='session')
def auth_login():
    return ApiAuth(settings_config)


@pytest.fixture(scope='session')
def login_page(browser):
    return LoginPage(driver=browser)


@pytest.fixture(scope='function')
def create_admin(auth_login, users):
    user_data = AUTH_DATA()
    users.create({
        **user_data,
        'token': admin['token'],
        'user_id': admin['id'],
    })
    data = auth_login.login(user_data)['data']
    Rights().create(user_id=data['id'], is_admin=1)
    yield {
        'token': data['token'],
        'id': data['id'],
        'user': user_data
    }
    Rights().delete().where(Rights.user_id == data['id']).execute()
    remove_user(users, user_id=admin['id'], token=admin['token'], id=data['id'])


@pytest.fixture(scope='function')
def material_types_name_allready_exist(create_admin, material_types):
    name = NAME_MATERIAL_TYPES_CREATE()
    material_types.create({
        'name': name,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
        'units_measurement_volume_id': 1
    })
    yield {
        'name': name,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
        'units_measurement_volume_id': 1
    }
    MaterialTypes().delete().where(MaterialTypes.name == name).execute()


@pytest.fixture(scope='function')
def materials_name_allready_exist(create_admin, materials, create_and_remove_material_type):
    name = NAME_MATERIAL_TYPES_CREATE()
    materials.create({
        'token': create_admin['token'],
        'type_id': create_and_remove_material_type,
        'name': name,
        'user_id': create_admin['id']
    })
    yield {
        'token': create_admin['token'],
        'type_id': create_and_remove_material_type,
        'name': name,
        'user_id': create_admin['id']
    }
    Materials().delete().where(Materials.name == name).execute()


@pytest.fixture(scope='function')
def objects_name_allready_exist(create_admin, objects):
    name = NAME_MATERIAL_TYPES_CREATE()
    objects.create({
        'token': create_admin['token'],
        'name': name,
        'user_id': create_admin['id']
    })
    yield {
        'token': create_admin['token'],
        'name': name,
        'user_id': create_admin['id']
    }
    Objects().delete().where(Objects.name == name).execute()


@pytest.fixture(scope='function')
def create_user_token_admin_id_user_delete(create_admin, users):
    user_data = users.create({
        **AUTH_CREATE(),
        'token': create_admin['token'],
        'user_id': create_admin['id'],
    })
    yield {
        'id': user_data['data']['id'],
        'password': AUTH_DATA_ADMIN['password'],
        'token': create_admin['token'],
        'user_id': create_admin['id'],
    }
    remove_user(
        users=users,
        id=user_data['data']['id'],
        token=create_admin['token'],
        user_id=create_admin['id'],
    )


@pytest.fixture(scope='function')
def create_login_delete_user(auth_login, create_admin, users):
    data = AUTH_CREATE()
    users.create({
        **data,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
    })
    user_token = auth_login.login({
        'login': data['login'],
        'password': data['password']
    })['data']
    yield {
        'token': user_token['token'],
        'password': data['password'],
        'id': user_token['id'],
        'user_id': create_admin['id']
    }
    remove_user(
        users=users,
        id=user_token['id'],
        token=create_admin['token'],
        user_id=create_admin['id'],
    )


@pytest.fixture(scope='function')
def delete_user(create_admin, users):
    def wrapper(id):
        remove_user(
            users=users,
            id=id, token=create_admin['token'],
            user_id=create_admin['id']
        )

    return wrapper


@pytest.fixture(scope='function')
def remove_material_type():
    def wrapper(name):
        MaterialTypes().delete().where(MaterialTypes.name == name).execute()

    return wrapper


@pytest.fixture(scope='function')
def remove_materials():
    def wrapper(name):
        Materials().delete().where(Materials.name == name).execute()

    return wrapper


@pytest.fixture(scope='function')
def remove_objects():
    def wrapper(name):
        Objects().delete().where(Objects.name == name).execute()

    return wrapper


@pytest.fixture(scope='function')
def remove_vendors():
    def wrapper(name):
        Vendors().delete().where(Vendors.name == name).execute()

    return wrapper


@pytest.fixture(scope='function')
def remove_legal_entities():
    def wrapper(name):
        LegalEntities().delete().where(LegalEntities.name == name).execute()

    return wrapper


@pytest.fixture(scope='function')
def remove_payments():
    def wrapper(vendor_id):
        Payments().delete().where(Payments.vendor_id == vendor_id).execute()

    return wrapper


@pytest.fixture(scope='function')
def remove_history_operation():
    def wrapper(comment):
        HistoryOperation().delete().where(HistoryOperation.comment == comment).execute()

    return wrapper


@pytest.fixture(scope='function')
def create_and_remove_material_type(create_admin, material_types, remove_material_type):
    mt_name = NAME_MATERIAL_TYPES_CREATE()
    material_types.create({
        'name': mt_name,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
        'units_measurement_volume_id': DATA_UNITS_MEASUREMENT_VOLUME_ID
    })
    mt_id = MaterialTypes().get(MaterialTypes.name == mt_name).id
    yield mt_id
    MaterialTypes().delete().where(MaterialTypes.id == mt_id).execute()


@pytest.fixture(scope='function')
def create_and_remove_materials(create_admin, materials, remove_material_type):
    mt_name = NAME_MATERIAL_TYPES_CREATE()
    materials.create({
        'token': create_admin['token'],
        'type_id': create_and_remove_material_type,
        'name': mt_name,
        'user_id': create_admin['id']
    })
    mt_id = Materials().get(Materials.name == mt_name).id
    yield mt_id
    Materials().delete().where(Materials.id == mt_id).execute()


@pytest.fixture(scope='function')
def create_material_type_materials_remove(create_admin, materials, create_and_remove_material_type,
                                          remove_materials):
    name = NAME_MATERIAL_TYPES_CREATE()
    materials.create({
        'token': create_admin['token'],
        'type_id': create_and_remove_material_type,
        'name': name,
        'user_id': create_admin['id']
    })
    material_id = Materials().get(Materials.name == name).id
    yield material_id
    Materials().delete().where(Materials.id == material_id).execute()


@pytest.fixture(scope='function')
def create_objects_remove(create_admin, objects, remove_objects):
    name = AUTH_DATA_FAIL_BAD_TOKEN
    objects.create({
        'token': create_admin['token'],
        'name': name,
        'user_id': create_admin['id']
    })
    object_id = Objects().get(Objects.name == name).id
    yield object_id
    remove_objects(name)


@pytest.fixture(scope='function')
def create_objects_delete_remove(create_admin, objects, remove_objects):
    name = AUTH_DATA_FAIL_BAD_TOKEN
    objects.create({
        'token': create_admin['token'],
        'name': name,
        'user_id': create_admin['id']
    })
    object_id = Objects().get(Objects.name == name).id
    objects.delete({
        'id': object_id,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
    })
    yield object_id
    remove_objects(name)


@pytest.fixture(scope='function')
def create_vendors_remove(create_admin, vendors, remove_vendors):
    name = AUTH_DATA_FAIL_BAD_PASSWORD
    vendors.create({
        'token': create_admin['token'],
        'name': name,
        'icon_id': 1,
        'user_id': create_admin['id']
    })
    vendor_id = Vendors().get(Vendors.name == name).id
    yield vendor_id
    remove_vendors(name)


@pytest.fixture(scope='function')
def create_vendors_delete_remove(create_admin, vendors, remove_vendors):
    name = AUTH_DATA_FAIL_BAD_PASSWORD
    vendors.create({
        'token': create_admin['token'],
        'name': name,
        'icon_id': 1,
        'user_id': create_admin['id']
    })
    vendor_id = Vendors().get(Vendors.name == name).id
    vendors.delete({
        'id': vendor_id,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
    })
    yield vendor_id
    remove_vendors(name)


@pytest.fixture(scope='function')
def create_legal_entities_remove(create_admin, legal_entities, remove_legal_entities):
    name = DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20
    legal_entities.create({
        'token': create_admin['token'],
        'name': name,
        "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
        'user_id': create_admin['id']
    })
    legal_entities_id = LegalEntities().get(LegalEntities.name == name).id
    yield legal_entities_id
    remove_legal_entities(name)


@pytest.fixture(scope='function')
def create_legal_entities_delete_remove(create_admin, legal_entities, remove_legal_entities):
    name = DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20
    legal_entities.create({
        'token': create_admin['token'],
        'name': name,
        "legal_entities_type_id": DATA_LEGAL_ENTITIES_TYPES_RANDOM,
        'user_id': create_admin['id']
    })
    legal_entities_id = LegalEntities().get(LegalEntities.name == name).id
    legal_entities.delete({
        'id': legal_entities_id,
        'token': create_admin['token'],
        'user_id': create_admin['id'],
    })
    yield legal_entities_id
    remove_legal_entities(name)


@pytest.fixture(scope='function')
def active_settings():
    Settings.update(active=1).where(Settings.name == 'debt').execute()


@pytest.fixture(scope='function')
def disable_settings():
    Settings.update(active=0).where(Settings.name == 'debt').execute()


@pytest.fixture(scope='function')
def generate_image():
    path = create_image(
        type='png',
        size=(500, 500),
        name=AUTH_DATA_FAIL_BAD_TOKEN
    )
    yield path
    os.remove(path)


@pytest.fixture(scope='function')
def create_payment_remove(create_admin, payments, create_vendors_remove, create_legal_entities_remove, remove_payments):
    vendor_id = create_vendors_remove
    amount = 9999999
    payments.create({
        "token": create_admin['token'],
        "vendor_id": vendor_id,
        "legal_entity_id": create_legal_entities_remove,
        "amount": amount,
        "created_at": DATA_PAYMENTS_TIMESTAMP,
        "user_id": create_admin['id']
    })
    payment_id = Payments.get(Payments.amount == amount)
    yield payment_id
    remove_payments(vendor_id)


@pytest.fixture(scope='function')
def create_vendor_legal_entity_payment_remove(create_admin, payments, remove_payments, vendors, remove_vendors,
                                              legal_entities, remove_legal_entities):
    vendor = AUTH_DATA_FAIL_BAD_PASSWORD
    vendors.create({
        'token': create_admin['token'],
        'name': vendor,
        'icon_id': 1,
        'user_id': create_admin['id']
    })
    vendor_id = Vendors().get(Vendors.name == vendor).id

    legal_entity = DATA_LEGAL_ENTITIES_RANDOM_NAME_1_TO_20
    legal_entities.create({
        'token': create_admin['token'],
        'name': legal_entity,
        "legal_entities_type_id": 6,
        'user_id': create_admin['id']
    })
    legal_entities_id = LegalEntities().get(LegalEntities.name == legal_entity).id

    amount = DATA_AMOUNT_PAYMENTS_SUCCESS
    created_at = DATA_PAYMENTS_TIMESTAMP
    payments.create({
        "token": create_admin['token'],
        "vendor_id": vendor_id,
        "legal_entity_id": legal_entities_id,
        "amount": amount,
        "created_at": created_at,
        "user_id": create_admin['id']
    })
    payment_id = Payments.get(Payments.created_at == created_at)
    yield {
        'id': payment_id,
        'vendor_id': vendor_id,
        'vendor': vendor,
        "amount": amount,
        "created_at": created_at,
        "legal_entity_id": legal_entities_id,
        "legal_entity": legal_entity,
        "legal_entity_type": "ИП",
        "legal_entities_type_id": 6
    }
    remove_vendors(vendor)
    remove_legal_entities(legal_entity)
    remove_payments(vendor_id)
