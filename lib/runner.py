from lib.review_scraper import ReviewScraper
from lib.sentiment_analyzer import SentimentAnalyzer

def run():
    print("\033[H\033[J") # clear screen
    review_texts = []
    scraper = ReviewScraper('https://www.dealerrater.com')

    for page_number in range(1, 6):
        print(f"Fetching page {page_number} of reviews...", end='\r')
        scraper.fetch_page_content(
            f"/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page{page_number}/?filter=ONLY_POSITIVE#link")
        review_texts += scraper.review_contents()

    results = []
    text_number = 1
    n = len(review_texts)
    # clear screen, clear line char wasn't working: print(..., end='\x1b[1K\r')
    print("\033[H\033[J")

    for text in review_texts:
        print(f"Analyzing text {text_number}/{n}...", end='\r')
        results.append(SentimentAnalyzer(text).analyze_text())
        text_number += 1

    filtered = list(filter(lambda sr: sr.sentiment == 'positive', results))
    filtered.sort(key=lambda sr: sr.score, reverse=True)

    print('*' * 24 + ' RESULTS ' + '*' * 24)

    for i, result in enumerate(filtered[0:3]):
        print(f"{i + 1}.\n" + "%s\n" % result)
