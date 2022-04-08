from requests import get, post, put, delete
from allure import step


class API:
    def __init__(self, settings):
        self.settings = settings

    def _base_url(self):
        return self.settings['API_URL']

    @step('Отправка POST запроса на url - {url}')
    def send_post(self, data, url='/', files={}):
        return post(url=f'{self._base_url()}/{url}', data=data, files=files, verify=False).json()

    @step('Отправка GET запроса на url - {url}')
    def send_get(self, url='/'):
        return get(url=f'{self._base_url()}/{url}', verify=False).json()

    @step('Отправка DELETE запроса на url - {url}')
    def send_delete(self, data, url='/'):
        return delete(url=f'{self._base_url()}/{url}', data=data, verify=False).json()

    @step('Отправка PUT запроса на url - {url}')
    def send_put(self, data, url='/'):
        return put(url=f'{self._base_url()}/{url}', data=data, verify=False).json()
