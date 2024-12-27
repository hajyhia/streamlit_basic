import streamlit as st
import matplotlib.pyplot as plt
import dataframe_tool as df_tool
import pandas as pd
import datetime
import math
import requests

API_KEY = "a97bfd1e514bbcb662cacbee64cb8eab"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

# BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&units=metric&appid=5796abbde9106b7da4febfae8c44c232"
params = {
    "lat": 51.5085,
    "lon": -0.1257,
    "appid": "5796abbde9106b7da4febfae8c44c232",
    "units": "metric"  # Use "imperial" for Fahrenheit
}
response = requests.get(BASE_URL, params=params)
response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
print(response.json())

weather_data = response.json()
# weather_data = df_tool.load_weather_data("weather_data.json")
hourly_weather_data = df_tool.get_hourly_weather_data(weather_data)
df = pd.DataFrame(hourly_weather_data)
now_ = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
# print(now_)
df = df[df['dt'].apply(lambda dt_: datetime.datetime.fromtimestamp(dt_)) >= now_].head(10)
st.write(df)

df['hourly'] = df['dt'].apply(lambda dt_: datetime.datetime.fromtimestamp(dt_).strftime("%I %p"))

sorted_ = df
# sorted_ = df.sort_values('dt').head(24)
# print(sorted_)

# Example data
x = sorted_.index
y = sorted_['temp']
labels = sorted_['hourly']

# Create a line plot
plt.figure(figsize=(8, 4))
plt.plot(labels, y, color = 'red')
# plt.plot(labels, y, marker='o', linestyle='-', color='blue', label='Line Plot')
plt.xticks(rotation=90)

# locs, labels = plt.xticks()
# st.write(locs)
# st.write(labels)
# locs, labels = plt.yticks()
# st.write(locs)
# st.write(labels)
# for i in range(math.floor(min(y)), math.ceil(max(y) + 1), 1):
#     st.write(i)

# plt.yticks(ticks=y, labels=[f"{s}°" for s in y])

temp_l = list(range(math.floor(min(y)), math.ceil(max(y) + 1), 1))
# print(temp_l)
plt.yticks(ticks=temp_l, labels=[f"{s}°" for s in temp_l])

# Add labels to each point
# for i, label in enumerate(labels):
#     plt.text(x[i], y[i], label, fontsize=10, ha='left', va='bottom')

# Customize the chart
plt.title('Hourly forecast', fontsize=16)
# plt.xlabel('Hourly', fontsize=12)
# plt.ylabel('Temperature', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.4, axis="y")
# plt.legend()

# Show the plot
st.pyplot(plt)

