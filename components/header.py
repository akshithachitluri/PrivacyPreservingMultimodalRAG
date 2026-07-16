import streamlit as st

def show_header(title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <div class="main-title">{title}</div>
        <div class="sub-title">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)