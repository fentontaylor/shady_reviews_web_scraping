import re
from typing import List, Union

from bs4 import BeautifulSoup
import requests

class ReviewScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url[0:-1] if base_url[-1] == '/' else base_url
        self.page_content: Union[str, None] = None

    def fetch_page_content(self, uri: str) -> None:
        url = self.base_url + (uri if uri[0] == '/' else '/' + uri)
        page = requests.get(url)
        self.page_content = page.content

    def review_contents(self) -> List[str]:
        review_contents: List[str] = []
        if self.page_content:
            review_entries = BeautifulSoup(self.page_content, 'html.parser').find(
                'div', id='reviews').find_all('div', class_='review-entry')
            for review_entry in review_entries:
                review: str = review_entry.find(
                    'p', class_='review-content').text
                cleaned_text = re.sub("\s+", ' ', review.replace('\n', ' ')).strip()
                if review: review_contents.append(cleaned_text)
        return review_contents
