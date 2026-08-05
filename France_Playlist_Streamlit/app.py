import streamlit as st

from utils import (
    load_css,
    load_data,
    sidebar_filters,
    footer
)

# ======================================================
# PAGE CONFIGURATION
# ======================================================

st.set_page_config(
    page_title="France Top 50 Playlist Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD CSS
# ======================================================

load_css()

# ======================================================
# LOAD DATA
# ======================================================

df = load_data()

# ======================================================
# APPLY GLOBAL FILTERS
# ======================================================

filtered_df = sidebar_filters(df)

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class="hero-card">

<h1>🎵 France Top 50 Playlist Dashboard</h1>

<p>

Interactive Business Intelligence Dashboard developed for
Atlantic Recording Corporation to analyze France's Top 50 Spotify Playlist.

This dashboard provides insights into:

• Audience Sensitivity

• Explicit Content Acceptance

• Album vs Single Preference

• Song Duration Trends

• Album Structure

• Executive Business Recommendations

</p>

</div>
""", unsafe_allow_html=True)

# ======================================================
# OVERVIEW
# ======================================================

st.markdown("""

<div class="description-card">

<h3>Dashboard Overview</h3>

<p>

Explore playlist trends through interactive filters.

The sidebar allows you to analyse different time periods,
rank tiers, release formats and content types.

All pages automatically respond to the selected filters.

</p>

</div>

""", unsafe_allow_html=True)

st.divider()

# ======================================================
# KPI SECTION
# ======================================================

st.markdown("""
<div class="section-title">
📊 Dashboard Overview
</div>
""", unsafe_allow_html=True)

# ======================================================
# KPIs
# ======================================================

total_songs = len(filtered_df)

total_artists = filtered_df["artist"].nunique()

avg_popularity = round(filtered_df["popularity"].mean(),2)

avg_duration = round(filtered_df["duration_minutes"].mean(),2)

explicit_percent = round(
    filtered_df["is_explicit"].mean()*100,
    2
)

clean_percent = round(
    100-explicit_percent,
    2
)

k1,k2,k3,k4,k5,k6 = st.columns(6)

k1.metric("Songs", total_songs)

k2.metric("Artists", total_artists)

k3.metric("Popularity", avg_popularity)

k4.metric("Duration", f"{avg_duration} min")

k5.metric("Explicit", f"{explicit_percent}%")

k6.metric("Clean", f"{clean_percent}%")

st.divider()

# ======================================================
# INFORMATION
# ======================================================

st.markdown("""

<div class="summary-card">

<h3>Dashboard Navigation</h3>

This project consists of four modules:

<ul>

<li><b>Home</b> – Executive Overview</li>

<li><b>Advanced KPI Dashboard</b> – Business KPIs</li>

<li><b>Detailed Analysis</b> – Deep Analytical Visualisations</li>

<li><b>Business Insights</b> – Strategic Recommendations</li>

</ul>

Use the filters in the sidebar to interactively explore
different sections of the France Top 50 Playlist.

</div>

""", unsafe_allow_html=True)

footer()