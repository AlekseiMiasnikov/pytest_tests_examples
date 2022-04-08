from api.api import API


class ApiFiles(API):
    def upload_avatar(self, data, file):
        return self.send_post(url='files/upload-avatar', data=data, files=file)

    def upload_avatar_method_not_allowed(self):
        return self.send_get(url='files/upload-avatar')
