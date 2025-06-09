from datetime import datetime
from typing import List
from uuid import UUID
import random


class Actuator:
    """
    @class Actuator
    @brief Represents a device controlling a climate parameter.
    """

    def __init__(self, actuatorId: int, actuatorType: str, deviceGuid: UUID, deviceFriendlyName: str):
        self.actuatorId = actuatorId
        self.actuatorType = actuatorType
        self.deviceGuid = deviceGuid
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
