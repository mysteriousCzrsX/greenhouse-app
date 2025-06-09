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
        sensor_types = ["temperature", "humidity", "co2", "n2"]
        sensor_list = [Sensor(sensorId=i+1, sensorType=sensor_types[i % len(sensor_types)]) for i in range(4)]
        self.sensor_list = sensor_list
        actuator_list = [Actuator(actuatorId=i+1, actuatorType=sensor_types[i % len(sensor_types)]) for i in range(4)]
        self.actuator_list = actuator_list
        self.database = Database()

    def loop(self):
        """
        @brief Mani control loop
        """
        while True:
            curr_measurements = self.monitorParameters()
            self.saveToDatabase(curr_measurements)
            self.getTargetValues()
            self.controlParameters()
            sleep(3)

    def monitorParameters(self) -> List[Measurement]:
        """
        @brief Collects data from all sensors.
        @param sensors List of sensor objects.
        @return List of Measurement objects.
        """
        measurements = [s.readData() for s in self.sensor_list]
        for m in measurements:
            print(f"{m.measurementType}: {m.value:.2f}")
        return measurements

    def controlParameters(self):
        """
        @brief Controls actuators based on setpoints.
        @param actuators List of actuators.
        @param measurements List of measurements.
        """
        return

    def saveToDatabase(self, measurements: List[Measurement]):
        """
        @brief Saves all measurements to the database.
        @param measurements List of measurements.
        """
        for m in measurements:
            if m.measurementType == "temperature":
                temperature = m.value
            if m.measurementType == "humidity":
                humidity = m.value
            if m.measurementType == "co2":
                co2 = m.value
            if m.measurementType == "n2":
                n2 = m.value
        self.database.add_data(temperature, humidity, co2, n2)

    def getTargetValues(self):
        """
        @brief Gets the target values from the web server.
        """
        return


if __name__ == "__main__":
    ctrl = ControlSystem()
    ctrl.loop()