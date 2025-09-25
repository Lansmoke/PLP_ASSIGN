import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# Load dataset
df = pd.read_csv("metadata.csv", low_memory=False)
df_clean = df.dropna(subset=["title", "abstract", "publish_time"]).copy()
df_clean["publish_time"] = pd.to_datetime(df_clean["publish_time"], errors="coerce")
df_clean["year"] = df_clean["publish_time"].dt.year

# Data for charts
papers_per_year = df_clean["year"].value_counts().sort_index()
top_journals = df_clean["journal"].value_counts().head(10)
titles_text = " ".join(df_clean["title"].dropna()).lower()
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)

# Streamlit App
st.title("CORD-19 Metadata Explorer")
st.write("An interactive app to explore COVID-19 research papers")

# Year filter
year_filter = st.slider("Select Year", int(df_clean["year"].min()), int(df_clean["year"].max()))
df_filtered = df_clean[df_clean["year"] == year_filter]

st.subheader("Publications Over Time")
st.line_chart(papers_per_year)

st.subheader("Top Journals")
st.bar_chart(top_journals)

st.subheader("Word Cloud of Titles")
st.image(wordcloud.to_array())

st.subheader(f"Sample Papers from {year_filter}")
st.dataframe(df_filtered.sample(10))
