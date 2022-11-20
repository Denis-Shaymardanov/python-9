from config import WEATHER_KEY
from pyowm import OWM

def current_weather(city):
    owm = OWM(WEATHER_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{city},RU')
    w = observation.weather
    temperature = w.temperature('celsius') 
    
    for key, value in temperature.items():
        if key=="temp":
            return value