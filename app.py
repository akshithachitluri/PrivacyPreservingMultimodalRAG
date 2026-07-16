import streamlit as st

from styles.theme import load_css
from components.header import show_header

st.set_page_config(
    page_title="Privacy-Preserving Multimodal RAG",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

show_header(
    "🔐 Privacy-Preserving Multimodal RAG",
    "Monitor your AI System"
)

st.write("")

st.markdown("""
## 👋 Welcome

This project implements a **Privacy-Preserving Multimodal Retrieval-Augmented Generation System**
with **Selective Knowledge Unlearning and Entity Forgetting** for Vision-Language Assistants.

Use the navigation menu on the left to explore different modules.
""")

st.info("Select a page from the sidebar to get started.")