import streamlit as st
import pandas as pd
import plotly.express as px
from utils import footer
# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------
st.set_page_config(
    page_title="Detailed Analysis",
    page_icon="📊",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------------------------------
# LOAD DATA
# -------------------------------------------------------
df = pd.read_csv("../data/france_top50_cleaned.csv")

# -------------------------------------------------------
# DATA PREPARATION
# -------------------------------------------------------

# Duration in minutes
df["duration_minutes"] = df["duration_ms"] / 60000

# Duration Bucket
df["duration_bucket"] = pd.cut(
    df["duration_minutes"],
    bins=[0,3,4,10],
    labels=["Short","Medium","Long"]
)

# Rank Group
def rank_group(position):
    if position <= 10:
        return "Top 10"
    elif position <= 25:
        return "Top 25"
    else:
        return "Top 50"

df["rank_group"] = df["position"].apply(rank_group)

# Album Size
df["album_size"] = pd.cut(
    df["total_tracks"],
    bins=[0,5,15,1000],
    labels=["Small","Medium","Large"]
)

# Keep only Album & Single
album_df = df[
    df["album_type"].str.lower().isin(["album","single"])
]

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.markdown("""
<div class="overview-card">

<h3>Analysis Overview</h3>

<p>

This page provides detailed insights into how
content format, duration, explicit content and
album characteristics influence popularity
within France's Top 50 Playlist.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =======================================================
# ROW 1
# =======================================================

col1, col2 = st.columns(2)

# -------------------------------------------------------
# CHART 1
# -------------------------------------------------------

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    popularity_album = (
        album_df
        .groupby("album_type")["popularity"]
        .mean()
        .reset_index()
    )
    

    fig = px.bar(
        popularity_album,
        x="album_type",
        y="popularity",
        color="album_type",
        text_auto=".2f",
        title="Average Popularity by Album Type",
        color_discrete_sequence=["#4F46E5","#0EA5E9"]
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        xaxis_title="Album Type",
        yaxis_title="Average Popularity"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
# -------------------------------------------------------
# CHART 2
# -------------------------------------------------------

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    popularity_duration = (
        df
        .groupby("duration_bucket", observed=True)["popularity"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        popularity_duration,
        x="duration_bucket",
        y="popularity",
        color="duration_bucket",
        text_auto=".2f",
        title="Average Popularity by Duration Bucket",
        color_discrete_sequence=["#4F46E5","#0EA5E9","#9699C2"]
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        xaxis_title="Duration Bucket",
        yaxis_title="Average Popularity"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
st.divider()

# =======================================================
# ROW 2
# =======================================================

col3, col4 = st.columns(2)

# -------------------------------------------------------
# CHART 3
# Explicit Content Distribution Across Rank Groups
# -------------------------------------------------------

with col3:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    explicit_rank = (
        df.groupby(["rank_group", "is_explicit"])
        .size()
        .reset_index(name="count")
    )

    explicit_rank["Content"] = explicit_rank["is_explicit"].map({
        True: "Explicit",
        False: "Clean"
    })

    fig = px.bar(
        explicit_rank,
        x="rank_group",
        y="count",
        color="Content",
        barmode="stack",
        text_auto=True,
        title="Explicit Content Distribution Across Rank Groups",
        color_discrete_map={
            "Explicit": "#4F46E5",
            "Clean": "#9699C2"
        }
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Rank Group",
        yaxis_title="Number of Songs",
        legend_title="Content Type"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
# -------------------------------------------------------
# CHART 4
# Album vs Single Distribution Across Rank Groups
# -------------------------------------------------------

with col4:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    album_rank = (
        album_df.groupby(["rank_group", "album_type"])
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        album_rank,
        x="rank_group",
        y="count",
        color="album_type",
        barmode="stack",
        text_auto=True,
        title="Album vs Single Distribution Across Rank Groups",
        color_discrete_map={
            "album": "#636EFA",
            "single": "#9699C2",
            "Album": "#636EFA",
            "Single": "#9699C2"
        }
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Rank Group",
        yaxis_title="Number of Songs",
        legend_title="Album Type"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
st.divider()

# =======================================================
# ROW 3
# =======================================================

col5, col6 = st.columns(2)

# -------------------------------------------------------
# CHART 5
# Average Popularity by Album Size
# -------------------------------------------------------

with col5:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    album_size_popularity = (
        df.groupby("album_size", observed=True)["popularity"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        album_size_popularity,
        x="album_size",
        y="popularity",
        color="album_size",
        text_auto=".2f",
        title="Average Popularity by Album Size",
        color_discrete_sequence=["#4F46E5","#0EA5E9","#9699C2"]
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        xaxis_title="Album Size",
        yaxis_title="Average Popularity"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
# -------------------------------------------------------
# CHART 6
# Average Popularity by Explicit Content
# -------------------------------------------------------

with col6:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    explicit_popularity = (
        df.groupby("is_explicit")["popularity"]
        .mean()
        .reset_index()
    )

    explicit_popularity["Content"] = explicit_popularity["is_explicit"].map({
        True: "Explicit",
        False: "Clean"
    })

    fig = px.bar(
        explicit_popularity,
        x="Content",
        y="popularity",
        color="Content",
        text_auto=".2f",
        title="Average Popularity by Explicit Content",
        color_discrete_map={
            "Explicit": "#4F46E5",
            "Clean": "#0EA5E9"
        }
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        xaxis_title="Content Type",
        yaxis_title="Average Popularity"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
# =======================================================
# PAGE SUMMARY
# =======================================================

st.divider()

st.markdown("""
<div class="summary-card">

<h3>Key Findings</h3>

<ul>

<li>Album and Single releases both contribute significantly to playlist performance.</li>

<li>Popularity varies across duration categories.</li>

<li>Explicit content appears across all ranking groups.</li>

<li>Album size has measurable influence on popularity.</li>

<li>Top-ranked songs reflect diverse release strategies.</li>

</ul>

</div>
""", unsafe_allow_html=True)


footer()