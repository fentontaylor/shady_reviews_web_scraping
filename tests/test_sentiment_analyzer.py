import unittest
from unittest.mock import patch

from lib.sentiment_analyzer import SentimentAnalyzer
from lib.watson_client import WatsonClient

class TestSentimentAnalyzer(unittest.TestCase):
    def test_it_can_init_with_arg(self):
        text = 'super great!'
        sa = SentimentAnalyzer(text)
        self.assertEqual(text, sa.text)

    @patch.object(WatsonClient, 'analyze')
    def test_it_can_analyze_text_with_watson_api(self, mock_watson_client_analyze):
        text = 'super great!'
        sentiment = 'positive'
        score = 0.993

        mock_watson_client_analyze.return_value = {'sentiment': {'document': {'label': sentiment, 'score': score}}}
        analyzer = SentimentAnalyzer(text)
        sentiment_result = analyzer.analyze_text()

        self.assertEqual(text, sentiment_result.text)
        self.assertEqual(sentiment, sentiment_result.sentiment)
        self.assertEqual(score, sentiment_result.score)

if __name__ == '__main__':
    unittest.main()
