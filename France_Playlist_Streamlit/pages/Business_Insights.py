import streamlit as st
from utils import footer

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = BASE_DIR / "assets" / "style.css"

with open(CSS_PATH, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================================================
# PAGE TITLE
# ==========================================================

st.markdown("""
<div class="business-header">

<h1>Business Insights & Recommendations</h1>

<p>

Executive summary of the France Top 50 Playlist analysis,
highlighting strategic findings and actionable recommendations
for Atlantic Recording Corporation.

</p>

</div>
""", unsafe_allow_html=True)
st.divider()

# ==========================================================
# KEY INSIGHTS
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.success("""
### Release Format Preference

Album tracks represent **52.88%** of playlist entries,
indicating a balanced preference for album releases alongside singles.
""")

    st.info("""
### Audience Sensitivity

Explicit songs account for **56.26%** of the playlist,
showing strong audience acceptance of explicit content.
""")

    st.warning("""
### Artist Retention

**Werenoi** appears most frequently in the playlist,
highlighting strong artist retention and sustained popularity.
""")

    st.success("""
### Popularity

The average popularity score (**76.65**) indicates that
the playlist primarily consists of highly successful tracks.
""")

with col2:

    st.info("""
### Duration Preference

Songs around **3 minutes** dominate the playlist,
matching modern streaming behaviour and listener preferences.
""")

    st.warning("""
### Content Compliance

Although explicit songs dominate the playlist,
clean songs still represent **43.74%**,
indicating a balanced approach toward content compliance.
""")

    st.success("""
### Album Size Impact

Large albums generally have lower average popularity than
small albums, suggesting compact releases concentrate
higher-performing tracks.
""")

    st.info("""
### 🇫🇷 France's Preferred Content Profile

France's preferred content profile consists of:

• Moderately short songs

• Balanced album and single releases

• Higher proportion of explicit content

reflecting current streaming trends.
""")

st.divider()

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

st.markdown("""
<div class="recommendation-card">

<h2>Strategic Recommendations</h2>

<ol>

<li><b>Maintain a balanced release strategy</b> by continuing to support both album and single releases.</li>

<li><b>Prioritize streaming-friendly song durations</b> around three minutes to align with listener preferences.</li>

<li><b>Optimize album size</b> by focusing on compact releases that concentrate high-performing tracks.</li>

<li><b>Balance explicit and clean content</b> to appeal to a wider audience while maintaining strong engagement.</li>

<li><b>Strengthen artist continuity</b> by investing in artists with repeated playlist success, such as Werenoi.</li>

</ol>

</div>
""", unsafe_allow_html=True)

footer()