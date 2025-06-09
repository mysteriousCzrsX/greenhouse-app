import unittest
import warnings
import os
from src.web_server import app

class GreenhouseAppTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up a test client before each test.
        """
        app.config['TESTING'] = True
        self.client = app.test_client()
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        """
        Clean up any test-generated files.
        """
        if os.path.exists("greenhouse_report.txt"):
            os.remove("greenhouse_report.txt")

    def test_home_redirects_to_data(self):
        """
        Test that accessing '/' redirects to '/data'.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/data', response.location)

    def test_display_data_route(self):
        """
        Test that the /data route returns expected content.
        """
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Measurement Data', response.data)

    def test_get_parameters_route(self):
        """
        Test that the /parameters route displays target parameters.
        """
        response = self.client.get('/parameters')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Target Parameters', response.data)
        self.assertIn(b'Temperature:', response.data)

    def test_generate_report_creates_file_and_page(self):
        """
        Test that the /report route creates a file and returns download link.
        """
        response = self.client.get('/report')
        self.assertEqual(response.status_code, 200)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        REPORT_PATH = os.path.join(BASE_DIR,"..","src","greenhouse_report.txt")
        self.assertTrue(os.path.exists(REPORT_PATH))
        self.assertIn(b'Download Report', response.data)

    def test_download_report_route(self):
        """
        Test that the /download route sends the report file.
        """
        # Ensure the file is generated first
        self.client.get('/report')
        response = self.client.get('/download')
        self.assertEqual(response.status_code, 200)
        self.assertIn('attachment; filename=greenhouse_report.txt', response.headers.get('Content-Disposition'))


if __name__ == '__main__':
    unittest.main()
