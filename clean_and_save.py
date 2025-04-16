import pandas as pd
import re

# Read tweets from CSV
df = pd.read_csv("tweets.csv")

# Clean function
def clean_tweet(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove links
    text = re.sub(r'\@\w+|\#', '', text)  # Remove mentions and hashtags
    text = re.sub(r'RT[\s]+', '', text)  # Remove RT
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower()  # Lowercase all text

# Apply cleaning
df['cleaned_tweet'] = df['Tweet'].apply(clean_tweet)

# Save to new file
df.to_csv("cleaned_tweets.csv", index=False)

print("✅ Tweets cleaned and saved to 'cleaned_tweets.csv'")
