from uuid import UUID

class Actuator:
    """
    @class Actuator
    @brief Represents a device controlling a climate parameter.
    """

    def __init__(self, actuatorId: int, actuatorType: str, deviceFriendlyName: str):
        self.actuatorId = actuatorId
        self.actuatorType = actuatorType
        self.deviceFriendlyName = deviceFriendlyName

    def TurnOn(self):
        """
        @brief Turns the actuator on.
        """
        print(f"{self.deviceFriendlyName} ON")

    def TurnOff(self):
        """
        @brief Turns the actuator off.
        """
        print(f"{self.deviceFriendlyName} OFF")

    def SetValue(self, val):
        """
        @brief Sets actuator to a specific value.
        @param val Value to set.
        """
        print(f"{self.deviceFriendlyName} set to {val}")
