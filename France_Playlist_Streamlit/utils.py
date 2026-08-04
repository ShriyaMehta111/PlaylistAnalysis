import streamlit as st
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "france_top50_cleaned.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def footer():

    st.divider()

    with st.container(border=True):

        st.markdown("## 🎵 France Top 50 Playlist Analysis Dashboard")

        st.write("**Developed by Shriya Mehta**")

        st.write("Python • Streamlit • Pandas • Plotly")

        st.caption("© 2026")