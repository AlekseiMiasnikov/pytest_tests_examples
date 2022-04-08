from api.api import API
# import urllib.parse


class ApiHistoryOperation(API):
    # def get_all(self, data):
    #     url = urllib.parse.urlencode(data)
    #     return self.send_get(url=f'history-operation/get-all?{url}')
    #
    # def get_all_method_not_allowed(self):
    #     return self.send_post(url='history-operation/get-all?token=', data=[])

    def create(self, data):
        return self.send_post(url='history-operation/create', data=data)

    def create_method_not_allowed(self):
        return self.send_get(url='history-operation/create')

    # def update(self, data):
    #     return self.send_put(url='history-operation/update', data=data)
    #
    # def update_method_not_allowed(self):
    #     return self.send_get(url='history-operation/update')
    #
    # def delete(self, data):
    #     return self.send_delete(url='history-operation/delete', data=data)
    #
    # def delete_method_not_allowed(self):
    #     return self.send_get(url='history-operation/delete')
