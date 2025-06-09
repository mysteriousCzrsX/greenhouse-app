import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_ctrl import Database, Base  # Assuming your code is in `greenhouse_db.py`
from time import sleep

class GreenhouseDBTest(unittest.TestCase):
    """
    Unit tests for the GreenhouseDB class.
    """

    def setUp(self):
        """
        Set up an in-memory SQLite database for testing.
        """
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

        # Create a custom DB object using the in-memory engine
        self.db = Database()
        self.db.engine = self.engine
        self.db.Session = self.Session

    def test_add_and_get_all_data(self):
        """
        Test adding a record and retrieving all records.
        """
        self.db.add_data(temperature=23.5, humidity=60.2, co2=410.0, n2=78.1)
        all_data = self.db.get_all_data()
        self.assertEqual(len(all_data), 1)
        self.assertAlmostEqual(all_data[0].temperature, 23.5)
        self.assertAlmostEqual(all_data[0].humidity, 60.2)
        self.assertAlmostEqual(all_data[0].co2, 410.0)
        self.assertAlmostEqual(all_data[0].n2, 78.1)

    def test_get_latest_data(self):
        """
        Test retrieval of the most recent record.
        """
        self.db.add_data(temperature=20.0, humidity=50.0, co2=400.0, n2=77.0)
        sleep(1)
        self.db.add_data(temperature=25.0, humidity=55.0, co2=420.0, n2=79.0)
        latest = self.db.get_latest_data()
        self.assertIsNotNone(latest)
        self.assertAlmostEqual(latest.temperature, 25.0)
        self.assertAlmostEqual(latest.humidity, 55.0)
        self.assertAlmostEqual(latest.co2, 420.0)
        self.assertAlmostEqual(latest.n2, 79.0)

    def test_empty_database_returns_none(self):
        """
        Test behavior of get_latest_data on an empty database.
        """
        latest = self.db.get_latest_data()
        self.assertIsNone(latest)

if __name__ == '__main__':
    unittest.main()
