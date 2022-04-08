from api.api import API


class ApiMaterial(API):
    def get_all(self, data):
        return self.send_get(url=f'materials/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='materials/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='materials/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='materials/create')

    def update(self, data):
        return self.send_put(url='materials/update', data=data)

    def update_method_not_allowed(self):
        return self.send_get(url='materials/update')
