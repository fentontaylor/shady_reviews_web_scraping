import random

def mock_watson_analyze(text: str):
    class MockAnalysis:
        def __init__(self, label: str, score: float) -> None:
            self.data = {
                'sentiment': {
                    'document': {
                        'label': label,
                        'score': score
                    }
                }
            }

    # These are the actual top 3 review comments, just randomize the rest
    if text == 'Love dealing at this dealership. Dennis was most helpful and efficient. Answered all our questions and knew every detail about the car. Am super pleased and will visit again.':
        return MockAnalysis('positive', 0.999427).data
    elif text == 'We had a great experience with Tito! He was helpful and friendly! Glad we got to work with him. Loving our new car!!':
        return MockAnalysis('positive', 0.999159).data
    elif text == 'No pressure sales. Fantastic experience. Tito went above and beyond in taking care of me and my family. Thanks to Tito I have my first sports car!!!':
        return MockAnalysis('positive', 0.998587).data
    
    return MockAnalysis('positive', random.uniform(0.9, 0.98)).data
