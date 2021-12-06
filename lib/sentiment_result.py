class SentimentResult:
    def __init__(self, text: str, sentiment: str, score: float) -> None:
        self.text = text
        self.sentiment = sentiment
        self.score = score

    def __str__(self):
        return f"TEXT: {self.text}\nSENTIMENT: {self.sentiment}\nSCORE: {self.score}"
