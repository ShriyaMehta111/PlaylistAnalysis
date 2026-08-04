import streamlit as st
import pandas as pd
import plotly.express as px
from utils import footer
# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Advanced KPI Dashboard",
    page_icon="📈",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv("../data/france_top50_cleaned.csv")

# ==========================================================
# DATA PREPARATION
# ==========================================================

df["duration_minutes"] = df["duration_ms"] / 60000

df["duration_bucket"] = pd.cut(
    df["duration_minutes"],
    bins=[0,3,4,10],
    labels=["Short","Medium","Long"]
)

def rank_group(position):
    if position <= 10:
        return "Top 10"
    elif position <= 25:
        return "Top 25"
    else:
        return "Top 50"

df["rank_group"] = df["position"].apply(rank_group)

df["album_size"] = pd.cut(
    df["total_tracks"],
    bins=[0,5,15,1000],
    labels=["Small","Medium","Large"]
)

album_df = df[
    df["album_type"].str.lower().isin(["album","single"])
]

# ==========================================================
# PAGE TITLE
# ==========================================================

st.markdown("""
<div class="executive-card">

<h1>Advanced KPI Dashboard</h1>

<p>

Executive overview of France's Top 50 Playlist.

Monitor content performance, audience sensitivity,
release strategy and playlist quality using
business KPIs.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# KPI CALCULATIONS
# ==========================================================


explicit_share = df["is_explicit"].mean()*100

clean_share = 100-explicit_share

single_ratio = (
    album_df["album_type"]
    .str.lower()
    .eq("single")
    .mean()*100
)

avg_duration = df["duration_minutes"].mean()

album_size_popularity = (
    df.groupby("album_size", observed=True)["popularity"]
    .mean()
)

album_size_impact = (
    album_size_popularity.max()
    -
    album_size_popularity.min()
)

content_score = df["popularity"].mean()

st.markdown("""
<div class="kpi-title">
Executive KPIs
</div>
""", unsafe_allow_html=True)

# ==========================================================
# KPI ROW 1
# ==========================================================

kpi1,kpi2,kpi3 = st.columns(3)

with kpi1:

    st.metric(
        "Explicit Share",
        f"{explicit_share:.2f}%"
    )

with kpi2:

    st.metric(
        "Clean Ratio",
        f"{clean_share:.2f}%"
    )

with kpi3:

    st.metric(
        "Single Ratio",
        f"{single_ratio:.2f}%"
    )

# ==========================================================
# KPI ROW 2
# ==========================================================

kpi4,kpi5,kpi6 = st.columns(3)

with kpi4:

    st.metric(
        "Avg Duration",
        f"{avg_duration:.2f} min"
    )

with kpi5:

    st.metric(
        "Album Impact",
        f"{album_size_impact:.2f}"
    )

with kpi6:

    st.metric(
        "Content Score",
        f"{content_score:.2f}"
    )

st.divider()

# ==========================================================
# CHARTS
# ==========================================================

chart1, chart2 = st.columns(2)

# ----------------------------------------------------------
# CHART 1
# Explicit vs Clean Content Share
# ----------------------------------------------------------

with chart1:
    
    explicit_df = pd.DataFrame({
        "Content": ["Explicit", "Clean"],
        "Percentage": [explicit_share, clean_share]
    })

    fig = px.pie(
        explicit_df,
        names="Content",
        values="Percentage",
        hole=0.55,
        title="Explicit vs Clean Content Share",
        color="Content",
        color_discrete_map={
            "Explicit": "#EF4444",
            "Clean": "#10B981"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="white",

        paper_bgcolor="white",

        font=dict(size=15),
        height=420,
        legend_title="Content"
    )
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# CHART 2
# Album vs Single Share
# ----------------------------------------------------------

with chart2:

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
        hole=0.55,
        title="Album vs Single Distribution",
        color="Album Type",
        color_discrete_map={
            "Album": "#4F46E5",
            "Single": "#0EA5E9"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="white",

        paper_bgcolor="white",

        font=dict(size=15),
        height=420
    )
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ==========================================================
# CHART 3
# Duration Bucket Distribution
# ==========================================================

duration_count = (
    df.groupby("duration_bucket", observed=True)
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
        "#10B981"
    ]
)

fig.update_layout(
    template="plotly_white",
    plot_bgcolor="white",

    paper_bgcolor="white",

    font=dict(size=15),
    height=450,
    showlegend=False,
    xaxis_title="Duration Category",
    yaxis_title="Number of Songs"
)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

st.markdown('<div class="chart-card">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


st.divider()

# ==========================================================
# EXECUTIVE OBSERVATIONS
# ==========================================================

st.markdown("""
<div class="summary-card">

<h3>Executive Observations</h3>

</div>
""", unsafe_allow_html=True)

st.info(f"""
• **Explicit songs** account for **{explicit_share:.2f}%** of the playlist, indicating strong audience acceptance.

• **Clean songs** still represent **{clean_share:.2f}%**, reflecting a balanced approach toward content compliance.

• **Singles** represent **{single_ratio:.2f}%** of the filtered releases, showing healthy competition between singles and album tracks.

• The **average song duration** is **{avg_duration:.2f} minutes**, aligning with modern streaming preferences.

• The **average popularity score** of **{content_score:.2f}** suggests that the playlist primarily consists of highly successful tracks.

• The **Album Size Impact Index** of **{album_size_impact:.2f}** indicates measurable variation in popularity across different album sizes.
""")



footer()