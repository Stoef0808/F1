import streamlit as st
import pandas as pd
import numpy

st.set_page_config(
    page_title="F1 Telemetry App",
    page_icon="🏎️",
)

st.title("Data Driven Business Lab")
st.subheader("F1 project")
st.markdown("""
Welcome to the DDBL F1 project. On this page you can upload your CSV files. 
""")



uploaded_file = st.file_uploader('Upload race data player 1!', key='player1',type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep = '\t')
    df['filename'] = uploaded_file.name
    st.session_state['df'] = df

uploaded_file = st.file_uploader('Upload race data player 2!', key='player2',type="csv")
if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file, sep = '\t')
    df1['filename'] = uploaded_file.name
    st.session_state['df1'] = df1

 

