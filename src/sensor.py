from datetime import datetime
import random
from measurement import Measurement


class Sensor:
    """
    @class Sensor
    @brief Represents a climate sensor.
    """

    def __init__(self, sensorId: int, sensorType: str):
        self.sensorId = sensorId
        self.sensorType = sensorType

    def readData(self) -> Measurement:
        """
        @brief Simulates reading sensor data.
        @return Measurement object.
        """
        value = random.uniform(15.0, 35.0)
        return Measurement(0, self.sensorId, datetime.now(), value, self.sensorType)

