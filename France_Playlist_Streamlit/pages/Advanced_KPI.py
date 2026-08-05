import streamlit as st
import plotly.express as px

from utils import (
    load_data,
    load_css,
    sidebar_filters,
    footer
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Advanced KPI Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

load_css()

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data()

# ==========================================================
# APPLY GLOBAL FILTERS
# ==========================================================

filtered_df = sidebar_filters(df)

# ==========================================================
# PAGE TITLE
# ==========================================================

st.markdown("""
<div class="executive-card">

<h1>📈 Advanced KPI Dashboard</h1>

<p>

Executive overview of France's Top 50 Playlist.

Monitor content performance,
audience sensitivity,
release strategy,
and playlist quality
using business KPIs.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

album_df = filtered_df[
    filtered_df["album_type"].str.lower().isin(["album", "single"])
]

explicit_share = filtered_df["is_explicit"].mean() * 100

clean_share = 100 - explicit_share

single_ratio = (
    album_df["album_type"]
    .str.lower()
    .eq("single")
    .mean() * 100
)

avg_duration = filtered_df["duration_minutes"].mean()

album_size_popularity = (
    filtered_df
    .groupby("album_size", observed=True)["popularity"]
    .mean()
)

album_size_impact = (
    album_size_popularity.max()
    -
    album_size_popularity.min()
)

content_score = filtered_df["popularity"].mean()

# ==========================================================
# KPI TITLE
# ==========================================================

st.markdown("""
<div class="kpi-title">
📊 Executive KPIs
</div>
""", unsafe_allow_html=True)

# ==========================================================
# KPI ROW 1
# ==========================================================

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:

    st.metric(
        label="🔞 Explicit Share",
        value=f"{explicit_share:.2f}%"
    )

with kpi2:

    st.metric(
        label="🟢 Clean Share",
        value=f"{clean_share:.2f}%"
    )

with kpi3:

    st.metric(
        label="💿 Single Ratio",
        value=f"{single_ratio:.2f}%"
    )

# ==========================================================
# KPI ROW 2
# ==========================================================

kpi4, kpi5, kpi6 = st.columns(3)

with kpi4:

    st.metric(
        label="⏱ Average Duration",
        value=f"{avg_duration:.2f} min"
    )

with kpi5:

    st.metric(
        label="📦 Album Impact",
        value=f"{album_size_impact:.2f}"
    )

with kpi6:

    st.metric(
        label="⭐ Content Score",
        value=f"{content_score:.2f}"
    )

st.divider()

# ==========================================================
# CHART ROW 1
# ==========================================================

col1, col2 = st.columns(2)

# ----------------------------------------------------------
# CHART 1
# Explicit vs Clean
# ----------------------------------------------------------

with col1:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    explicit_df = filtered_df["is_explicit"].value_counts().reset_index()
    explicit_df.columns = ["Content", "Count"]

    explicit_df["Content"] = explicit_df["Content"].map({
        True: "Explicit",
        False: "Clean"
    })

    fig = px.pie(
        explicit_df,
        names="Content",
        values="Count",
        hole=0.60,
        title="Explicit vs Clean Content",
        color="Content",
        color_discrete_map={
            "Explicit": "#4F46E5",
            "Clean": "#0EA5E9"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=430,
        legend_title=""
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# CHART 2
# Album vs Single
# ----------------------------------------------------------

with col2:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    album_share = (
        album_df["album_type"]
        .str.title()
        .value_counts()
        .reset_index()
    )

    album_share.columns = ["Album Type", "Count"]

    fig = px.pie(
        album_share,
        names="Album Type",
        values="Count",
        hole=0.60,
        title="Album vs Single Distribution",
        color="Album Type",
        color_discrete_map={
            "Album": "#4F46E5",
            "Single": "#9699C2"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=430,
        legend_title=""
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ==========================================================
# CHART 3
# Duration Distribution
# ==========================================================

st.markdown('<div class="chart-card">', unsafe_allow_html=True)

duration_count = (
    filtered_df
    .groupby("duration_bucket", observed=True)
    .size()
    .reset_index(name="Songs")
)

fig = px.bar(
    duration_count,
    x="duration_bucket",
    y="Songs",
    color="duration_bucket",
    text_auto=True,
    title="Song Distribution by Duration Category",
    color_discrete_sequence=[
        "#4F46E5",
        "#0EA5E9",
        "#9699C2"
    ]
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=470,
    showlegend=False,
    xaxis_title="Duration Category",
    yaxis_title="Number of Songs"
)

fig.update_xaxes(showgrid=False)

fig.update_yaxes(showgrid=False)

st.plotly_chart(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="summary-card">

<h3>Executive Observations</h3>

</div>
""", unsafe_allow_html=True)

st.info(f"""
**Key Insights**

• Explicit songs account for **{explicit_share:.2f}%** of the filtered playlist.

• Clean songs represent **{clean_share:.2f}%**.

• Singles contribute **{single_ratio:.2f}%** of all filtered releases.

• Average song duration is **{avg_duration:.2f} minutes**.

• Content quality score is **{content_score:.2f}**, indicating consistently popular tracks.

• Album popularity varies by **{album_size_impact:.2f}** points across album sizes.
""")

footer()