from api.api import API


class ApiIcons(API):
    def get_all(self, data):
        return self.send_get(url=f'icons/get-all?token={data["token"]}&limit={data["limit"]}'
                                 f'&offset={data["offset"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='icons/get-all?token=', data=[])
