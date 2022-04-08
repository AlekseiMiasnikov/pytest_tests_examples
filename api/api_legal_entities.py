from api.api import API


class ApiLegalEntities(API):
    def get_all(self, data):
        return self.send_get(url=f'legal-entities/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&archive={data["archive"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='legal-entities/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='legal-entities/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='legal-entities/create')

    def delete(self, data):
        return self.send_delete(url='legal-entities/delete', data=data)

    def delete_method_not_allowed(self):
        return self.send_get(url='legal-entities/delete')

    def update(self, data):
        return self.send_put(url='legal-entities/update', data=data)

    def update_method_not_allowed(self):
        return self.send_get(url='legal-entities/update')

    def restore(self, data):
        return self.send_put(url='legal-entities/restore', data=data)

    def restore_method_not_allowed(self):
        return self.send_get(url='legal-entities/restore')
