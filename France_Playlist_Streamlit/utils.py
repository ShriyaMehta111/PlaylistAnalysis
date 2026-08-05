import streamlit as st
import pandas as pd
from pathlib import Path

# ======================================================
# BASE PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "france_top50_cleaned.csv"
CSS_PATH = BASE_DIR / "assets" / "style.css"

# ======================================================
# LOAD CSS
# ======================================================

def load_css():
    with open(CSS_PATH, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    # ------------------------
    # Date
    # ------------------------

    df["date"] = pd.to_datetime(df["date"])

    # ------------------------
    # Duration
    # ------------------------

    df["duration_minutes"] = df["duration_ms"] / 60000

    df["duration_bucket"] = pd.cut(
        df["duration_minutes"],
        bins=[0,3,4,10],
        labels=["Short","Medium","Long"]
    )

    # ------------------------
    # Rank Group
    # ------------------------

    def rank_group(position):

        if position <= 10:
            return "Top 10"

        elif position <= 25:
            return "Top 25"

        else:
            return "Top 50"

    df["rank_group"] = df["position"].apply(rank_group)

    # ------------------------
    # Album Size
    # ------------------------

    df["album_size"] = pd.cut(
        df["total_tracks"],
        bins=[0,5,15,1000],
        labels=["Small","Medium","Large"]
    )

    return df

# ======================================================
# GLOBAL FILTERS
# ======================================================

def sidebar_filters(df):

    st.sidebar.header("🎛 Dashboard Filters")

    # ==============================
    # DATE FILTER
    # ==============================

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    date_range = st.sidebar.date_input(
        "📅 Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(date_range) == 2:

        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[1])

        df = df[
            (df["date"] >= start_date)
            &
            (df["date"] <= end_date)
        ]

    # ==============================
    # RANK FILTER
    # ==============================

    rank_options = st.sidebar.multiselect(

        "🏆 Rank Tier",

        options=[
            "Top 10",
            "Top 25",
            "Top 50"
        ],

        default=[
            "Top 10",
            "Top 25",
            "Top 50"
        ]
    )

    df = df[df["rank_group"].isin(rank_options)]

    # ==============================
    # EXPLICIT FILTER
    # ==============================

    explicit = st.sidebar.selectbox(

        "🔞 Explicit Content",

        [
            "All",
            "Explicit Only",
            "Clean Only"
        ]
    )

    if explicit == "Explicit Only":
        df = df[df["is_explicit"]]

    elif explicit == "Clean Only":
        df = df[~df["is_explicit"]]

    # ==============================
    # ALBUM FILTER
    # ==============================

    album_options = st.sidebar.multiselect(

        "💿 Album Type",

        options=[
            "album",
            "single"
        ],

        default=[
            "album",
            "single"
        ]
    )

    df = df[
        df["album_type"]
        .str.lower()
        .isin(album_options)
    ]

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"Showing **{len(df)}** records"
    )

    return df

# ======================================================
# FOOTER
# ======================================================

def footer():

    st.divider()

    with st.container(border=True):

        st.markdown("## 🎵 France Top 50 Playlist Analysis Dashboard")

        st.write("**Developed by Shriya Mehta**")

        st.write("Python • Streamlit • Pandas • Plotly")

        st.caption("© 2026")