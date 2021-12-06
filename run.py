from lib.review_scraper import ReviewScraper
from lib.sentiment_analyzer import SentimentAnalyzer
from lib.watson_client import WatsonClient

def run():
    review_texts = []
    scraper = ReviewScraper('https://www.dealerrater.com')
    
    for page_number in range(1, 6):
        print(f"Fetching page {page_number} of reviews")
        scraper.fetch_page_content(f"/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page{page_number}/?filter=ONLY_POSITIVE#link")
        review_texts += scraper.review_contents()
    
    results = []
    text_number = 1
    n = len(review_texts)

    for text in review_texts:
        print(f"Analyzing text {text_number}/{n}")
        results.append(SentimentAnalyzer(text).analyze_text())
        text_number += 1

    filtered = list(filter(lambda sr: sr.sentiment == 'positive', results))
    filtered.sort(key=lambda sr: sr.score, reverse=True)

    print('\n' + '*' * 24 + ' RESULTS ' + '*' * 24 + '\n')

    for result in filtered[0:3]:
        print("%s\n" % result)

if __name__ == '__main__':
    run()
