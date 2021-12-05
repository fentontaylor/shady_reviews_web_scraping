def mock_requests_get(url):
    class MockResponse:
        def __init__(self, page_content, status_code):
            self.content = page_content
            self.status_code = status_code

    if url == 'http://test.com/reviews/page_1':
        with open('tests/fixtures/reviews_page_1.html') as f:
            return MockResponse(f.read(), 200)

    return MockResponse(None, 404)
