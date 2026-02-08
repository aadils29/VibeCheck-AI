"""VibeCheck AI — AI-Powered Vibe-to-Playlist Generator."""

import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="VibeCheck AI",
    page_icon="🎵",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("🎵 VibeCheck AI")
st.subheader("Describe your vibe. Get a playlist.")

# ---------------------------------------------------------------------------
# Vibe input
# ---------------------------------------------------------------------------
vibe = st.text_area(
    "What's your vibe?",
    placeholder="e.g. Studying in a rainy castle at 2 a.m. with a cup of tea…",
    max_chars=500,
    height=120,
)

# ---------------------------------------------------------------------------
# Action buttons
# ---------------------------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    generate = st.button("🎧 Generate Playlist", type="primary", disabled=not vibe)

with col2:
    if st.button("🗑️ Clear"):
        st.rerun()

# ---------------------------------------------------------------------------
# Playlist output (placeholder for Step 2 — Gemini integration)
# ---------------------------------------------------------------------------
if generate and vibe:
    st.info("⏳ Playlist generation coming soon — Gemini integration is next!")
