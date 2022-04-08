from api.api import API


class ApiObjects(API):
    def get_all(self, data):
        return self.send_get(url=f'objects/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&archive={data["archive"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='objects/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='objects/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='objects/create')

    def delete(self, data):
        return self.send_delete(url='objects/delete', data=data)

    def delete_method_not_allowed(self):
        return self.send_get(url='objects/delete')

    def update(self, data):
        return self.send_put(url='objects/update', data=data)

    def update_method_not_allowed(self):
        return self.send_get(url='objects/update')

    def restore(self, data):
        return self.send_put(url='objects/restore', data=data)

    def restore_method_not_allowed(self):
        return self.send_get(url='objects/restore')
