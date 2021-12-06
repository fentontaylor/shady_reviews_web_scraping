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

        with open('tests/fixtures/actual_reviews_page_1.html') as f:
            expected_content = f.read()

        self.assertEqual(expected_content, scraper.page_content)

    @mock.patch('lib.review_scraper.requests.get', side_effect=mock_requests_get)
    def test_review_contents(self, mock_get):
        url = 'http://test.com'
        expected_review_contents = [
            'Great service! No hassle, honest communication, and no back and forth fake bargaining experience. We’ll be back here for our next vehicle purchase.',
            'Adrian is hands down the best person who will see you through your car buying experience! Very professional, not pushy at all, and he will listen to what YOU want! He was patient with me and did not steer the sale like other local dealerships do. McKaig has a true gem of a person like Adrian on their team. I can make a recommendation here but I would strongly encourage you to rate them yourself! I believe we, as people, recommend ourselves and you won’t be disappointed with the inventory, Adrian, the finance guys, and the service altogether!',
            'Above and beyond. Feels like home when you walk in there. Best experience, a must go to. Will definitely be seeing us again.',
            'I had a wonderful experience as a first time buyer. I honestly was not confident I would walk out with a car but adrian helped me so much to achieve that goal. Everyone was very helpful and wonderful to work with. I definitely recommend Mckaig chevrolet buik!',
            'Me and my wife were in a pretty bad position, we only had one car and lived in Longview and I had just taking a position in Tyler and due to the pandemic our credit was really tough so finding someone to work with us was tough until we talked to Mckaig and they talked to and worked with on a personal level that no one else. We have two young kids so we able to do a lot of the shopping and paperwork over the phone with summer, which was awesome and the next day, we meet Adrian who treated us like family and every employee greeted and joked around with us my kids. We’re really grateful for everyone there for giving us a chance and treating us like people and not just bad credit scores!',
            'Came from Longview to look at a new car. Jeannie was very polite and effective. She was able to get me exactly what I needed.',
            'We purchased a 2019 Jeep Cherokee from Dennis on 11/23/21. He was very helpful in the buying process.',
            'We have finally met the sales team and it was FAN-xxxxxx-TASTIC!! We got to buy a new vehicle yesterday! Jeannie Evans is a gem! She helped me pick the truck we wanted, Freddie Thomlinson went above and beyond to help me find discounts to lower our finance amount and Taylor helped us to put the final touches in finance. If you are looking to buy from genuine people and want a GREAT deal, you most definately want to see these guys. You will NOT regret it! 10 stars out of 5!!',
            'Adrian was great! He went far and beyond to reach superb customer satisfaction. I am happily satisfied with my new vehicle. It was quick and painless and made the buying process easy. If you are looking for a new vehicle, I would definitely recommend anyone to go see Adrian at McKaig Chevrolet.',
            'Adrian is excellent. I didn’t get the exact deal I wanted, but close enough to make it work. I drove from Henderson and would do it again. I highly recommend you do the same.']

        scraper = ReviewScraper(url)
        scraper.fetch_page_content('/reviews/page_1')
        
        self.assertEqual(expected_review_contents, scraper.review_contents())

    def test_it_returns_empty_list_if_no_page_content(self):
        url = 'http://test.com'
        scraper = ReviewScraper(url)
        self.assertEqual([], scraper.review_contents())

if __name__ == '__main__':
    unittest.main()
