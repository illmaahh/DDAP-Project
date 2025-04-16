# main_sentiment_pipeline.py

import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# -----------------------------------
# Step 1: Load and Clean the Tweets
# -----------------------------------

print("🔄 Loading tweets...")
df = pd.read_csv('tweets.csv')

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)     # Remove mentions
    text = re.sub(r"#", "", text)        # Remove hashtags symbol
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower().strip()
    return text

df['cleaned_tweet'] = df['Tweet'].astype(str).apply(clean_text)
df.to_csv('cleaned_tweets.csv', index=False)
print("✅ Tweets cleaned and saved to 'cleaned_tweets.csv'")

# -----------------------------------
# Step 2: Perform Sentiment Analysis
# -----------------------------------

print("🧠 Analyzing sentiment...")
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['cleaned_tweet'].apply(get_sentiment)
df.to_csv('tweets_with_sentiment.csv', index=False)
print("✅ Sentiment analysis complete. Saved to 'tweets_with_sentiment.csv'")

# -----------------------------------
# Step 3: Pie Chart of Sentiment Distribution
# -----------------------------------

print("📊 Creating pie chart...")
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightblue'])
plt.title('Sentiment Distribution')
plt.savefig('sentiment_pie_chart.png')
plt.close()
print("✅ Pie chart saved as 'sentiment_pie_chart.png'")

# -----------------------------------
# Step 4: Bar Chart of Word Frequency
# -----------------------------------

print("📊 Creating bar chart of word frequency...")
all_words = ' '.join(df['cleaned_tweet']).split()
word_counts = Counter(all_words)
common_words = word_counts.most_common(10)

words, counts = zip(*common_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='skyblue')
plt.title('Top 10 Most Frequent Words in Tweets')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.savefig('word_frequency_bar_chart.png')
plt.close()
print("✅ Bar chart saved as 'word_frequency_bar_chart.png'")

# -----------------------------------
# Step 5: WordCloud (Optional but beautiful)
# -----------------------------------

print("☁️ Creating word cloud...")
text = ' '.join(df['cleaned_tweet'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Tweets")
plt.savefig('wordcloud.png')
plt.close()
print("✅ Word cloud saved as 'wordcloud.png'")

# -----------------------------------
# Step 6: (Optional) Time Series Analysis (if you have a date column)
# -----------------------------------

if 'date' in df.columns:
    print("📅 Creating time series analysis...")
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # Sentiment trend over time (rolling average for smoothing)
    sentiment_trend = df['Sentiment'].apply(lambda x: 1 if x == 'Positive' else (-1 if x == 'Negative' else 0)).rolling(window=7).mean()
    
    plt.figure(figsize=(10, 6))
    sentiment_trend.plot(title='Sentiment Trend Over Time', xlabel='Date', ylabel='Sentiment (Smoothed)')
    plt.savefig('sentiment_time_series.png')
    plt.close()
    print("✅ Time series chart saved as 'sentiment_time_series.png'")

print("🎉 All steps complete!")
