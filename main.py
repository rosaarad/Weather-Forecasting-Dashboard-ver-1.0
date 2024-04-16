import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

city_names = pd.read_excel('city_names.xlsx')
current_weather = pd.read_excel('current_Weather.xlsx')
weather_hour1 = pd.read_excel('weather_hour1.xlsx') 
weather_hour2 = pd.read_excel('weather_hour2.xlsx') 
weather_hour3 = pd.read_excel('weather_hour3.xlsx') 
weather_hour4 = pd.read_excel('weather_hour4.xlsx')  
weather_hour5 = pd.read_excel('weather_hour5.xlsx')  
airPollution_tehran = pd.read_excel('airPollution_tehran.xlsx') 

st.title("Weather Forecasting Dashboard ver-1.0")
st.write("This is a streamlit app that shows the data driven from weather website API")
st.write("Made By: Rosa Rad")


tab1, tab2, tab3 = st.tabs(["Current Weather", "Weather Forecast", "Air Pollution Forecast"])

with tab1:
    st.subheader('Current Weather', divider='rainbow')
    st.write(current_weather)
    
    if st.checkbox("search"):
        selected_weathers = st.multiselect("Select weathers:", current_weather["weather"].unique())
        data_multiweather = current_weather.loc[current_weather["weather"].apply(lambda w: w in selected_weathers)]
        st.write(f"Filtered data: ")
        st.write(data_multiweather)



with tab2:
    st.subheader('Weather Forecast', divider='rainbow')
    if st.toggle("Show Selected Element "):
        selected2 = st.selectbox("Select a country/city:", city_names["Country"])
        data_forecast1 = weather_hour1.loc[weather_hour1["Country"] == selected2]
        st.write(f"Weather of {selected2} in 1 hour: ")
        st.write(data_forecast1)

        data_forecast2 = weather_hour2.loc[weather_hour2["Country"] == selected2]
        st.write(f"Weather of {selected2} in 3 hours: ")
        st.write(data_forecast2)

        data_forecast3 = weather_hour3.loc[weather_hour3["Country"] == selected2]
        st.write(f"Weather of {selected2} in 6 hours: ")
        st.write(data_forecast3)

        data_forecast4 = weather_hour4.loc[weather_hour4["Country"] == selected2]
        st.write(f"Weather of {selected2} in 9 hours: ")
        st.write(data_forecast4)

        data_forecast5 = weather_hour5.loc[weather_hour5["Country"] == selected2]
        st.write(f"Weather of {selected2} in 12 hours: ")
        st.write(data_forecast5)

    if st.toggle("Show All Elements "):
        st.markdown("##### 1 hour later:")
        st.write(weather_hour1)

        st.markdown("##### 3 hours later:")
        st.write(weather_hour2)

        st.markdown("##### 6 hours later:")
        st.write(weather_hour3)

        st.markdown("##### 9 hours later:")
        st.write(weather_hour4)

        st.markdown("##### 12 hours later:")
        st.write(weather_hour5)

with tab3:
    st.subheader('Air Pollution - Tehran', divider='rainbow')
    st.write(airPollution_tehran)

    figure = px.line(airPollution_tehran, x="date", y="Overall Air Quality", title="Overall Air Quality in Tehran")
    st.plotly_chart(figure)