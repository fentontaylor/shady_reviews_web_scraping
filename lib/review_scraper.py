import requests

class ReviewScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url[0:-1] if base_url[-1] == '/' else base_url

    def fetch_page_content(self, uri: str) -> str:
        url = self.base_url + (uri if uri[0] == '/' else '/' + uri)
        page = requests.get(url)
        return page.content
