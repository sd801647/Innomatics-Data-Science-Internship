import streamlit as st
import pandas as pd
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path of directory_of_interest
dir_of_interest = os.path.join(FILE_DIR, "data")
DATA_PATH = os.path.join(dir_of_interest, "open_pubs.csv")
df=pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Home")

st.sidebar.success("navigate pages ^ ")
st.title("Open Pubs near me")
st.subheader('Dataset')
st.dataframe(df)

st.subheader('Covariance in dataset')
st.dataframe(df.cov())

st.subheader('Satistical Analysis')    
st.dataframe(df.describe())

st.subheader('Correlation')  
st.dataframe(df.corr())
