import streamlit as st

st.set_page_config(
    page_title="Investor Portal",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 Quant Fund Investor Portal")

st.markdown("""
### Institutional Reporting Dashboard

Navigate using the sidebar:

- Fund Overview
- Performance
- Risk Analytics
- Attribution
- Strategy Tear Sheets
""")