"""
@file gui_interface.py
@brief Provides a simulated GUI interface.
@date 2025
"""

class GUIInterface:
    """
    @class GUIInterface
    @brief Simulates a graphical user interface.
    """

    def __init__(self, control_system):
        self.control_system = control_system

    def DisplayData(self, data):
        """
        @brief Displays sensor data.
        @param data List of measurements.
        """
        print("\n[GUI] Dane pomiarowe:")
        for m in data:
            print(f"Sensor {m.sensorId}, {m.measurementType}: {m.value:.2f} ({m.timestamp})")

    def GetTargetParameters(self):
        """
        @brief Retrieves target climate parameters.
        @return Dictionary with targets.
        """
        return {
            "Temperature": self.control_system.targetTemperature,
            "Humidity": self.control_system.targetHumidity,
            "CO2": self.control_system.targetCO2
        }

    def DisplayReport(self, report):
        """
        @brief Displays a climate report.
        @param report Report object.
        """
        print("\n[GUI] Raport:")
        print(report.generateRaport())
