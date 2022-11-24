import streamlit as st
import pandas as pd
#from page_1 import player

df = st.session_state['df']
pl1 = df[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel', 'filename']]
pl1 = pl1[pl1['lap_number'] > 0]
pl1['velocity_X'] = pl1['velocity_X'] * 3.6
pl1['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
pl1['totalDistance'] = pl1['binDistance'].cumsum() / 1000
pl1['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
pl1 = pl1[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance', 'filename']]
st.write(pl1)
st.session_state['pl1'] = pl1

df1 = st.session_state['df1']
pl2 = df1[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel', 'filename']]
pl2 = pl2[pl2['lap_number'] > 0]
pl2['velocity_X'] = pl2['velocity_X'] * 3.6
pl2['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
pl2['totalDistance'] = pl2['binDistance'].cumsum() / 1000
pl2['Time'] = pd.to_datetime(df.lap_time, unit='s').dt.time.astype(str).str[3:]
pl2 = pl2[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance', 'filename']]
st.write(pl2)
st.session_state['pl2'] = pl2


