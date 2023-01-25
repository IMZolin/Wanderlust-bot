import requests
import datetime
from pprint import pprint
from config import OW_TOKEN
from googletrans import Translator, constants

translator = Translator()


def get_weather(city, OW_TOKEN):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW_TOKEN}&units=metric"
    )
    data = r.json()
    # pprint(data)
    city = data["name"]
    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        w_d = code_to_smile[weather_description]
    else:
        w_d = "OMG! Check it yourself please."
    x = w_d.split()
    w_d_rus = x[0]
    w_d_img = x[1]
    cur_weather = data["main"]["temp"]
    feel_weather = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    length_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
        data["sys"]["sunrise"])
    answer = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n City: {city}\n {w_d_img} Temperature: {cur_weather}C; Feels like: {feel_weather}C;\n Humidity: {humidity}%; Pressure: {pressure} mmHg; Speed of wind: {wind}m/s;\n Sunrise: {sunrise_timestamp}; Sunset: {sunset_timestamp}; Length of day: {length_day};\n Good day!"
    # print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    #         f"City: {city}\n"
    #       f"{w_d_img} Temperature: {cur_weather}C; Feels like: {feel_weather}C;\n"
    #       f"Humidity: {humidity}%; Pressure: {pressure} mmHg; Speed of wind: {wind}m/s;\n"
    #       f"Sunrise: {sunrise_timestamp}; Sunset: {sunset_timestamp}; Length of day: {length_day};\n"
    #       f"Good day!")
    return answer


def main():
    city = input("Enter the city: ")
    get_weather(city, OW_TOKEN)


if __name__ == '__main__':
    main()
