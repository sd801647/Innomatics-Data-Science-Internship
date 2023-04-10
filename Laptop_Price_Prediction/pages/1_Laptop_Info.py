import streamlit as st
import os
import time
import pickle
import pandas as pd

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

st.title("Find Your Laptop")

data_path = os.path.join(dir_of_interest, "data", "df.pkl")

lap = pickle.load(open(data_path, 'rb'))

df = pd.DataFrame(lap)

laptop = df["Product"].values
index = df["Product"].index
st.subheader("Information About Some of Laptop Model")
selected_laptop_name = st.selectbox("Select the model", laptop)
button = st.button("See Result")
if button:
    info = df.loc[df['Product'] == selected_laptop_name]
    st.write(info.iloc[0])
    st.subheader("Visit the next page for laptop price prediction")