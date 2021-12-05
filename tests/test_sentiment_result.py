import unittest
from lib.sentiment_result import SentimentResult

class TestSentimentResult(unittest.TestCase):
    def test_it_can_init_with_args(self):
        text = 'Super great and positive'
        sentiment = 'positive'
        score = 0.995
        sr = SentimentResult(text, sentiment, score)
        self.assertEqual(text, sr.text)
        self.assertEqual(sentiment, sr.sentiment)
        self.assertEqual(score, sr.score)

if __name__ == '__main__':
    unittest.main()
