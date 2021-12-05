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

        self.assertIsNone(scraper.page_content)

        scraper.fetch_page_content('/reviews/page_1')

        with open('tests/fixtures/mock_reviews_page_1.html') as f:
            expected_content = f.read()

        self.assertEqual(expected_content, scraper.page_content)

    @mock.patch('lib.review_scraper.requests.get', side_effect=mock_requests_get)
    def test_review_contents(self, mock_get):
        url = 'http://test.com'
        expected_review_contents = [
            "Great service! No hassle, honest communication, and no back and forth fake bargaining experience. We’ll be back here for our next vehicle purchase.",
            "Adrian is hands down the best person who will see you through your car buying experience! Very professional, not pushy at all, and he will listen to what YOU want! He was patient with me and did not steer the sale like other local dealerships do. McKaig has a true gem of a person like Adrian on their team. I can make a recommendation here but I would strongly encourage you to rate them yourself! I believe we, as people, recommend ourselves and you won’t be disappointed with the inventory, Adrian, the finance guys, and the service altogether!",
            "Above and beyond. Feels like home when you walk in there. Best experience, a must go to. Will definitely be seeing us again."
        ]

        scraper = ReviewScraper(url)
        scraper.fetch_page_content('/reviews/page_1')
        
        self.assertEqual(expected_review_contents, scraper.review_contents())

    def test_it_returns_empty_list_if_no_page_content(self):
        url = 'http://test.com'
        scraper = ReviewScraper(url)
        self.assertEqual([], scraper.review_contents())

if __name__ == '__main__':
    unittest.main()
