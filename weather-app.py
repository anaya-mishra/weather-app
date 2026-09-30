import requests

# 1 API setup 
api_key = "22ecb2d195f89bf3fe3a09fbfb3a1d92" 
city = input("Enter city name: ")

# 2 get data from openweathermap 
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
weather_data = response.json()

# 3 check if the request was successful
if response.status_code == 200: 
    # 4 extract relevant data
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # 5 display the data
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Error: Unable to fetch weather data for {city}. Please check the city name and try again.")
