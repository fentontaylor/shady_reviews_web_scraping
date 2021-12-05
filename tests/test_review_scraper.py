import unittest
from unittest import mock
from lib.review_scraper import ReviewScraper

from tests.helpers.mock_requests_get import mock_requests_get

class TestReviewScraper(unittest.TestCase):
    def test_it_can_init_with_base_url(self):
        # Sets attribute without trailing slash
        url = 'http://test.com'

        scraper = ReviewScraper(url)
        self.assertEqual(url, scraper.base_url)

        scraper = ReviewScraper(url + '/')
        self.assertEqual(url, scraper.base_url)

    @mock.patch('lib.review_scraper.requests.get', side_effect=mock_requests_get)
    def test_fetch_page_content(self, mock_get):
        url = 'http://test.com'
        scraper = ReviewScraper(url)
        page_content = scraper.fetch_page_content('/reviews/page_1')
        with open('tests/fixtures/reviews_page_1.html') as f:
            expected_content = f.read()
        self.assertEqual(expected_content, page_content)

if __name__ == '__main__':
    unittest.main()
