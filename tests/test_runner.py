import unittest
from unittest.mock import patch

from tests.helpers.mock_requests_get import mock_requests_get
from tests.helpers.mock_watson_analyze import mock_watson_analyze
from lib.runner import run

class TestRunner(unittest.TestCase):
    @patch('lib.review_scraper.requests.get', side_effect=mock_requests_get)
    @patch('lib.watson_client.WatsonClient.analyze', side_effect=mock_watson_analyze)
    def test_script_runner(self, mock_watson, mock_get):
        # This test is just for manual observation of runner script with mocked requests
        run()

if __name__ == '__main__':
    unittest.main()
