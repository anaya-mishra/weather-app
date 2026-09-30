# Weather App

Small python project that fetches current weather data for any city using the OpenWeatherMap API and displays the temperature, description, humidity, and wind speed. I made it to easily check live weather details right from the terminal.

It's a simple script, not a full weather dashboard. Don't use it for mission-critical weather forecasting or anything like that.

## What it does

It prompts the user to enter a city name, sends a request to the OpenWeatherMap API, and parses the JSON response. If the city is found and the request is successful, it extracts and displays:

* Current temperature in Celsius
* Weather description (e.g., clear sky, light rain)
* Humidity percentage
* Wind speed in m/s

If the city name is invalid or the request fails, it catches the error and lets you know.

## Running it

You need Python installed along with the `requests` library. Make sure to run the following command before running the script:

```bash
pip install requests
```

Once installed, place the script in your directory and run:

```bash
python weather-app.py
```

Type in any city name when prompted, and it will output the current weather conditions.

## Files

* `weather-app.py` handles the API connection, user input, data parsing, and console output.

*Note: The API key is hardcoded into the script for now, but will be moved to an environment variable or config file later.*

## What it doesn't do (yet)

Being honest here, it only fetches current weather and doesn't provide multi-day forecasts or historical data. There's also no graphical user interface (GUI)—it runs entirely in the terminal.

Other small things: it doesn't handle saved favorite cities, and it relies on an active internet connection to reach the OpenWeatherMap API.

## Todo

* 5-day / 3-hour forecast support
* Save favorite or recent cities
* Add a simple GUI (Tkinter or Streamlit)
* Move the API key out of the source code (environment variables)
* Better command-line argument parsing

Issues and PRs are welcome if you want to add features or fix something.

Made by [@anay-mishra](https://github.com/anay-mishra)