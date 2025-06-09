from datetime import datetime
from typing import List
from uuid import UUID
import random

class Measurement:
    """
    @class Measurement
    @brief Represents a sensor measurement.
    """

    def __init__(self, measurementId: int, sensorId: int, timestamp: datetime, value: float, measurementType: str):
        """
        @brief Constructor.
        @param measurementId Unique identifier for the measurement.
        @param sensorId ID of the sensor that took the measurement.
        @param timestamp Time of the measurement.
        @param value Measured value.
        @param measurementType Type of the measurement (e.g., Temperature).
        """
        self.measurementId = measurementId
        self.sensorId = sensorId
        self.timestamp = timestamp
        self.value = value
        self.measurementType = measurementType
