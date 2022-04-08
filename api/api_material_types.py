from api.api import API


class ApiMaterialTypes(API):
    def get_all(self, data):
        return self.send_get(url=f'material-types/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='material-types/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='material-types/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='material-types/create')

    def update(self, data):
        return self.send_put(url='material-types/update', data=data)

    def update_method_not_allowed(self):
        return self.send_get(url='material-types/update')
