# F1
DDBL F1 streamlit application

## Introduction
In this project we are going to compare our F1 2021 laptimes. 
We made a streamlit website where you can upload CSV files and it will auto generate visualisations to compare the laptimes.

## Requirements

The requirements for this project are:
- F1 2021
- sim racing telemetry (F1 2021 model unlocked)
- Python 3.9
- streamlit 1.14.0
- Pandas 1.2.4
- Plotly 5.3.1
- Matplotlib 3.3.4
- Numpy 1.20.1

## Settings

Before you start recording the data, your F1 game needs to be on the following settings.
- Grand prix
- 5 laps (short)
- Cars need to be on equal performance
- Currently we only have the corners mapped out for spain but it will be a feature that can be added in the future. But other circuits can also be raced at but corners won't be mapped out in the telemetry.
- Currently you need to upload 2 player files, if you upload one file it will show errors. 

## Data collection

The data used in this notebook is gathered from the F1 2021 game. To extract data out of the game we use Sim Racing Telemetry. This is a 3d party application on steam that allows to record sessions in F1. It has an understandable UI and low effort in set up to connect to the game. All it requires the user to do is input the IP address of the device trying to connect to the game, into the telemetry settings of the game. 

<img src = "https://i.imgur.com/y3sHjIX.png">

As you can see, the telemetry app displays your IP. The ports should be set up already. If this is not the case go to this page for troubleshooting: https://www.simracingtelemetry.com/games/F12021/

It also has a quick guide into setting up the app

## Recorded sessions
Once you have recorded sessions, they will displayed on the openingscreen of the SRT application. You can see this below

<img src = "https://i.imgur.com/pzqDaIt.png">

If you open one of the recorded sessions, you can export this session to a CSV file that contains 193 columns of data. This ranges from laptimes and track information to damage picked up and tuning of the car. This can then all be used to analyze your track performance!

## Demo

Here is the link to the working online environment: https://jordds-f1-page-1-64jy3n.streamlit.app/ 

