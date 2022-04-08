from api.api import API


class ApiUsers(API):
    def get_all(self, data):
        return self.send_get(url=f'users/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self, token):
        return self.send_post(url=f'users/get-all?token={token}', data=[])

    def get_info(self, data):
        return self.send_get(url=f'users/get-info?token={data["token"]}&user_id={data["user_id"]}')

    def get_info_method_not_allowed(self, token):
        return self.send_post(url=f'users/get-info?token={token}', data=[])

    def create(self, data):
        return self.send_post(url='users/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='users/create')

    def delete(self, data):
        return self.send_delete(url='users/delete', data=data)

    def delete_method_not_allowed(self):
        return self.send_get(url='users/delete')

    def update_info(self, data):
        return self.send_put(url='users/update-info', data=data)

    def update_info_method_not_allowed(self):
        return self.send_get(url='users/update-info')

    def change_password(self, data):
        return self.send_put(url='users/change-password', data=data)

    def change_password_mehtod_not_allowed(self):
        return self.send_get(url='users/change-password')
