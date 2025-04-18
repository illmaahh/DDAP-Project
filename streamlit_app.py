import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud

# Set up the app
st.set_page_config(page_title="Digital Addiction Pattern Detection", layout="wide")
st.title("📱 Detecting Digital Addiction Patterns Using Social Media Data")

# Step 1: Upload CSV file
uploaded_file = st.file_uploader("Upload your social media data CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Raw Data Preview")
    st.write(df.head())  # Show the first few rows of the data

    # Step 2: Clean the data
    def clean_text(text):
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"@\w+", "", text)     # Remove mentions
        text = re.sub(r"#", "", text)        # Remove hashtags symbol
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
        return text.lower().strip()

    df['cleaned_tweet'] = df['Tweet'].astype(str).apply(clean_text)
    st.subheader("🧹 Cleaned Data Preview")
    st.write(df.head())  # Show cleaned data

    # Step 3: Perform sentiment analysis
    def get_sentiment(text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity == 0:
            return "Neutral"
        else:
            return "Negative"

    df["Sentiment"] = df["cleaned_tweet"].apply(get_sentiment)
    st.subheader("📊 Sentiment Analysis Results")
    st.write(df[['Tweet', 'Sentiment']])

    # Step 4: Visualize results

    # Sentiment Distribution (Pie Chart)
    sentiment_counts = df['Sentiment'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightblue'])
    ax.set_title('Sentiment Distribution')
    st.pyplot(fig)

    # Word Cloud (for visualizing the most frequent words)
    text = ' '.join(df['cleaned_tweet'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.subheader("☁️ Word Cloud")
    st.image(wordcloud, use_column_width=True)

    # Top 10 Most Frequent Words (Bar Chart)
    all_words = ' '.join(df['cleaned_tweet']).split()
    word_freq = pd.Series(all_words).value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=word_freq.index, y=word_freq.values, ax=ax, palette='viridis')
    ax.set_title('Top 10 Most Frequent Words in Tweets')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to get started.")
