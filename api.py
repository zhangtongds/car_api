import requests
import json
import pprint

headers = {
    'Content-Type': 'application/json'
}

class SmartCarApi(object):
    """
    """

    def __init__(self, ):
        self.base_url = 'http://gmapi.azurewebsites.net/getVehicleInfoService'

    # def get_vehicle_info_v1(info):
    #     car_id = info.split('/')[-1]
    #     self.get_vehicle_info(car_id, "JSON")

    def get_vehicle_info(self, car_id, response_type):
        """
        Make request to GM api for vehicle information
        and return results in Smartcar API format.
        """
        search_param = {
            'id': car_id,
            'responseType': response_type
        }
        data = requests.post(self.base_url, data=json.dumps(search_param), headers=headers)
        gm_data = data.json()
        vin = gm_data['data']['vin']['value']
        color = gm_data['data']['color']['value']
        door_count = None
        if gm_data['data']['fourDoorSedan']:
            door_count = 4
        if gm_data['data']['twoDoorCoupe']:
            door_count = 2
        drive_train = gm_data['data']['driveTrain']['value']
        smartcar_vehicle_info = {
                                'vin': vin,
                                'color': color,
                                'doorCount': door_count,
                                'driveTrain': drive_train
                                }
        pprint.pprint(smartcar_vehicle_info)
        return smartcar_vehicle_info


    

tester = SmartCarApi()

info = '/vehicles/:id'

tester.get_vehicle_info_v1(info)

tester.get_vehicle_info("1234", "JSON")

