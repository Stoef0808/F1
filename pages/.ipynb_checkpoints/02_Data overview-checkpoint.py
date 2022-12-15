import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import re
import gc

st.set_page_config(
    page_title="F1 Telemetry App",
    page_icon="🏎️",
)


def transformCSV(data):
    df = data[['carId',
               'trackId', 
               'binIndex', 
               'lap_number',
               'lap_distance',
               'velocity_X',
               'lap_time', 
               'fuel',
               'filename',
               'world_position_X',
               'world_position_Y', 
               'world_position_Z',
               'throttle', 'brake',
               'tyre_wear_0',
               'tyre_wear_1',
               'tyre_wear_2',
               'tyre_wear_3',
               'tyre_temp_0',
               'tyre_temp_1',
               'tyre_temp_2',
               'tyre_temp_3']]
    df = df[df['lap_number'] > 0] # openingsronde buiten beschouwing laten
    df['velocity_X'] = df['velocity_X'] * 3.6 # omrekenen m/s naarkm/h
    df['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
    df['totalDistance'] = df['binDistance'].cumsum() / 1000 # berekenen van de totale afstand gereden in kilometers
    df['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
    df['Right front'] = df['tyre_wear_0'] * 100 #0 is rechts voor
    df['Left front'] = df['tyre_wear_1'] * 100 #1 is links voor
    df['Right rear'] = df['tyre_wear_2'] * 100 #2 is rechts achter
    df['Left rear'] = df['tyre_wear_3'] * 100 #3 is links achter
    df['Right front tyre temp'] = df['tyre_temp_0']#0 is rechts voor
    df['Left front tyre temp'] = df['tyre_temp_1']#1 is links voor
    df['Right rear tyre temp'] = df['tyre_temp_2']#2 is rechts achter
    df['Left rear tyre temp'] = df['tyre_temp_3']#3 is links achter
    df['throttle'] = df['throttle'] * 100 # data transformeren naar percentage
    df['brake'] = df['brake'] * 100 # data transformeren naar percentage
    data = df[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'filename','totalDistance', 'world_position_X', 'world_position_Y', 'world_position_Z', 'throttle', 'brake', 'Right front', 'Left front', 'Right rear', 'Left rear', 'Right front tyre temp', 'Left front tyre temp',
              'Right rear tyre temp', 'Left rear tyre temp']]
    return data


def time(df):
    time = df[df['lap_number'].between(0,4)]
    time = time.groupby('lap_number')['lap_time'].max()
    return time

def laptime(df):
    laptime = df.groupby(['lap_number'], sort=False)['lap_time'].max()
    laptime = laptime.iloc[:-1]
    #aptime = laptime[laptime['lap_time'] > 0]
    laptime = laptime.replace(0,np.NaN)
    laptime = laptime.mean()
    return laptime

col1, col2, col3, col4 = st.columns(4)
#from page_1 import player

with col1: 
    st.empty()

    
with col2:
    df = st.session_state['df']
    pl1 = transformCSV(df)
    cm1 = transformCSV(df)
    st.session_state['cm1'] = cm1
    del(df)
    gc.collect()

    st.title('Results of player 1')

    st.subheader('Collected data of player 1')
    with st.expander('Show data'):
        st.markdown("""
        This shows the raw data that is collected through Sim Racing Telemetry.
        """)
        st.write(pl1.head(1000))
    # averages per lap
    pl1_stats = pl1.groupby('lap_number')['velocity_X', 'throttle', 'brake'].mean().reset_index()
    st.subheader('Averages')
    st.write(pl1_stats)
    
    # average laptime
    timePl1 = time(pl1)
    st.dataframe(timePl1.to_frame().style.highlight_min(axis=0))
    
    
    avgTimePl1 = laptime(pl1)
    st.subheader('Average lap time')
    st.write("Player 1's average laptime:" ,avgTimePl1)
    #st.write(laptime)
    # Player 1 fastest lap
    



    pl1_statsMax = pl1.groupby('lap_number')[['velocity_X', 'throttle', 'brake']].max().reset_index()
    st.subheader('Max values')
    st.write(pl1_statsMax)


    maxTime = pl1.groupby('lap_number')['lap_time'].max().reset_index()
    pl1 = pd.merge(pl1,maxTime, on='lap_number')
    pl1 = pl1[pl1['lap_number'] < 5]
    pl1 = pl1[(pl1['lap_time_y'] == pl1['lap_time_y'].min())]
    st.session_state['pl1'] = pl1
    
   
    
    
    

with col3:
   
    st.title('Results of player 2')
    df1 = st.session_state['df1']
    pl2 = transformCSV(df1)
    cm2 = transformCSV(df1)
    st.session_state['cm2'] = cm2
    del(df1)
    gc.collect()

    st.subheader('Collected data of player 2')
    with st.expander('Show data'):
         
        st.write(pl2.head(1000))
    
    
    pl2_stats = pl2.groupby('lap_number')['velocity_X', 'throttle', 'brake'].mean().reset_index()
    st.subheader('Averages')
    st.write(pl2_stats)
    #st.write(pl2)
    
    
    timePl2 = time(pl2)
    st.dataframe(timePl2.to_frame().style.highlight_min(axis=0))
    
    
    avgTimePL2 = laptime(pl2)
    st.subheader('Average lap time')
    st.write("Player 2's average laptime:" , avgTimePL2)
    
    pl2_statsMax = pl2.groupby('lap_number')['velocity_X', 'throttle', 'brake'].max().reset_index()
    st.subheader('Max values')
    st.write(pl2_statsMax)
    # Player 2 fastest lap
    maxTime = pl2.groupby('lap_number')['lap_time'].max().reset_index()
    #st.write(maxTime)
    pl2 = pd.merge(pl2,maxTime, on='lap_number')
    pl2 = pl2[pl2['lap_number'] < 5]
    pl2 = pl2[(pl2['lap_time_y'] == pl2['lap_time_y'].min())]
    st.session_state['pl2'] = pl2

with col4:
    st.empty()




