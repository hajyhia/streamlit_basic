import pandas as pd
import datetime
import dataframe_tool as dftools
import requests

# def load_weather_data(file):
#     with open(file, "r") as file:
#         data = json.load(file)
#     # print(data["hourly"])
#     return data
#
#
# def get_hourly_weather_data(weather_data_):
#     new_list = []
#     for item in weather_data_["hourly"]:
#         new_item = {}
#         for key, value in item.items():
#             if key != 'weather':
#                 new_item[key] = value
#             else:
#                 new_item.update(value[0])
#         new_list.append(new_item)
#
#     # for item in new_list:
#     #     print(item)
#
#     return new_list

API_KEY = "a97bfd1e514bbcb662cacbee64cb8eab"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

# BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&units=metric&appid=5796abbde9106b7da4febfae8c44c232"
params = {
    "lat": 51.5085,
    "lon": -0.1257,
    "appid": API_KEY,
    "units": "metric"  # Use "imperial" for Fahrenheit
}
response = requests.get(BASE_URL, params=params)
response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
print(response.json())

weather_data = dftools.load_weather_data("weather_data.json")
hourly_weather_data = dftools.get_hourly_weather_data(weather_data)
df = pd.DataFrame(hourly_weather_data)
# df.to_csv("hourly_weather_data.csv")
# with open("hourly_weather_data.csv", 'w') as file:
#     file.write()

# st.line_chart(df, x='x', y='y')
print(df)
# print(df['dt'])
# print(df.loc[0])
now_ = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
print(now_)
print(df[df['dt'].apply(lambda dt_: datetime.datetime.fromtimestamp(dt_)) >= now_])
# print(datetime.datetime.fromtimestamp(1735225200).strftime("%I %p"))
df['hourly'] = df['dt'].apply(lambda dt_: datetime.datetime.fromtimestamp(dt_).strftime("%I %p"))
# df['hourly'] = datetime.datetime.fromtimestamp(df['dt']).strftime("%I %p")
sorted_ = df.sort_values('dt').head(10)
print(sorted_)
# st.line_chart(sorted_, x='hourly', y='temp')
# st.write(sorted_)

