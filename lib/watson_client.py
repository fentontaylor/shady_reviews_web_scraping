import os
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from dotenv import load_dotenv

load_dotenv()

class WatsonClient:
    def __init__(self) -> None:
        self.client = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=IAMAuthenticator(os.environ.get('WATSON_API_KEY')))
        self.client.set_service_url(os.environ.get('WATSON_URL'))

    def analyze(self, text: str):
        response = self.client.analyze(
            text=text,
            features=Features(sentiment=SentimentOptions()))
        return response.get_result()
