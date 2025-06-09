import unittest
from unittest.mock import patch
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from sensor import Sensor
from measurement import Measurement

class Measurement:
    def __init__(self, measurementId, sensorId, timestamp, value, sensorType):
        self.measurementId = measurementId
        self.sensorId = sensorId
        self.timestamp = timestamp
        self.value = value
        self.sensorType = sensorType 

class TestSensor(unittest.TestCase):

    def setUp(self):
        self.sensor_id = 1
        self.sensor_type = "temperature"
        self.sensor = Sensor(self.sensor_id, self.sensor_type)

    def test_sensor_initialization(self):
        self.assertEqual(self.sensor.sensorId, self.sensor_id)
        self.assertEqual(self.sensor.sensorType, self.sensor_type)

    @patch('sensor.Measurement', side_effect=Measurement)
    def test_read_data_returns_measurement(self):
        measurement = self.sensor.readData()
        self.assertIsInstance(measurement, Measurement)
        self.assertEqual(measurement.sensorId, self.sensor_id)
        self.assertEqual(measurement.sensorType, self.sensor_type)
        self.assertTrue(15.0 <= measurement.value <= 35.0)
        self.assertIsInstance(measurement.timestamp, datetime)


if __name__ == '__main__':
    unittest.main()
