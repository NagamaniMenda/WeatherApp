# Weather Forecast Dashboard App

This is a beginner-friendly Weather App built using Python, Tkinter, and the OpenWeatherMap API. It fetches real-time weather data for any city you enter and displays it in a user-friendly interface — with weather-specific icons and dynamic background images based on current conditions.

## Features

- City-based weather search
- Shows temperature in Celsius
- Weather condition and description
- Humidity and wind speed (basic)
- Weather icons (auto-fetched from OpenWeather)
- Dynamic background that changes for:
  - Clear sky
  - Cloudy
  - Rainy
  - Snowy
  - Thunderstorm
  - Light rain / scattered clouds (optional storm theme)
  - Default fallback
- Snow background triggered if temperature is less than or equal to 2°C

## Screenshots

(Add screenshots of your app showing clear, cloudy, rainy, etc. conditions here.)

## How to Run

1. Clone or Download this repository.
2. Make sure you have Python installed (version 3.6 or higher recommended).
3. Install the required libraries:

```bash
pip install requests pillow


Place the following background images in the same folder as your main.py file:

clear.jpg

clouds.jpg

rain.jpg

snow.jpg

storm.jpg

default.jpg

*Run the app:*

bash
Copy
Edit
python main.py
*API Used*
OpenWeatherMap API: https://openweathermap.org/api
Sign up and get a free API key.
Replace the API_KEY in the code with your personal key.

*File Structure*
arduino
Copy
Edit
WeatherApp/
├── main.py
├── clear.jpg
├── clouds.jpg
├── rain.jpg
├── snow.jpg
├── storm.jpg
├── default.jpg
└── README.md
*AUTHOR:*
Nagamani
BTech CSE Student
Weather App Project using Python

*Future Improvements*
Add multi-day forecast (3 to 5 days)

Option to switch between Celsius and Fahrenheit

Toggle between dark mode and light mode

Add sunrise/sunset and air quality information