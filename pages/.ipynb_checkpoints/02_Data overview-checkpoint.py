import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

#from page_1 import player
with st.expander('Player 1'):
    df = st.session_state['df']
    st.write(df)
    pl1 = df[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z']]
    pl1 = pl1[pl1['lap_number'] > 0]
    pl1['velocity_X'] = pl1['velocity_X'] * 3.6
    pl1['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
    pl1['totalDistance'] = pl1['binDistance'].cumsum() / 1000
    pl1['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
    pl1 = pl1[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z']]
    #st.write(pl1)
    # Player 1 fastest lap
    maxTime = pl1.groupby('lap_number')['lap_time'].max().reset_index()
    pl1 = pd.merge(pl1,maxTime, on='lap_number')
    pl1 = pl1[pl1['lap_number'] < 5]
    pl1 = pl1[(pl1['lap_time_y'] == pl1['lap_time_y'].min())]
    st.session_state['pl1'] = pl1
    
    
    

with st.expander('player 2'):    
    df1 = st.session_state['df1']
    st.write(df1)
    pl2 = df1[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z']]
    pl2 = pl2[pl2['lap_number'] > 0]
    pl2['velocity_X'] = pl2['velocity_X'] * 3.6
    pl2['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
    pl2['totalDistance'] = pl2['binDistance'].cumsum() / 1000
    pl2['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
    pl2 = pl2[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance', 'filename', 'world_position_X', 'world_position_Y', 'world_position_Z']]
    #st.write(pl2)
    # Player 2 fastest lap
    maxTime = pl2.groupby('lap_number')['lap_time'].max().reset_index()
    pl2 = pd.merge(pl2,maxTime, on='lap_number')
    pl2 = pl2[pl2['lap_number'] < 5]
    pl2 = pl2[(pl2['lap_time_y'] == pl2['lap_time_y'].min())]
    st.session_state['pl2'] = pl2






