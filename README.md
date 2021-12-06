# Shady Reviews Web Scraping
There are some potentially fake, overly positive reviews on a dealer's page. This script will scrape the first 5 pages of reviews, perform sentiment analysis on each review text, and display the 3 most likely problematic entries.

## How To Run
Prerequisites: Python 3.7, virtualenv

### Setup

```bash
$ git clone https://github.com/fentontaylor/shady_reviews_web_scraping.git
$ cd shady_reviews_web_scraping
$ virtualenv venv --python=python3.7
$ source venv/bin/activate
$ pip install -r requirements.txt
```

TODO: Add Watson setup instructions

### Run Main Script

```bash
$ python run.py
```

### Run Tests

#### Basic
Will run all tests and print coverage report in console.
```bash
$ nose2
```

#### HTML Coverage Report
Will run tests, generate html report, and open in browser.
```bash
$ nose2 && coverage html && open htmlcov/index.html
```

## Sample Watson Client Response
```py
{
  'usage': {
    'text_units': 1,
    'text_characters': 149,
    'features': 1
  },
  'sentiment': {
    'document': {
      'score': -0.344922,
      'label': 'negative'
    }
  },
  'language': 'en'
}
```
