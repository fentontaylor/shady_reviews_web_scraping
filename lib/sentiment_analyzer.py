from lib.sentiment_result import SentimentResult
from lib.watson_client import WatsonClient

class SentimentAnalyzer:
    def __init__(self, text) -> None:
        self.text = text

    def analyze_text(self) -> SentimentResult:
        response = WatsonClient().analyze(self.text)
        sentiment = response['sentiment']['document']['label']
        score = response['sentiment']['document']['score']
        return SentimentResult(self.text, sentiment, score)
