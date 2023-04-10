import streamlit as st
from PIL import Image
import os
from pathlib import Path

curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

pageTitle = "Laptop Price Recommendation"
st.title("This is an Application for Laptop Price Recommendation")

st.write(
    """
- ✔️ Go to Page 1 for Laptop Info
- ✔️ Go to Page 2 for Prediction Page
- ✔️ Go to Page 3 for Laptop Dashboard
"""
)