import pandas as pd
import numpy as np

import streamlit as st

import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

st.set_page_config(
    page_title="F1 Telemetry App",
    page_icon="🏎️",
)

#load in cached data
pl1 = st.session_state['pl1']
pl2 = st.session_state['pl2']

fig = go.Figure()
fig.add_trace(go.Scatter(x=pl1["world_position_X"], y=pl1["world_position_Y"], name='player 1'))
fig.add_trace(go.Scatter(x=pl2["world_position_X"], y=pl2["world_position_Y"], name='player 2'))
fig.update_layout(
    width=1100,
    height=1000,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
)
st.plotly_chart(fig)

