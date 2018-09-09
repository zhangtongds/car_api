import requests
import json
import pprint
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

headers = {
    'Content-Type': 'application/json'
}
app = Flask(__name__)
base_url = 'http://gmapi.azurewebsites.net/'

@app.route('/vehicles/<car_id>', methods=['GET'])
def get_vehicle_info(car_id):
    
    """
    Make request to GM api for vehicle information
    and return results in Smartcar API format.
    """
    vehicle_info_url = base_url + 'getVehicleInfoService'
    search_param = {
        'id': car_id,
        'responseType': 'JSON'
    }
    data = requests.post(vehicle_info_url, data=json.dumps(search_param), headers=headers)
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
    return jsonify(smartcar_vehicle_info)


def get_security_status(car_id, response_type):

    """
    Make request to GM api for security status
    and return results in Smartcar API format.
    """

    pass

    



# print(data)
#get_vehicle_info("1234")

if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(host = '0.0.0.0')