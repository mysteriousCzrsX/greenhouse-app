import os
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class GreenhouseData(Base):
    """
    @brief ORM class representing a single greenhouse data record.

    Contains environmental readings including temperature, humidity, CO2, and N2 levels.
    """
    __tablename__ = 'greenhouse_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now(datetime.UTC))
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    co2 = Column(Float, nullable=False)
    n2 = Column(Float, nullable=False)

    def __repr__(self):
        """
        @brief String representation of the GreenhouseData instance.
        @return Formatted string with all field values.
        """
        return (f"<GreenhouseData(id={self.id}, timestamp={self.timestamp}, "
                f"temperature={self.temperature}, humidity={self.humidity}, "
                f"co2={self.co2}, n2={self.n2})>")

class GreenhouseDB:
    """
    @brief Database handler class for greenhouse environmental data.

    Provides methods to add and retrieve greenhouse sensor data using SQLite and SQLAlchemy.
    """

    def __init__(self, db_filename='greenhouse.db'):
        """
        @brief Constructor that sets up the database connection and creates tables if needed.

        @param db_filename Name of the SQLite database file.
        """
        db_exists = os.path.exists(db_filename)
        db_path = f"sqlite:///{db_filename}"
        self.engine = create_engine(db_path, echo=False)

        if not db_exists:
            Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)

    def add_data(self, temperature, humidity, co2, n2):
        """
        @brief Inserts a new row of environmental data into the database.

        @param temperature Temperature in degrees Celsius.
        @param humidity Relative humidity in percent.
        @param co2 CO2 concentration in ppm.
        @param n2 N2 concentration in ppm.
        """
        session = self.Session()
        try:
            data = GreenhouseData(
                temperature=temperature,
                humidity=humidity,
                co2=co2,
                n2=n2
            )
            session.add(data)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting data: {e}")
        finally:
            session.close()

    def get_all_data(self):
        """
        @brief Retrieves all greenhouse data records from the database.

        @return List of GreenhouseData objects.
        """
        session = self.Session()
        try:
            return session.query(GreenhouseData).all()
        finally:
            session.close()

    def get_latest_data(self):
        """
        @brief Retrieves the most recent greenhouse data record.

        @return A single GreenhouseData object or None if no records exist.
        """
        session = self.Session()
        try:
            return session.query(GreenhouseData).order_by(GreenhouseData.timestamp.desc()).first()
        finally:
            session.close()