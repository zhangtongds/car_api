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
    # pprint.pprint(smartcar_vehicle_info)
    return jsonify(smartcar_vehicle_info)

@app.route('/vehicles/<car_id>/doors', methods=['GET'])
def get_security_status(car_id):

    """
    Make request to GM api for security status
    and return results in Smartcar API format.
    """

    security_status_url = base_url + 'getSecurityStatusService'
    search_param = {
        'id': car_id,
        'responseType': 'JSON'
    }
    data = requests.post(security_status_url, data=json.dumps(search_param), headers=headers)
    gm_data = data.json()
    # pprint.pprint(gm_data)
    smartcar_security_status = []
    for status in gm_data['data']['doors']['values']:
        smartcar_security_status.append({'location': status['location']['value'], 'locked': status['locked']['value']})
    pprint.pprint(smartcar_security_status)
    return jsonify(smartcar_security_status)

@app.route('/vehicles/<car_id>/fuel', methods=['GET'])
def get_tank_level(car_id):
    
    """
    Make request to GM api for tank level
    and return results in Smartcar API format.
    """
    energy_serice_url = base_url + 'getEnergyService'
    search_param = {
        'id': car_id,
        'responseType': 'JSON'
    }
    data = requests.post(energy_serice_url, data=json.dumps(search_param), headers=headers)
    gm_data = data.json()
    fuel = gm_data['data']['tankLevel']['value']
    fuel_level = {
                    'fuel': fuel
                    }
    # pprint.pprint(smartcar_vehicle_info)
    return jsonify(fuel_level)


@app.route('/vehicles/<car_id>/battery', methods=['GET'])
def get_battery_level(car_id):
    
    """
    Make request to GM api for battery level
    and return results in Smartcar API format.
    """
    energy_serice_url = base_url + 'getEnergyService'
    search_param = {
        'id': car_id,
        'responseType': 'JSON'
    }
    data = requests.post(energy_serice_url, data=json.dumps(search_param), headers=headers)
    gm_data = data.json()
    battery = gm_data['data']['batteryLevel']['value']
    battery_level = {
                    'battery': battery
                    }
    # pprint.pprint(smartcar_vehicle_info)
    return jsonify(battery_level)

@app.route('/vehicles/<car_id>/engine', methods=['POST'])
def change_engine_status(car_id):

    """
    Make request to GM api for engine status
    and change engine status in Smartcar API format.
    """

    engine_status_url = base_url + 'actionEngineService'
    change_engine = json.loads(request.data)
    search_param = {
            'id': car_id,
            'responseType': 'JSON'
        }
    if change_engine['action'].upper() == 'START':
        search_param['command'] = 'START_VEHICLE'
    elif change_engine['action'].upper() == 'STOP':
        search_param['command'] = 'STOP_VEHICLE'
    data = requests.post(engine_status_url, data=json.dumps(search_param), headers=headers)
    gm_data = data.json()
    engine_status = gm_data['actionResult']['status']
    action_status = {}
    if engine_status == "EXECUTED":
        action_status['action'] = 'success'
    elif engine_status == "FAILED":
        action_status['action'] = 'error'
    return jsonify(action_status)

        



if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(host = '0.0.0.0')