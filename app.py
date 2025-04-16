import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.set_page_config(page_title="Digital Addiction Detector", layout="wide")
st.title("📱 Detecting Digital Addiction Patterns Using Social Media Data")

# Upload CSV
uploaded_file = st.file_uploader("Upload your social media data CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df.head())

    # Try to auto-detect datetime columns
    datetime_columns = [col for col in df.columns if 'time' in col.lower() or 'date' in col.lower()]
    if datetime_columns:
        for col in datetime_columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass  # Keep as-is if conversion fails

    # Basic summary
    st.subheader("📊 Data Summary")
    st.write(df.describe(include='all'))

    # Optional: Select numeric column to visualize usage
    st.subheader("📈 Visualize Screen Time or Usage Frequency")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Choose a numeric column", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        ax.set_title(f'Distribution of {selected_col}')
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found to visualize.")

    # Optional: Detect signs of addiction based on thresholds
    st.subheader("🧠 Addiction Pattern Detection (Basic)")
    threshold_col = st.selectbox("Choose a column to check for high usage", numeric_cols)
    threshold_val = st.slider("Set a threshold value", float(df[threshold_col].min()), float(df[threshold_col].max()), float(df[threshold_col].mean()))

    high_usage = df[df[threshold_col] > threshold_val]
    st.write(f"🔴 Entries above threshold ({threshold_val}): {len(high_usage)}")
    st.dataframe(high_usage)
else:
    st.info("Please upload a CSV file to get started.")
