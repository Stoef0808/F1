import streamlit as st
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import datetime

pl1 = st.session_state['pl1']

pl2 = st.session_state['pl2']
maxTime = pl2.groupby('lap_number')['lap_time'].max().reset_index()
pl2 = pd.merge(pl2,maxTime, on='lap_number')
pl2_test = pl2[(pl2['lap_time_y'] == pl2['lap_time_y'].min()) & pl2['lap_number'] < pl2['lap_number'].max()]

st.write(maxTime)
st.write(pl2_test)
pl1Fast = pl1.groupby('lap_number')['lap_time'].max()
pl2Fast = pl2.groupby('lap_number')['lap_time_y'].max()

st.write(pl1Fast)
st.write(pl2Fast)

fig = go.Figure()
fig.add_trace(go.Scatter(x=pl1["binIndex"], y=pl1["velocity_X"], name='lap_number'))
fig.add_trace(go.Scatter(x=pl2["binIndex"], y=pl2["velocity_X"], name='lap_number'))
st.plotly_chart(fig)
"""
laps = pd.concat([pl1,pl2])
player = laps['lap_number'].unique().tolist()


players = st.sidebar.multiselect("select laps", player)


dfs = {player: laps[laps["lap_number"] == player] for player in players}

fig = go.Figure()
for player, laps in dfs.items():
    fig = fig.add_trace(go.Scatter(x=laps["binIndex"], y=laps["velocity_X"], name=player))

    st.plotly_chart(fig)
"""