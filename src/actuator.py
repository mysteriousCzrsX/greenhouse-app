from uuid import UUID

class Actuator:
    """
    @class Actuator
    @brief Represents a device controlling a climate parameter.
    """

    def __init__(self, actuatorId: int, actuatorType: str):
        self.actuatorId = actuatorId
        self.actuatorType = actuatorType

    def TurnOn(self):
        """
        @brief Turns the actuator on.
        """
        print(f"{self.actuatorType} ON")

    def TurnOff(self):
        """
        @brief Turns the actuator off.
        """
        print(f"{self.actuatorType} OFF")

    def SetValue(self, val):
        """
        @brief Sets actuator to a specific value.
        @param val Value to set.
        """
        print(f"{self.actuatorType} set to {val}")
