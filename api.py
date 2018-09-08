import requests

headers = {
    'Content-Type': 'application/json'
}

class SmartCarApi(object):
    """
    """

    def __init__(self):
        self.base_url = "/gmapi.azurewebsites.net/getVehicleInfoService"

    def get_vehicle_info(self, car_id, response_type):
        url_params = {
            'id': car_id
            'response_type': response_type
        }
        request_url = self.base_url + '?' + '&'.join(url_params)
        data = requests.get(request_url, headers = headers)
        return data
