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

color = pl1['velocity_X']
x = pl1['world_position_X']          # values for x-axis
y = pl1['world_position_Y']
colormap = mpl.cm.plasma
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)


fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))
fig.suptitle('Player 1', size=24, y=0.97)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)
ax.axis('off')

# After this, we plot the data itself.
# Create background track line
ax.plot(pl1['world_position_X'] , pl1['world_position_Y'] , color='black', linestyle='-', linewidth=15, zorder=0)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(color.min(), color.max())
lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle='-', linewidth=5)

# Set the values used for colormapping
lc.set_array(color)

# Merge all line segments together
line = ax.add_collection(lc)


# Finally, we create a color bar as a legend.
cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])
normlegend = mpl.colors.Normalize(vmin=color.min(), vmax=color.max())
legend = mpl.colorbar.ColorbarBase(cbaxes, norm=normlegend, cmap=colormap, orientation="horizontal")

st.pyplot(plt)

color = pl2['velocity_X']
x = pl2['world_position_X']          # values for x-axis
y = pl2['world_position_Y']
colormap = mpl.cm.plasma
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)


fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))
fig.suptitle('Player 2', size=24, y=0.97)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)
ax.axis('off')

# After this, we plot the data itself.
# Create background track line
ax.plot(pl2['world_position_X'] , pl2['world_position_Y'] , color='black', linestyle='-', linewidth=15, zorder=0)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(color.min(), color.max())
lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle='-', linewidth=5)

# Set the values used for colormapping
lc.set_array(color)

# Merge all line segments together
line = ax.add_collection(lc)


# Finally, we create a color bar as a legend.
cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])
normlegend = mpl.colors.Normalize(vmin=color.min(), vmax=color.max())
legend = mpl.colorbar.ColorbarBase(cbaxes, norm=normlegend, cmap=colormap, orientation="horizontal")

st.pyplot(plt)
