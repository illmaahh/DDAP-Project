import pandas as pd
from textblob import TextBlob

# Load the cleaned tweets
df = pd.read_csv("cleaned_tweets.csv")

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Apply sentiment analysis
df["Sentiment"] = df["Tweet"].apply(get_sentiment)

# Save the result
df.to_csv("tweets_with_sentiment.csv", index=False)
print("✅ Sentiment analysis complete. Results saved to 'tweets_with_sentiment.csv'")
