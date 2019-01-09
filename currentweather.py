#!/usr/bin/python
import pyowm
import os
import sys

def celsius(kelvin):
    return kelvin-273.15

def fahrenheit(kelvin):
    return (9/5)*(kelvin-273.15)+32

if __name__ == "__main__":

    city_var = 'CITY_NAME'
    try:
        city = os.environ[city_var]
    except KeyError:
        print city_var + ': No city pointed'
        sys.exit(1)

    api_key = 'OPENWEATHER_API_KEY'
    try:
        api_key = os.environ[api_key]
    except KeyError:
        print api_key + ': No API key added'
        sys.exit(1)

    owm = pyowm.OWM(API_key=api_key, version='2.5')
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    print 'source=openweathermap,',\
          'city=' + '"' + city + '",',\
          'description=' + '"' +  str(w.get_detailed_status()) + '",',\
          'temp=' + str(celsius(w.get_temperature()['temp'])) + ",",\
          'humidity=' + str(w.get_humidity())
