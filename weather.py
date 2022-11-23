from config import WEATHER_KEY
from pyowm import OWM
from pyowm.utils import timestamps

owm = OWM(WEATHER_KEY)
mgr = owm.weather_manager()

def current_temperature(city):
    observation = mgr.weather_at_place(f'{city},RU')
    w = observation.weather
    
    return w.temperature('celsius')['temp']

def tomorrow_temperature(city):
    forecast = mgr.forecast_at_place(f'{city},RU', '3h')
    answer = forecast.get_weather_at(timestamps.tomorrow())

    return answer.temperature('celsius')['temp']