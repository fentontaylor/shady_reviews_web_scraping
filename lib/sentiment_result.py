class SentimentResult:
    def __init__(self, text: str, sentiment: str, score: float) -> None:
        self.text = text
        self.sentiment = sentiment
        self.score = score
