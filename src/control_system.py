from datetime import datetime
from typing import List
from uuid import UUID
import random

class ControlSystem:
    """
    @class ControlSystem
    @brief Controls the greenhouse environment.
    """

    def __init__(self, targetTemperature: float, targetHumidity: float, targetCO2: float):
        self.targetTemperature = targetTemperature
        self.targetHumidity = targetHumidity
        self.targetCO2 = targetCO2
        self.database = Database()

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

    def generateReport(self, measurements: List[Measurement]) -> Raport:
        """
        @brief Generates a report.
        @param measurements List of measurements.
        @return Raport object.
        """
        raport = Raport(1, measurements)
        print(raport.generateRaport())
        return raport

    def saveToDatabase(self, measurements: List[Measurement]):
        """
        @brief Saves all measurements to the database.
        @param measurements List of measurements.
        """
        self.database.Connect()
        for m in measurements:
            self.database.SaveMeasurement(m)
        self.database.Disconnect()
