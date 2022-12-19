import streamlit as st
import plotly.graph_objects as go
import pandas 

pl1 = st.session_state['cm1']
pl2 = st.session_state['cm2']

#@@
fig = go.Figure()

fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Right rear'], name='Right rear'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Left rear'], name='Left rear'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Right front'], name='Right front'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Left front'], name='Left front'))
fig.add_trace(go.Scatter(x=pl2['totalDistance'], y=pl2['Right rear'], name='Right rear P2'))
fig.add_trace(go.Scatter(x=pl2['totalDistance'], y=pl2['Left rear'], name='Left rear P2'))
fig.add_trace(go.Scatter(x=pl2['totalDistance'], y=pl2['Right front'], name='Right front P2'))
fig.add_trace(go.Scatter(x=pl2['totalDistance'], y=pl2['Left front'], name='Left front P2'))
fig.update_layout(
    title='Tyre Deg player 1',
    xaxis_title='Distance lap',
    yaxis_title='Tyre deg',
    width=1200,
    height=1000,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
updatemenus=[
       dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, True, True, True,True,True,True,True]}],
                    label="All tyres",
                    method="update"
                ),
                dict(
                    args=[{'visible': [True, True, True, True,False,False,False,False]}],
                    label="All tyres player 1",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, False, False, True, True, True, True]}],
                    label="All tyres player 2",
                    method="update"
                ),
            ]),
        ),   
    ]
)

st.plotly_chart(fig)
#@@
fig = go.Figure()

fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['fuel'], name='Fuel usage player 1'))
fig.add_trace(go.Scatter(x=pl2['totalDistance'], y=pl2['fuel'], name='Fuel usage player 2'))
fig.update_layout(title='Fuel ussage',
                   xaxis_title='Distance on track',
                   yaxis_title='Kilo fuel')
st.plotly_chart(fig)
#@@
fig = go.Figure()

fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Right rear tyre temp'], name='Right rear'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Left rear tyre temp'], name='Left rear'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Right front tyre temp'], name='Right front'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl1['Left front tyre temp'], name='Left front'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl2['Right rear tyre temp'], name='Right rear'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl2['Left rear tyre temp'], name='Left rear'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl2['Right front tyre temp'], name='Right front'))
fig.add_trace(go.Scatter(x=pl1['totalDistance'], y=pl2['Left front tyre temp'], name='Left front'))
fig.update_layout(
    title='Tyre temp',
    xaxis_title='Distance lap',
    yaxis_title='Tyre deg',
    width=1200,
    height=1000,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    updatemenus=[
       dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, True, True, True,True,True,True,True]}],
                    label="All tyres",
                    method="update"
                ),
                dict(
                    args=[{'visible': [True, True, True, True,False,False,False,False]}],
                    label="All tyres player 1",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, False, False, True, True, True, True]}],
                    label="All tyres player 2",
                    method="update"
                ),
            ]),
        ),   
    ]
)

st.plotly_chart(fig)
