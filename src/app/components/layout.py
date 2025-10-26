# src/app/components/layout.py
import streamlit as st

def set_page_style():
    """Set Streamlit page style and CSS."""
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #2b7cff;
            color: white;
            font-weight: 600;
            border-radius: 8px;
        }
        .stMetric {
            background-color: #f6f6f6;
            padding: 10px;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)
