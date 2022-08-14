import requests
import datetime
from pprint import pprint
from config import OW_TOKEN

def get_weather(city,OW_TOKEN):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW_TOKEN}&units=metric"
        )
        data = r.json()
        pprint(data)
        city = data["name"]
        cur_weather = data["main"]["temp"]
        feel_weather = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        print(F"City: {city}\n"
              f"Temperature: {cur_weather}C; Feels like: {feel_weather}C;\n"
              f"Humidity: {humidity}%; Pressure: {pressure} mmHg; Speed of wind: {wind}m/s;\n"
              f"Sunrise: {sunrise_timestamp}; Sunset: {sunset_timestamp}; Length of day: {length_day};\n"
              f"Good day!")
    except Exception as ex:
        print(ex)
        print("Check city's name")

def main():
    city = input("Enter the city: ")
    get_weather(city, OW_TOKEN)

if __name__ == '__main__':
    main()