import requests
from datetime import datetime

ApiKey = '90320064e22ef4634c0056f44fe6b7b1'

def get_weather(city):

    base_url = ("http://api.openweathermap.org/data/2.5/weather?appid="+ApiKey+"&q="+city)

    data = requests.get(base_url).json()

    return data


def convert_data(data):
    try:
        new_temp = ((float(data['main']['temp'])) - 273.15) * 9/5 + 32

        max_temp = ((float(data['main']['temp_max'])) - 273.15) * 9/5 + 32

        min_temp = ((float(data['main']['temp_min'])) - 273.15) * 9/5 + 32

        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')

        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')

        weather_cond = str(data['weather'][0]['description'])

        wind_direct = data['wind']['deg']

        wind_speed = (float(data['wind']['speed'])) * 2.237


        return round(new_temp, 2), round(max_temp, 2), round(min_temp, 2), sunrise, sunset, weather_cond, wind_direct, wind_speed

    except (ValueError, KeyError):
        print("Weather data not available")


def main():

    city = input("Enter city name: ")

    weather_data = get_weather(city)
    converted = convert_data(weather_data)

    try:
        converted_list = list(converted)
        if weather_data:
            print(f"Temperature: {converted_list[0]} F°")
            print(f"Maximum Temperature: {converted_list[1]} F°")
            print(f"Minimum Temperature: {converted_list[2]} F°")
            print(f"Sunrise: {converted_list[3]}")
            print(f"Sunset: {converted_list[4]}")
            print(f"Visibility: {converted_list[5]}")
            print(f"Wind: Due {converted_list[6]}° at {converted_list[7]} mph")

        else:
            print("Weather data not available")

    except (ValueError, KeyError, TypeError):
        print("", end="")




if __name__ == "__main__":
    main()
