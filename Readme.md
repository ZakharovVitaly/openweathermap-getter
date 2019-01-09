Script retrieves weather data from https://openweathermap.org/api
It uses the current weather data API https://openweathermap.org/current and uses pyowm library: https://pypi.python.org/pypi/pyowm

The python script uses no arguments, it using only environment variables:
OPENWEATHER_API_KEY and CITY_NAME

Example:

export OPENWEATHER_API_KEY="xxxxxxxxxxxx" && export CITY_NAME="Moscow"

./getweather.py

source=openweathermap, city="Moscow", description="few clouds", temp=-10.2, humidity=75
