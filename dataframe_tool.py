import json


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
