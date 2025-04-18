import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import altair as alt

# ------------------- PAGE CONFIG ---------------------
st.set_page_config(page_title="Digital Addiction Insights", layout="wide")

# ------------------- HEADER ---------------------
st.title("📱 Detecting Digital Addiction Patterns")
st.subheader("🔍 A Research Project on Social Media Behavior Analysis")

st.markdown("""
Welcome to the Digital Addiction Analyzer App!  
Upload your dataset, analyze patterns, visualize usage, and extract insights for research.

---
""")

# ------------------- SIDEBAR ---------------------
st.sidebar.title("🔧 Settings")
st.sidebar.markdown("Adjust filters, upload files, and explore visualizations.")

uploaded_file = st.sidebar.file_uploader("📂 Upload CSV File", type=["csv"])

# ------------------- MAIN FUNCTION ---------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Your file has these columns:", df.columns.tolist())

    st.success("✅ Data uploaded successfully!")
    
    st.markdown("### 👁️ Data Preview")
    st.dataframe(df.head())

    # ------------------- FILTERS ---------------------
    st.markdown("### 🔍 Filter Data")
    col1, col2 = st.columns(2)
    with col1:
        selected_platform = st.selectbox("Select Platform", options=["All"] + df['platform'].unique().tolist())
    with col2:
        selected_age = st.slider("Select Age Range", int(df["age"].min()), int(df["age"].max()), (18, 30))

    filtered_df = df.copy()
    if selected_platform != "All":
        filtered_df = filtered_df[filtered_df["platform"] == selected_platform]
    filtered_df = filtered_df[(filtered_df["age"] >= selected_age[0]) & (filtered_df["age"] <= selected_age[1])]

    # ------------------- VISUALIZATIONS ---------------------
    st.markdown("### 📊 Visualizations")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("#### 🕒 Avg Daily Usage by Platform")
        usage_chart = filtered_df.groupby('platform')['daily_usage_hours'].mean().reset_index()
        st.altair_chart(
            alt.Chart(usage_chart).mark_bar(color='#3182CE').encode(
                x='platform', y='daily_usage_hours'
            ).properties(width=350, height=300), use_container_width=True
        )

    with col4:
        st.markdown("#### 📈 Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(filtered_df['age'], kde=True, ax=ax, color='skyblue')
        st.pyplot(fig)

    st.markdown("#### ☁️ Common Words in Comments")
    if "comments" in df.columns:
        text = " ".join(filtered_df["comments"].astype(str))
        wordcloud = WordCloud(width=800, height=300, background_color='white').generate(text)
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.info("No 'comments' column found in the dataset.")

    # ------------------- INSIGHTS ---------------------
    st.markdown("### 📌 Summary Insights")
    st.markdown(f"""
    - Total Records Analyzed: **{len(filtered_df)}**
    - Age Range: **{selected_age[0]} - {selected_age[1]}**
    - Most Used Platform: **{filtered_df['platform'].mode()[0]}**
    - Avg Daily Usage: **{filtered_df['daily_usage_hours'].mean():.2f} hrs**
    """)

else:
    st.info("👆 Please upload a CSV file from the sidebar to get started.")

# ------------------- FOOTER ---------------------
st.markdown("---")
st.markdown("""
👩‍💻 Built by **Ilma Rasheed** | 🧪 Part of Digital Addiction Detection Research  
💬 For queries, contact: *ilmaaa.rashid@gmail.com*
📚 References: WHO, APA Digital Use Guidelines, TechWellness  
""")
