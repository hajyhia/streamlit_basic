import streamlit as st
import json
import pandas as pd
import datetime
import pytz
from timezonefinder import TimezoneFinder


def load_weather_data(file):
    with open(file, "r") as file:
        data = json.load(file)
    # print(data["hourly"])
    return data


def get_hourly_weather_data(weather_data_):
    new_list = []
    for item in weather_data_["hourly"]:
        new_item = {}
        for key, value in item.items():
            if key != 'weather':
                new_item[key] = value
            else:
                new_item.update(value[0])
        new_list.append(new_item)

    # for item in new_list:
    #     print(item)

    return new_list


weather_data = load_weather_data("weather_data.json")
hourly_weather_data = get_hourly_weather_data(weather_data)
df = pd.DataFrame(hourly_weather_data)
df.to_csv("hourly_weather_data.csv")
# with open("hourly_weather_data.csv", 'w') as file:
#     file.write()

# st.line_chart(df, x='x', y='y')
print(df)
# print(df['dt'])
# print(df.loc[0])
# print(df[df['temp'] > 11])
# print(datetime.datetime.fromtimestamp(1735225200).strftime("%I %p"))
df['hourly'] = df['dt'].apply(lambda dt_: datetime.datetime.fromtimestamp(dt_).strftime("%I %p"))
# df['hourly'] = datetime.datetime.fromtimestamp(df['dt']).strftime("%I %p")
print(df.tail(10))
st.line_chart(df.tail(10), x='hourly', y='temp')
