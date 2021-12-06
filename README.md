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

### IBM Watson NLP credentials
1. Go to [IBM Watson NLP](https://www.ibm.com/cloud/watson-natural-language-understanding) page, and follow the steps to create a free account.
2. Once you are on your main dashboard page, click the "Create" button in the right sidebar to create your instance.
3. You should now be on your instance dashboard. Click "Manage" to view your credentials.
4. In the shady_reviews_web_scraping repo, create a .env file with 2 key/value pairs:
```
WATSON_API_KEY={your API key}
WATSON_URL={your unique url}
```

### Run Main Script
Execute the following command to run the script. You should see progress printed to the console, and finally results similar to below:

```bash
$ python run.py
```

```
************************ RESULTS ************************
1.
TEXT: Love dealing at this dealership. Dennis was most helpful and efficient. Answered all our questions and knew every detail about the car. Am super pleased and will visit again.
SENTIMENT: positive
SCORE: 0.999427

2.
TEXT: We had a great experience with Tito! He was helpful and friendly! Glad we got to work with him. Loving our new car!!
SENTIMENT: positive
SCORE: 0.999159

3.
TEXT: No pressure sales. Fantastic experience. Tito went above and beyond in taking care of me and my family. Thanks to Tito I have my first sports car!!!
SENTIMENT: positive
SCORE: 0.998587
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
