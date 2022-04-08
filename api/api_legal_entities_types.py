from api.api import API


class ApiLegalEntitiesTypes(API):
    def get_all(self, data):
        return self.send_get(url=f'legal-entities-types/get-all?token={data["token"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='legal-entities-types/get-all?token=', data=[])
