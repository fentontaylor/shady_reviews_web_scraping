import unittest
from lib.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_it_can_init_with_arg(self):
        text = 'super great!'
        sa = SentimentAnalyzer(text)
        self.assertEqual(text, sa.text)

if __name__ == '__main__':
    unittest.main()
