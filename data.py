# Inside your streamlit_app.py or a separate data.py file
import pandas as pd

data = [
    {"Tweet": "This is a tweet", "cleaned_tweet": "this is a tweet", "Sentiment": "Neutral"},
    {"Tweet": "Another tweet here", "cleaned_tweet": "another tweet here", "Sentiment": "Neutral"},
    {"Tweet": "Digital addiction is real!", "cleaned_tweet": "digital addiction is real", "Sentiment": "Positive"},
    # Add all other rows like this
]

df = pd.DataFrame(data)
