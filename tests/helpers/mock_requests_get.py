def dealerrater_page(page: int) -> str:
    return f"https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page{page}/?filter=ONLY_POSITIVE#link"

def mock_requests_get(url):
    class MockResponse:
        def __init__(self, page_content, status_code):
            self.content = page_content
            self.status_code = status_code

    if url == 'http://test.com/reviews/page_1':
        with open('tests/fixtures/actual_reviews_page_1.html') as f:
            return MockResponse(f.read(), 200)
    elif url == dealerrater_page(1):
        with open('tests/fixtures/actual_reviews_page_1.html') as f:
            return MockResponse(f.read(), 200)
    elif url == dealerrater_page(2):
        with open('tests/fixtures/actual_reviews_page_2.html') as f:
            return MockResponse(f.read(), 200)
    elif url == dealerrater_page(3):
        with open('tests/fixtures/actual_reviews_page_3.html') as f:
            return MockResponse(f.read(), 200)
    elif url == dealerrater_page(4):
        with open('tests/fixtures/actual_reviews_page_4.html') as f:
            return MockResponse(f.read(), 200)
    elif url == dealerrater_page(5):
        with open('tests/fixtures/actual_reviews_page_5.html') as f:
            return MockResponse(f.read(), 200)

    return MockResponse(None, 404)
