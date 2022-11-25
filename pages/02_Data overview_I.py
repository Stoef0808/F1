import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

col1, col2 = st.columns(2)
#from page_1 import player
with col1:
    st.title('Results of player 1')
    
    df = st.session_state['df']
    st.subheader('Collected data of player 1')
    with st.expander('Show data'):
        st.write(df.head(1000))
    
    
    
    
    
    pl1 = df[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z', 'throttle', 'brake']]
    pl1 = pl1[pl1['lap_number'] > 0]
    pl1['velocity_X'] = pl1['velocity_X'] * 3.6
    pl1['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
    pl1['totalDistance'] = pl1['binDistance'].cumsum() / 1000
    pl1['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
    pl1 = pl1[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z', 'throttle', 'brake']]
    
    pl1_stats = pl1.groupby('lap_number')['velocity_X', 'throttle', 'brake'].mean().reset_index()
    st.subheader('Averages')
    st.write(pl1_stats)
    
    
    time = pl1[pl1['lap_number'].between(0,4)]
    time = time.groupby('lap_number')['lap_time'].max()
    st.dataframe(time.to_frame().style.highlight_min(axis=0))
    laptime = pl1.groupby(['lap_number'], sort=False)['lap_time'].max()
    laptime = laptime.iloc[:-1]
    #laptime = laptime[laptime['lap_time'] > 45]
    laptime = laptime.replace(0,np.NaN)
    st.subheader('Average lap time')
    st.write("Player 1's average laptime:" ,laptime.mean())
    #st.write(pl1)
    # Player 1 fastest lap
    
    
    
    pl1_statsMax = pl1.groupby('lap_number')['velocity_X', 'throttle', 'brake'].max().reset_index()
    st.subheader('Max values')
    st.write(pl1_statsMax)
    
    
    maxTime = pl1.groupby('lap_number')['lap_time'].max().reset_index()
    pl1 = pd.merge(pl1,maxTime, on='lap_number')
    pl1 = pl1[pl1['lap_number'] < 5]
    pl1 = pl1[(pl1['lap_time_y'] == pl1['lap_time_y'].min())]
    
    #st.write(maxTime)
    st.session_state['pl1'] = pl1
    
   
    
    
    

with col2:
    st.title('Results of player 2')
    df1 = st.session_state['df1']
    st.subheader('Collected data of player 2')
    with st.expander('Show data'):
        st.write(df1.head(1000))
    pl2 = df1[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z', 'throttle', 'brake']]
    pl2 = pl2[pl2['lap_number'] > 0]
    pl2['velocity_X'] = pl2['velocity_X'] * 3.6
    pl2['brake'] = pl2['brake'] * 100
    pl2['throttle'] =  pl2['throttle'] * 100
    pl2['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
    pl2['totalDistance'] = pl2['binDistance'].cumsum() / 1000
    pl2['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
    pl2 = pl2[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z', 'throttle', 'brake']]
    
    pl2_stats = pl2.groupby('lap_number')['velocity_X', 'throttle', 'brake'].mean().reset_index()
    st.subheader('Averages')
    st.write(pl2_stats)
    #st.write(pl2)
    
    
    time = pl2[pl2['lap_number'].between(0,4)]
    time = time.groupby('lap_number')['lap_time'].max()
    st.dataframe(time.to_frame().style.highlight_min(axis=0))
    laptime = pl2.groupby(['lap_number'], sort=False)['lap_time'].max()
    laptime = laptime.replace(0,np.NaN)
    st.subheader('Average lap time')
    st.write("Player 2's average laptime:" , laptime.mean())
    
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






