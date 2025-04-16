import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ✅ Load the CSV file first
df = pd.read_csv('tweets_with_sentiment.csv')

# ✅ Combine all cleaned tweets into one big string
text = ' '.join(df['cleaned_tweet'])

# ✅ Generate the Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# ✅ Display it
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Cleaned Tweets')
plt.tight_layout()
plt.show()
