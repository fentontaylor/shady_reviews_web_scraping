import unittest
from lib.review_scraper import ReviewScraper

class TestReviewScraper(unittest.TestCase):
    def test_it_can_init_with_base_url(self):
        url = 'http://test.com'
        scraper = ReviewScraper(url)
        self.assertEqual(url, scraper.base_url)


if __name__ == '__main__':
    unittest.main()
