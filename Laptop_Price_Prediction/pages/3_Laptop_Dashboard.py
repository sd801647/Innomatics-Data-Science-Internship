import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import pickle

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

data_path = os.path.join(dir_of_interest, "data", "df.pkl")
lap = pickle.load(open(data_path, 'rb'))

df = pd.DataFrame(lap)

draft_template = go.layout.Template()
draft_template.layout.annotations = [
    dict(
        opacity=0.1,
        font=dict(color="red", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]

st.subheader("Visualization Without Filtering")
st.write(":blue[Zoom to better visualization]")
col1, col2, col3, col4 = st.columns(4)


avg_price = df.groupby("brand")["MRP"].mean().reset_index()
fig1 = px.bar(avg_price, x="brand", y="MRP", color="brand")
fig1.update_layout(template=draft_template, paper_bgcolor="lightblue",
                   title="<b> Avarage Price of Laptop of All Brand")
fig1.update_layout(
    font_color="white",
    title_font_color="white",
    legend_title_font_color="white"
)

col1.plotly_chart(fig1, use_container_width=True)

total_freq = df.processor.value_counts()[:10]
fig2 = go.Figure(
    data=[go.Pie(labels=total_freq.index, values=total_freq, pull=[0, 0.2], hole=0.3, title="<b> RITWIK </b>")])
fig2.update_traces(textposition="inside", textinfo="percent+label")
fig2.update_layout(paper_bgcolor="lightblue", title="<b> Total Brands Processor Wise(TOP 10)")
fig2.update_layout(
    font_color="white",
    title_font_color="white",
    legend_title_font_color="white"
)
col2.plotly_chart(fig2, use_container_width=True)

line = df.groupby("ram")["MRP"].mean().reset_index()
fig3 = px.line(line, x="ram", y="MRP")
fig3.update_layout(template=draft_template, paper_bgcolor="lightblue",
                   title="<b> Avarage Price RAM wise of All Brand")
fig3.update_layout(
    font_color="white",
    title_font_color="white",
    legend_title_font_color="white"
)
col3.plotly_chart(fig3, use_container_width=True)

os_plot = df.groupby("os")["MRP"].mean().reset_index()
fig4 = px.bar(os_plot, x="os", y="MRP", color="os")
fig4.update_layout(template=draft_template, paper_bgcolor="lightblue",
                   title="<b> Operating System Wise Avarage Price of All Brands")
fig4.update_layout(
    font_color="white",
    title_font_color="white",
    legend_title_font_color="white"
)
col4.plotly_chart(fig4, use_container_width=True)


st.subheader("Visualization With Filtering 📊")


st.header("The Input Section,Take Patience")
processor = st.selectbox("Select the Processor:- ", df["processor"].unique())
ram = st.selectbox("Select the RAM:- ", df["ram"].unique())
Storage = st.selectbox("Select the Storage:- ", df["Storage"].unique())


butt = st.button("submit")
col1, col2, col3, col4 = st.columns(4)


if butt:
    st.write(":green[Zoom to better visualization]")
    data = df[df["processor"] == processor]
    data = data[data["ram"] == ram]
    data = data[data["Storage"] == Storage]
    avg_price = data.groupby("brand")["MRP"].mean().reset_index()
    fig1 = px.bar(avg_price, x="brand", y="MRP", color="brand")
    fig1.update_layout(template=draft_template, paper_bgcolor="lightblue",
                      title="<b> Avarage Price of Laptop of All Brand")
    fig1.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    col1.plotly_chart(fig1, width=500,height=500, use_container_width=True)

    total_freq = data.processor.value_counts()[:10]
    fig2 = go.Figure(
        data=[go.Pie(labels=total_freq.index, values=total_freq, pull=[0, 0.2], hole=0.3, title="<b> RG </b>")])
    fig2.update_traces(textposition="inside", textinfo="percent+label")
    fig2.update_layout(paper_bgcolor="lightblue", title="<b> Total Brands Processor Wise(TOP 10)")
    fig2.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    col2.plotly_chart(fig2, width=1100,height=900, use_container_width=True)

    line = data.groupby("ram")["MRP"].mean().reset_index()
    fig3 = px.line(line, x="ram", y="MRP")
    fig3.update_layout(template=draft_template, paper_bgcolor="lightblue",
                      title="<b> Avarage Price RAM wise of All Brand")
    fig3.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    col3.plotly_chart(fig3, width=1100,height=900, use_container_width=True)

    os_plot = data.groupby("os")["MRP"].mean().reset_index()
    fig4 = px.bar(os_plot, x="os", y="MRP", color="os")
    fig4.update_layout(template=draft_template, paper_bgcolor="lightblue",
                      title="<b> Operating System Wise Avarage Price of All Brands")
    fig4.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    col4.plotly_chart(fig4, width=1100,height=900, use_container_width=True)
