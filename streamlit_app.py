import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App title with animation using markdown
st.markdown(
    """
    <h1 style='text-align: center; font-size: 42px; color: #00c0ff; animation: glow 2s infinite;'>💡 Detecting Digital Addiction Patterns (DDAP)</h1>
    <style>
    @keyframes glow {
        0% { text-shadow: 0 0 5px #00f2ff, 0 0 10px #00f2ff, 0 0 20px #00f2ff; }
        50% { text-shadow: 0 0 20px #00ffcc, 0 0 30px #00ffcc, 0 0 40px #00ffcc; }
        100% { text-shadow: 0 0 5px #00f2ff, 0 0 10px #00f2ff, 0 0 20px #00f2ff; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("### 🤖 Welcome to the Digital Addiction Analysis Web App by **Ilma Rasheed**")

# Load embedded data
data = pd.DataFrame({
    "Tweet": [
        "This is a tweet", "Another tweet here", "Digital addiction is real!",
        "Can't stop scrolling reels", "Been on phone 10 hours today!", "Taking a digital detox 🌿",
        "Feeling anxious without Wi-Fi", "Scrolling endlessly on Instagram", "This app is so addictive!", "Happy to stay offline"
    ],
    "Platform": [
        "Twitter", "Twitter", "Twitter", "Instagram", "Instagram", "Facebook",
        "Wi-Fi", "Instagram", "Snapchat", "Offline"
    ],
    "Sentiment": [
        "Neutral", "Neutral", "Positive", "Negative", "Negative", "Positive",
        "Negative", "Negative", "Negative", "Positive"
    ]
})

st.success("✅ Data Loaded Successfully!")

# Show data preview
with st.expander("📄 Click to View Data"):
    st.dataframe(data, use_container_width=True)

# Show sentiment distribution
st.markdown("### 📊 Sentiment Distribution")
sentiment_counts = data['Sentiment'].value_counts()
fig1, ax1 = plt.subplots()
colors = ['#ffb3ba', '#baffc9', '#bae1ff']
ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
st.pyplot(fig1)

# Show platform usage
st.markdown("### 🌐 Platform Usage")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.countplot(data=data, x='Platform', palette='cool', ax=ax2)
plt.xticks(rotation=30)
st.pyplot(fig2)

# Display analytics summary
st.markdown("### 📌 Summary")
st.info(f"""
- Total Tweets Analyzed: {len(data)}
- Positive Tweets: {sum(data['Sentiment'] == 'Positive')}
- Negative Tweets: {sum(data['Sentiment'] == 'Negative')}
- Neutral Tweets: {sum(data['Sentiment'] == 'Neutral')}
""")

st.markdown("---")
st.markdown("👩‍💻 **Developed by Ilma Rasheed** | 🔍 A Project on Digital Wellbeing")


