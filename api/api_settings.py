from api.api import API


class ApiSettings(API):
    def get_debt(self, data):
        return self.send_get(url=f'settings/get-debt?token={data["token"]}&user_id={data["user_id"]}')

    def get_debt_method_not_allowed(self):
        return self.send_post(url='settings/get-debt?token=', data=[])

    def set_debt(self, data):
        return self.send_post(url='settings/set-debt', data=data)

    def set_debt_method_not_allowed(self):
        return self.send_get(url='settings/set-debt')
