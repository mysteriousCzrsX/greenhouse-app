from typing import List
from measurement import Measurement
from db_ctrl import Database
from sensor import Sensor
from actuator import Actuator
from time import sleep

class ControlSystem:
    """
    @class ControlSystem
    @brief Controls the greenhouse environment.
    """

    def __init__(self):
        self.targetTemperature = 0
        self.targetHumidity = 0
        self.targetCO2 = 0
        self.targetN2 = 0
        self.database = Database()

    def loop():
        """
        @brief Mani control loop
        """
        while True:
            sleep(3)

    def monitorParameters(self, sensors: List[Sensor]) -> List[Measurement]:
        """
        @brief Collects data from all sensors.
        @param sensors List of sensor objects.
        @return List of Measurement objects.
        """
        measurements = [s.readData() for s in sensors]
        for m in measurements:
            print(f"{m.measurementType}: {m.value:.2f}")
        return measurements

    def controlParameters(self, actuators: List[Actuator], measurements: List[Measurement]):
        """
        @brief Controls actuators based on measurements.
        @param actuators List of actuators.
        @param measurements List of measurements.
        """
        for m in measurements:
            for a in actuators:
                if m.measurementType.lower() in a.actuatorType.lower():
                    if m.value < 20:
                        a.TurnOn()
                    elif m.value > 30:
                        a.TurnOff()

    def saveToDatabase(self, measurements: List[Measurement]):
        """
        @brief Saves all measurements to the database.
        @param measurements List of measurements.
        """
        self.database.Connect()
        for m in measurements:
            self.database.SaveMeasurement(m)
        self.database.Disconnect()

    def getTargetValues(self):
        """
        @brief Gets the target values from the web server.
        """

        


if __name__ == "__main__":
    ctrl = ControlSystem()
    ctrl.loop()