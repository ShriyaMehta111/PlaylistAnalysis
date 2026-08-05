import streamlit as st
import plotly.express as px

from utils import (
    load_data,
    load_css,
    sidebar_filters,
    footer
)

# ======================================================
# PAGE CONFIGURATION
# ======================================================

st.set_page_config(
    page_title="Detailed Analysis",
    page_icon="📊",
    layout="wide"
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
# APPLY FILTERS
# ======================================================

filtered_df = sidebar_filters(df)

# ======================================================
# KEEP ONLY ALBUM + SINGLE
# ======================================================

album_df = filtered_df[
    filtered_df["album_type"]
    .str.lower()
    .isin(["album", "single"])
]

# ======================================================
# PAGE TITLE
# ======================================================

st.markdown("""
<div class="overview-card">

<h2>📊 Detailed Playlist Analysis</h2>

<p>

Explore how popularity, duration,
album structure,
explicit content,
and release formats influence
France's Top 50 Playlist.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)

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
        color_discrete_sequence=[
            "#4F46E5",
            "#0EA5E9"
        ]
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        xaxis_title="Album Type",
        yaxis_title="Popularity"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig = px.histogram(

        filtered_df,

        x="duration_minutes",

        nbins=25,

        color_discrete_sequence=["#4F46E5"],

        title="Song Duration Histogram"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Duration (Minutes)",

        yaxis_title="Number of Songs"

    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================================================
# ROW 2
# ======================================================

col3, col4 = st.columns(2)

# -----------------------------------------------------
# CHART 3
# Explicit vs Clean Across Rank Groups
# -----------------------------------------------------

with col3:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    explicit_rank = (
        filtered_df
        .groupby(["rank_group","is_explicit"])
        .size()
        .reset_index(name="Songs")
    )

    explicit_rank["Content"] = explicit_rank["is_explicit"].map({
        True:"Explicit",
        False:"Clean"
    })

    fig = px.bar(

        explicit_rank,

        x="rank_group",

        y="Songs",

        color="Content",

        barmode="stack",

        text_auto=True,

        title="Explicit Content Distribution Across Rank Groups",

        color_discrete_map={

            "Explicit":"#4F46E5",

            "Clean":"#0EA5E9"

        }

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Rank Group",

        yaxis_title="Number of Songs",

        legend_title="Content"

    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# CHART 4
# Album vs Single Across Rank Groups
# -----------------------------------------------------

with col4:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    album_rank = (

        album_df

        .groupby(["rank_group","album_type"])

        .size()

        .reset_index(name="Songs")

    )

    fig = px.bar(

        album_rank,

        x="rank_group",

        y="Songs",

        color="album_type",

        barmode="stack",

        text_auto=True,

        title="Album vs Single Distribution Across Rank Groups",

        color_discrete_map={

            "album":"#4F46E5",

            "single":"#9699C2",

            "Album":"#4F46E5",

            "Single":"#9699C2"

        }

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Rank Group",

        yaxis_title="Number of Songs",

        legend_title="Album Type"

    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================================================
# ROW 3
# ======================================================

col5, col6 = st.columns(2)

# -----------------------------------------------------
# CHART 5
# Album Size
# -----------------------------------------------------

with col5:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    album_size = (

        filtered_df

        .groupby("album_size", observed=True)["popularity"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        album_size,

        x="album_size",

        y="popularity",

        color="album_size",

        text_auto=".2f",

        title="Average Popularity by Album Size",

        color_discrete_sequence=[

            "#4F46E5",

            "#0EA5E9",

            "#9699C2"

        ]

    )

    fig.update_layout(

        template="plotly_white",

        showlegend=False,

        xaxis_title="Album Size",

        yaxis_title="Average Popularity"

    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# CHART 6
# Popularity by Explicit Content
# -----------------------------------------------------

with col6:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    popularity = (

        filtered_df

        .groupby("is_explicit")["popularity"]

        .mean()

        .reset_index()

    )

    popularity["Content"] = popularity["is_explicit"].map({

        True:"Explicit",

        False:"Clean"

    })

    fig = px.bar(

        popularity,

        x="Content",

        y="popularity",

        color="Content",

        text_auto=".2f",

        title="Average Popularity by Content Type",

        color_discrete_map={

            "Explicit":"#4F46E5",

            "Clean":"#0EA5E9"

        }

    )

    fig.update_layout(

        template="plotly_white",

        showlegend=False,

        xaxis_title="Content",

        yaxis_title="Popularity"

    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown("""

<div class="summary-card">

<h3>Analytical Summary</h3>

<ul>

<li>Explicit content is distributed across every ranking tier, showing broad audience acceptance.</li>

<li>Album and single releases compete closely throughout the playlist.</li>

<li>Most songs fall between approximately 2.5 and 4 minutes, confirming modern streaming preferences.</li>

<li>Smaller albums generally achieve higher average popularity.</li>

<li>Popularity differences between explicit and clean songs remain relatively balanced.</li>

</ul>

</div>

""", unsafe_allow_html=True)

footer()

