from api.api import API


class ApiVendors(API):
    def get_all(self, data):
        return self.send_get(url=f'vendors/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&archive={data["archive"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='vendors/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='vendors/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='vendors/create')

    def delete(self, data):
        return self.send_delete(url='vendors/delete', data=data)

    def delete_method_not_allowed(self):
        return self.send_get(url='vendors/delete')

    def update(self, data):
        return self.send_put(url='vendors/update', data=data)

    def update_method_not_allowed(self):
        return self.send_get(url='vendors/update')

    def restore(self, data):
        return self.send_put(url='vendors/restore', data=data)

    def restore_method_not_allowed(self):
        return self.send_get(url='vendors/restore')
