import streamlit as st

from styles.theme import load_css
from components.header import show_header
from components.cards import metric_card

# Header
show_header(
    "🔐 Privacy-Preserving Multimodal RAG",
    "Monitor your AI System"
)

st.write("")

# ===========================
# Metric Cards
# ===========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card(
        "Documents",
        "0",
        "📄",
        "#E67E22"
    )

with col2:
    metric_card(
        "Images",
        "0",
        "🖼️",
        "#F4B400"
    )

with col3:
    metric_card(
        "Stored Entities",
        "0",
        "🧠",
        "#8E5A3C"
    )

with col4:
    metric_card(
        "Forgotten",
        "0",
        "🗑️",
        "#E57373"
    )

st.divider()

# ===========================
# System Status & Activity
# ===========================

left, right = st.columns([2, 1])

with left:
    st.subheader("⚡ System Status")

    st.success("✅ Streamlit Running")
    st.info("⏳ ChromaDB - Not Connected")
    st.info("⏳ Gemini API - Not Connected")

with right:
    st.subheader("📋 Recent Activity")

    st.write("• Project Initialized")
    st.write("• Waiting for document upload")