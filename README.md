# Shady Reviews Web Scraping
There are some potentially fake, overly positive reviews on a dealer's page on dealerrater.com. This script will scrape the first 5 pages of reviews for that dealer, perform sentiment analysis on each review text, and display the 3 most "overly positive" entries.

The criteria for sorting the reviews is the results from IBM Watson's Natural Language Understanding API. Watson analyzed the text, performing what's known as "sentiment analysis" to determine if the given text is "postive" or "negative", and assigns a score to represent the magnitude of such a label. Sample analyses can be seen below.

The script in this repo uses the results of these analyses to filter only "positive" reviews and sort them according to the sentiment score. This way, we can determine the review entries that are most likely to be "overly positive" and therefore potentially fake.

#### Note:
- I chose to do this challenge with Python because it is a language that I have very limited experience with. I wanted to showcase my ability to apply my knowledge  of programming principles and test-driven development in a different paradigm, but still complete the task at a high level of competency.
- Between 12/5/2021 evening and 12/6/2021 morning, the HTML structure of the reviews pages on dealerrater.com changed. You can see evidence of that change in commit history. The first 5 pages of HTML can be found in `tests/fixtures` directory to show what the HTML was on morning of 12/6. If you get an error running the script, please refer to the tests as proof of working code as of that time. 

### Sample Watson Client Responses

#### Negative Sentiment
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

#### Positive Sentiment
```py
{
  'usage': {
    'text_units': 1,
    'text_characters': 112,
    'features': 1
  },
  'sentiment': {
    'document': {
      'score': 0.974371,
      'label': 'positive'
    }
  },
  'language': 'en'
}
```

## Setup
Prerequisites: Python 3.7, virtualenv

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
<img width="300" alt="Screen Shot 2021-12-06 at 11 17 30 AM" src="https://user-images.githubusercontent.com/18686466/144902073-9d0e8ae7-ebed-4d42-b29e-a83498fe5498.png">

4. You should now be on your instance dashboard. Click "Manage" to view/copy your credentials.
<img width="600" alt="Screen Shot 2021-12-06 at 11 16 59 AM" src="https://user-images.githubusercontent.com/18686466/144902237-858d998f-1039-4ec4-862d-32518daf7de6.png">

5. In the shady_reviews_web_scraping repo, create a `.env` file with 2 key/value pairs:

```
WATSON_API_KEY={your Watson API key}
WATSON_URL={your unique Watson url}
```

## How To Run
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

