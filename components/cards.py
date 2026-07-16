import streamlit as st

def metric_card(title, value, icon, color):
    st.markdown(
        f"""
<div class="metric-card">
    <h1>{icon}</h1>
    <h4>{title}</h4>
    <h2 style="color:{color};">{value}</h2>
</div>
""",
        unsafe_allow_html=True
    )