import streamlit as st
import plotly.express as px

from utils import (
    load_css,
    load_data,
    sidebar_filters,
    footer
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

load_css()

df = load_data()
filtered_df = sidebar_filters(df)

# ==========================================================
# CALCULATIONS
# ==========================================================

explicit_share = round(filtered_df["is_explicit"].mean()*100,2)
clean_share = round(100-explicit_share,2)

album_share = (
    filtered_df["album_type"]
    .str.lower()
    .eq("album")
    .mean()*100
)

single_share = 100-album_share

avg_popularity = round(filtered_df["popularity"].mean(),2)

avg_duration = round(filtered_df["duration_minutes"].mean(),2)

# ==========================================================
# TITLE
# ==========================================================

st.markdown("""
<div class="business-header">

<h1>💡 Business Insights & Recommendations</h1>

<p>

Executive recommendations generated from the France Top 50 Playlist analysis.

These insights can support release planning,
content strategy,
playlist optimization,
and audience engagement.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# KPI CARDS
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

k1.metric("Explicit Content",f"{explicit_share}%")

k2.metric("Album Releases",f"{album_share:.2f}%")

k3.metric("Popularity",avg_popularity)

k4.metric("Avg Duration",f"{avg_duration} min")

st.divider()

# ==========================================================
# CONTENT COMPLIANCE SUMMARY PANEL
# ==========================================================

st.divider()

st.markdown("""
<div class="summary-card">

<h2>🛡 Content Compliance Summary</h2>

<p>
Quick assessment of the playlist's content profile based on
the selected filters.
</p>

</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

# ------------------------------
# Explicit Content
# ------------------------------

with c1:

    if explicit_share >= 60:

        st.error("""
### 🔴 Explicit Content

High explicit content dominance.

May reduce suitability for
family-friendly playlists.
""")

    elif explicit_share >= 40:

        st.warning("""
### 🟡 Explicit Content

Balanced mix of explicit and clean songs.

Suitable for mainstream audiences.
""")

    else:

        st.success("""
### 🟢 Explicit Content

Clean-content dominant playlist.

Highly suitable for broad audience reach.
""")

# ------------------------------
# Song Duration
# ------------------------------

with c2:

    if avg_duration <= 3.5:

        st.success("""
### 🟢 Song Duration

Streaming-friendly duration.

Matches current listener preferences.
""")

    else:

        st.warning("""
### 🟡 Song Duration

Average duration is slightly higher.

Longer songs may reduce completion rate.
""")

# ------------------------------
# Release Strategy
# ------------------------------

with c3:

    if 45 <= album_share <= 55:

        st.success("""
### 🟢 Release Strategy

Balanced Album & Single representation.

Healthy release diversity.
""")

    elif album_share > 55:

        st.warning("""
### 🟡 Release Strategy

Album releases dominate.

Consider increasing single releases.
""")

    else:

        st.warning("""
### 🟡 Release Strategy

Singles dominate.

Consider balanced album releases.
""")

# ==========================================================
# BUSINESS CHART
# ==========================================================

summary = {
    "Metric":[
        "Explicit",
        "Clean",
        "Album",
        "Single"
    ],
    "Percentage":[
        explicit_share,
        clean_share,
        album_share,
        single_share
    ]
}

fig = px.bar(

    summary,

    x="Metric",

    y="Percentage",

    color="Metric",

    text_auto=".2f",

    title="Overall Content Profile",

    color_discrete_sequence=[
        "#4F46E5",
        "#0EA5E9",
        "#10B981",
        "#9699C2"
    ]

)

fig.update_layout(

    template="plotly_white",

    showlegend=False,

    xaxis_title="Content Metric",

    yaxis_title="Percentage"

)

st.markdown('<div class="chart-card">', unsafe_allow_html=True)

st.plotly_chart(fig,use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ==========================================================
# INSIGHTS
# ==========================================================

st.markdown("""

<div class="summary-card">

<h3>Key Business Findings</h3>

<ul>

<li>France listeners show strong acceptance of explicit music while maintaining demand for clean content.</li>

<li>Album and single releases receive comparable audience attention, indicating that both release strategies remain effective.</li>

<li>Songs around three minutes dominate the playlist, matching modern streaming behaviour.</li>

<li>Highly popular tracks consistently appear throughout the ranking tiers, reflecting stable audience engagement.</li>

<li>Smaller albums tend to achieve higher average popularity, suggesting focused releases perform better.</li>

</ul>

</div>

""",unsafe_allow_html=True)

st.divider()

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

st.markdown("""

<div class="recommendation-card">

<h2>Strategic Recommendations</h2>

<ol>

<li>Continue investing in both album and single releases to maximize audience reach.</li>

<li>Prioritize tracks between 2.5 and 4 minutes for improved streaming performance.</li>

<li>Maintain a balanced catalogue of explicit and clean content to satisfy diverse listener preferences.</li>

<li>Focus on compact albums with stronger individual tracks rather than very large albums.</li>

<li>Strengthen long-term partnerships with consistently successful artists appearing frequently in the Top 50.</li>

</ol>

</div>

""",unsafe_allow_html=True)

st.divider()

st.success("""

### Executive Conclusion

The France Top 50 Playlist demonstrates a balanced preference for album and single releases,
strong acceptance of explicit content,
and clear preference for streaming-friendly song durations.

These findings can help Atlantic Recording Corporation optimize future release strategies,
playlist placement,
and audience engagement.

""")

footer()