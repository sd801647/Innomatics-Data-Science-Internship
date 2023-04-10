import streamlit as st
import os
import time
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

st.title("Laptop Price Prediction")

data_path = os.path.join(dir_of_interest, "data", "df.pkl")
ml_data = os.path.join(dir_of_interest, "data", "rf.pkl")
model = os.path.join(dir_of_interest, "data", "model.pkl")

lap = pickle.load(open(data_path, 'rb'))
rf = pickle.load(open(ml_data, 'rb'))

df = pd.DataFrame(lap)

# ----------------------------------------ML section------------------------------------------
features = ["brand", "processor", "ram", "os", "Storage"]
f = df[["brand", "processor", "ram", "os", "Storage"]]
y = np.log(df['MRP'])
X_train, X_test, y_train, y_test = train_test_split(f, y, test_size=0.2, random_state=47)
step1 = ct(transformers=[
    ('encoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,3,4])
],remainder='passthrough')

step2 = RandomForestRegressor(n_estimators=100,
                              random_state=3,
                              max_samples=0.5,
                              max_features=0.75,
                              max_depth=15)

pipe = Pipeline([
    ('step1',step1),
    ('step2',step2)
])

pipe.fit(X_train,y_train)
# -----------------------------------Input Section---------------------------------------------
brand = st.selectbox("Select the Brand:- ", df["brand"].unique())
processor = st.selectbox("Select the Processor:- ", df["processor"].unique())
ram = st.selectbox("Select the RAM:- ", df["ram"].unique())
os = st.selectbox("Select the Operating Syatem:- ", df["os"].unique())
Storage = st.selectbox("Select the Storage:- ", df["Storage"].unique())
butt = st.button("Predict")

query = np.array([brand, processor, ram, os, Storage])
query = query.reshape(1, -1)
p = pipe.predict(query)[0]
result = np.exp(p)
st.subheader("Your Predicted Prize is: ")
st.subheader(":red[₹{}]".format(result.round(2)))