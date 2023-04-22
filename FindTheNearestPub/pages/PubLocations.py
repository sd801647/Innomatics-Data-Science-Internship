import streamlit as st
import pandas as pd
import numpy as np
import os
import app

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "data")
DATA_PATH = os.path.join(dir_of_interest, "open_pubs.csv")
df=pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Pub Locations")
opt=st.selectbox('',('Local Authority','Postal Code'))
if opt=='Local Authority':
    option=st.selectbox(opt,df.local_authority.unique())

    if st.button("Find"):
        pubs_data = df.loc[df["local_authority"]==option]
        "You searched for:",option
        "Total no of pubs in this location is:",len(pubs_data)
        st.map(pubs_data)
        st.dataframe(pubs_data)
else:
    pc=st.selectbox(opt,df.postcode.unique())

    if st.button("Find"):
        pubs_data = df.loc[df["postcode"]==pc]
        "You searched for:",pc
        "Total no of pubs in this location is:",len(pubs_data)
        st.map(pubs_data)
        st.dataframe(pubs_data)