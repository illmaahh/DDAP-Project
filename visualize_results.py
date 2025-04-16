import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

# Load your data
df = pd.read_csv("tweets_with_sentiment.csv")

# ----- PIE CHART: Sentiment Distribution -----
sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'yellowgreen'])
plt.title('Sentiment Distribution')
plt.savefig('sentiment_pie_chart.png')  # Saves the pie chart
plt.show()

# ----- BAR CHART: Word Frequency -----
all_words = ' '.join(df['cleaned_tweet']).split()
word_freq = Counter(all_words)

# Top 10 common words
most_common_words = word_freq.most_common(10)
words, counts = zip(*most_common_words)

plt.figure(figsize=(8, 5))
sns.barplot(x=list(words), y=list(counts), palette='viridis')
plt.title('Top 10 Most Frequent Words in Tweets')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('word_frequency_bar_chart.png')  # Saves the bar chart
plt.show()
