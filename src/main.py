"""
@file main.py
@brief Entry point of the greenhouse control application.
@date 2025
"""

from control_system import Sensor, Actuator, ControlSystem
from gui_interface import GUIInterface
from web_server import WebServer
from uuid import uuid4

if __name__ == "__main__":
    sensors = [
        Sensor(1, "Temperature"),
        Sensor(2, "Humidity")
    ]

    actuators = [
        Actuator(1, "TemperatureController", uuid4(), "Heater"),
        Actuator(2, "HumidityController", uuid4(), "Humidifier")
    ]

    system = ControlSystem(24.0, 50.0, 400.0)

    gui = GUIInterface(system)
    web = WebServer(system)

    measurements = system.monitorParameters(sensors)
    system.controlParameters(actuators, measurements)

    gui.DisplayData(measurements)
    web.DisplayData(measurements)

    system.saveToDatabase(measurements)

    report = system.generateReport(measurements)
    gui.DisplayReport(report)
    web.DisplayReport(report)
