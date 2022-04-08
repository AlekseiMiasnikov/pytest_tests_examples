from api.api import API


class ApiUnitsMeasurementVolume(API):
    def get_all(self, data):
        return self.send_get(url=f'units-measurement-volume/get-all?token={data["token"]}&user_id={data["user_id"]}')

    def get_all_method_not_allowed(self):
        return self.send_post(url='units-measurement-volume/get-all?token=', data=[])
