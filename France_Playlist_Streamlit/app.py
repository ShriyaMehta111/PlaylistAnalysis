import streamlit as st
import pandas as pd
from utils import footer



# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="France Top 50 Playlist Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "france_top50_cleaned.csv"

df = pd.read_csv(DATA_PATH)
#df = pd.read_csv("../data/france_top50_cleaned.csv")
from pathlib import Path

css_path = Path(__file__).resolve().parent.parent / "assets" / "style.css"

with open(css_path, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("🎵 Navigation")

st.sidebar.success(
    """
    Welcome!

    Use the pages below to explore the dashboard.
    """
)

# -------------------------------------------------
# Dashboard Title
# -------------------------------------------------


st.markdown("""
<div class="hero-card">

<h1>🎵 France Top 50 Playlist Dashboard</h1>

<p>
Interactive Business Intelligence Dashboard for analyzing
France's Top 50 Spotify Playlist.
Explore audience sensitivity, explicit content,
album structure, release format preference,
popularity trends and business insights.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="description-card">

<h3>Dashboard Overview</h3>

<p>
This dashboard analyzes the France Top 50 Playlist dataset to identify
listener preferences, content characteristics and strategic insights.
</p>

<ul>

<li>Audience Sensitivity</li>

<li>Explicit Content Acceptance</li>

<li>Album vs Single Preference</li>

<li>Popularity Analysis</li>

<li>Song Duration Trends</li>

<li>Executive Business Insights</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<div class="section-title">
Key Performance Indicators
</div>
""", unsafe_allow_html=True)
# -------------------------------------------------
# KPIs
# -------------------------------------------------
total_songs = len(df)
total_artists = df["artist"].nunique()
avg_popularity = round(df["popularity"].mean(), 2)
avg_duration = round(df["duration_minutes"].mean(), 2)
explicit_percent = round(df["is_explicit"].mean() * 100, 2)
clean_ratio = round((~df["is_explicit"]).mean(), 2)

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Songs", total_songs)
col2.metric("Artists", total_artists)
col3.metric("Avg Popularity", avg_popularity)
col4.metric("Clean Ratio", clean_ratio)
col5.metric("Avg Duration", avg_duration)
col6.metric("Explicit %", explicit_percent)

st.divider()

st.markdown("""
<div class="footer-card">

### Navigate Through the Dashboard

Use the sidebar to explore:

- Advanced KPI Dashboard
- Detailed Analysis
- Business Insights

Each page focuses on a different aspect of the France Top 50 Playlist and provides interactive visualizations and business recommendations.

</div>
""", unsafe_allow_html=True)



footer()
