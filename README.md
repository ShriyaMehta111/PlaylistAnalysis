# PlaylistAnalysis
This is my first git repository.
Author - Shriya Mehta

# 🎵 Audience Sensitivity, Content Compliance & Format Preference Analysis of France Top 50 Playlist

A comprehensive data analytics project developed as part of the **Unified Mentor Internship Program** for **Atlantic Recording Corporation**. This project analyzes the France Top 50 Spotify playlist to understand audience sensitivity, explicit content acceptance, release format preferences, song duration trends, and album structure impact using **Python, Streamlit, and Power BI**.

---

# 📌 Project Objective

The primary objective of this project is to help Atlantic Recording Corporation understand the listening behavior of the French audience by analyzing:

- Explicit vs Clean content acceptance
- Album vs Single release preference
- Song duration trends
- Album size impact on popularity
- Overall content profile preferred in France

These insights help support data-driven decisions for music release strategies, playlist pitching, and audience engagement.

---

# 📂 Dataset Information

The dataset contains daily snapshots of the **France Top 50 Playlist**.

### Dataset Fields

| Column | Description |
|---------|-------------|
| date | Playlist snapshot date |
| position | Playlist rank (1–50) |
| song | Song title |
| artist | Artist name |
| popularity | Spotify popularity score |
| duration_ms | Song duration (milliseconds) |
| album_type | Album or Single |
| total_tracks | Number of tracks in album |
| is_explicit | Explicit content flag |
| album_cover_url | Album artwork URL |

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Git
- GitHub

---

# 📊 Project Workflow

## 1. Data Preparation

- Removed duplicate records
- Converted duration from milliseconds to minutes
- Standardized album type labels
- Created duration buckets
- Created rank groups (Top 10, Top 25, Top 50)
- Created album size categories

---

## 2. Exploratory Data Analysis

Performed detailed analysis on:

- Explicit vs Clean content
- Album vs Single distribution
- Song duration trends
- Album size analysis
- Popularity analysis
- Rank-based content analysis

---

## 3. KPI Analysis

Developed business KPIs including:

- Explicit Content Share
- Clean Content Ratio
- Single vs Album Ratio
- Average Song Duration
- Album Size Impact Index
- Content Acceptance Score

---

## 4. Business Insights

Generated business recommendations based on the analytical findings.

---


---

# 🌐 Streamlit Dashboard

The Streamlit application provides an interactive version of the analysis with multiple pages.

### Pages

- Home
- Advanced KPI Dashboard
- Detailed Analysis
- Business Insights

### Features

- Interactive visualizations
- KPI cards
- Plotly charts
- Executive business insights
- Responsive layout

---

# 📊 Key Findings

- Album tracks represent **52.88%** of playlist entries, indicating a balanced preference for album releases.

- Explicit songs account for **56.26%** of the playlist, showing strong audience acceptance.

- Clean songs still represent **43.74%**, indicating balanced content compliance.

- Songs around **3 minutes** dominate the playlist, matching modern streaming behavior.

- Large albums generally have lower average popularity than small albums.

- The average popularity score of **76.65** indicates that the playlist mainly contains highly popular tracks.

- Werenoi appears most frequently, highlighting strong artist retention.

---

# 💡 Business Recommendations

- Maintain a balanced mix of album releases and singles.

- Continue producing songs around three minutes to match listener preferences.

- Focus on compact album releases to maximize track popularity.

- Balance explicit and clean content for broader audience reach.

- Strengthen collaborations with consistently high-performing artists.

---



---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/France_Playlist_Streamlit.git
```

Navigate to the project folder

```bash
cd France_Playlist_Streamlit
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🌍 Live Demo

**Streamlit App**



---

# 📷 Dashboard Preview



---

# 👩‍💻 Developed By

**Shriya Mehta**



---

# 📄 License

This project is developed for educational and internship purposes only.
