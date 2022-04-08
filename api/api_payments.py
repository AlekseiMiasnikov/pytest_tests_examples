from api.api import API
import urllib.parse


class ApiPayments(API):
    def get_all(self, data):
        url = urllib.parse.urlencode(data)
        return self.send_get(url=f'payments/get-all?{url}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='payments/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='payments/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='payments/create')

    def update(self, data):
        return self.send_put(url='payments/update', data=data)

    def update_method_not_allowed(self):
        return self.send_get(url='payments/update')

    def delete(self, data):
        return self.send_delete(url='payments/delete', data=data)

    def delete_method_not_allowed(self):
        return self.send_get(url='payments/delete')
