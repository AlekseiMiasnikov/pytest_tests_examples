from api.api import API


class ApiTime(API):
    def get_timezones(self, data):
        return self.send_get(url=f'time/get-timezones?token={data["token"]}&user_id={data["user_id"]}')

    def get_timezones_method_not_allowed(self):
        return self.send_post(url='time/get-timezones?token=', data=[])

    def get_timezone(self, data):
        return self.send_get(url=f'time/get-timezone?token={data["token"]}&timezone_name={data["timezone_name"]}'
                                 f'&user_id={data["user_id"]}')

    def get_timezone_method_not_allowed(self):
        return self.send_post(url='time/get-timezone?token=', data=[])

    def set_timezone(self, data):
        return self.send_post(url='time/set-timezone', data=data)

    def set_timezone_method_not_allowed(self):
        return self.send_get(url='time/set-timezone')
