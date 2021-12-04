# Shady Reviews Web Scraping
There are some potentially fake, overly positive reviews on a dealer's page. This script will scrape the first 5 pages of reviews, perform sentiment analysis on each review text, and display the 3 most likely problematic entries.

## How To Run
Prereuqisites: Python 3.7, virtualenv

### Setup

```bash
$ git clone https://github.com/fentontaylor/shady_reviews_web_scraping.git
$ cd shady_reviews_web_scraping
$ virtualenv venv --python=python3.7
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Run Main Script

```bash
$ python run.py
```
