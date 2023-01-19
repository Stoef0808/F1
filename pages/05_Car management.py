import streamlit as st
import plotly.graph_objects as go
import pandas 

pl1 = st.session_state['cm1']
pl2 = st.session_state['cm2']

#@@
Lap1 = [dict(type='square',
                 xref='x', yref='y',
                 x0=0, y0=0,
                 x1=5.441, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]

Lap2 = [dict(type='square',
                 xref='x', yref='y',
                 x0=5.442, y0=0,
                 x1=10.882, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
Lap3 = [dict(type='square',
                 xref='x', yref='y',
                 x0=10.883, y0=0,
                 x1=16.323, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
Lap4 = [dict(type='square',
                 xref='x', yref='y',
                 x0=16.303, y0=0,
                 x1=21.733, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]

fig = go.Figure()

fig.add_trace(go.Scatter(x=cm1['totalDistance'], y=cm1['Right rear'], name='Right rear'))
fig.add_trace(go.Scatter(x=cm1['totalDistance'], y=cm1['Left rear'], name='Left rear'))
fig.add_trace(go.Scatter(x=cm1['totalDistance'], y=cm1['Right front'], name='Right front'))
fig.add_trace(go.Scatter(x=cm1['totalDistance'], y=cm1['Left front'], name='Left front'))

button_layer_1_height = 1.12
button_layer_2_height = 1.065


fig.update_layout(title='Tyre Deg player 1',
                   xaxis_title='Distance lap',
                   yaxis_title='Tyre deg',
    width=1500,
    height=900,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
                  yaxis= dict(
                    tickmode = 'array',
                    tickvals = [0,5,10,15,20,25]
                )
               
                  
)

fig.update_layout(
    
    updatemenus=[
        dict(
            buttons=list([
                dict(label="No laps",
                         method="relayout",
                         args=["shapes", []]),
                dict(label="Lap 1",
                         method="relayout",
                         args=["shapes", Lap1]),
                dict(label="Lap 2",
                         method="relayout",
                         args=["shapes", Lap2]),
                dict(label="Lap 3",
                         method="relayout",
                         args=["shapes", Lap3]),
                dict(label="Lap 4",
                         method="relayout",
                         args=["shapes", Lap4]),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.15,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, True, True, True]}],
                    label="All tyres",
                    method="update"
                ),
                dict(
                    args=[{'visible': [True, False, False, False]}],
                    label="Right rear",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, True, False, False]}],
                    label="Left rear",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, True, False]}],
                    label="Right front",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, False, True]}],
                    label="Left front",
                    method="update"
                ),
                dict(
                    args=[{'visible': [True, True, False, False]}],
                    label="Rear tyres",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, True, True]}],
                    label="Front tyres",
                    method="update"
                ),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.15,
            xanchor="left",
            y=button_layer_2_height,
            yanchor="top",
        ),   
    ]
)

st.plotly_chart(fig)
#@@

Lap1 = [dict(type='square',
                 xref='x', yref='y',
                 x0=0, y0=0,
                 x1=5.441, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]

Lap2 = [dict(type='square',
                 xref='x', yref='y',
                 x0=5.442, y0=0,
                 x1=10.882, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
Lap3 = [dict(type='square',
                 xref='x', yref='y',
                 x0=10.883, y0=0,
                 x1=16.323, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
Lap4 = [dict(type='square',
                 xref='x', yref='y',
                 x0=16.303, y0=0,
                 x1=21.733, y1=24,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]

fig = go.Figure()

fig.add_trace(go.Scatter(x=cm2['totalDistance'], y=cm2['Right rear'], name='Right rear'))
fig.add_trace(go.Scatter(x=cm2['totalDistance'], y=cm2['Left rear'], name='Left rear'))
fig.add_trace(go.Scatter(x=cm2['totalDistance'], y=cm2['Right front'], name='Right front'))
fig.add_trace(go.Scatter(x=cm2['totalDistance'], y=cm2['Left front'], name='Left front'))

button_layer_1_height = 1.12
button_layer_2_height = 1.065


fig.update_layout(title='Tyre Deg player 1',
                   xaxis_title='Distance lap',
                   yaxis_title='Tyre deg',
    width=1500,
    height=900,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
                  yaxis= dict(
                    tickmode = 'array',
                    tickvals = [0,5,10,15,20,25]
                )
               
                  
)

fig.update_layout(
    
    updatemenus=[
        dict(
            buttons=list([
                dict(label="No laps",
                         method="relayout",
                         args=["shapes", []]),
                dict(label="Lap 1",
                         method="relayout",
                         args=["shapes", Lap1]),
                dict(label="Lap 2",
                         method="relayout",
                         args=["shapes", Lap2]),
                dict(label="Lap 3",
                         method="relayout",
                         args=["shapes", Lap3]),
                dict(label="Lap 4",
                         method="relayout",
                         args=["shapes", Lap4]),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.15,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, True, True, True]}],
                    label="All tyres",
                    method="update"
                ),
                dict(
                    args=[{'visible': [True, False, False, False]}],
                    label="Right rear",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, True, False, False]}],
                    label="Left rear",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, True, False]}],
                    label="Right front",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, False, True]}],
                    label="Left front",
                    method="update"
                ),
                dict(
                    args=[{'visible': [True, True, False, False]}],
                    label="Rear tyres",
                    method="update"
                ),
                dict(
                    args=[{'visible': [False, False, True, True]}],
                    label="Front tyres",
                    method="update"
                ),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.15,
            xanchor="left",
            y=button_layer_2_height,
            yanchor="top",
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
fig.update_layout(
    title='Tyre Deg player 1',
    xaxis_title='Distance lap',
    yaxis_title='Tyre deg',
    width=1200,
    height=1000,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white")

st.plotly_chart(fig)
