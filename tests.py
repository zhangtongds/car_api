
import json
import server
import unittest

class SmartcarTestCase(unittest.TestCase):
    """
    Test cases for returned results from Flask server.
    """

    def test_vehicle_info(self):
        """
        Testing returned keys from vehicle info.
        """

        client = server.app.test_client()
        result = client.get('/vehicles/1235')
        self.assertIn(b'vin', result.data)
        self.assertIn(b'color', result.data)
        self.assertIn(b'driveTrain', result.data)
        self.assertIn(b'doorCount', result.data)

    def test_get_security_status(self):
        """
        Testing returned keys from security status.
        """

        client = server.app.test_client()
        result = client.get('/vehicles/1234/doors')
        self.assertIn(b'location', result.data)
        self.assertIn(b'locked', result.data)

    def test_get_tank_level(self):
        """
        Testing returned keys from fuel level.
        """

        client = server.app.test_client()
        result = client.get('/vehicles/1235/fuel')
        self.assertIn(b'fuel', result.data)

    def test_get_battery_level(self):
        """
        Testing returned keys from battery level.
        """

        client = server.app.test_client()
        result = client.get('/vehicles/1234/battery')
        self.assertIn(b'battery', result.data)


    def test_change_engine_status(self):
        """
        Testing returned keys from engine status.
        """

        client = server.app.test_client()
        result = client.post('/vehicles/1235/engine', data=json.dumps({'action': 'START'}))
        self.assertIn(b'action', result.data)

if __name__ == '__main__':
    unittest.main()
