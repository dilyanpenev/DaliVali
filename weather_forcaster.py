from pyowm.owm import OWM
from datetime import datetime


def get_remaining_hours(timezone='EEST'):
    hour_now = datetime.now().hour
    return 24 - hour_now


class CitySearch:
    def __init__(self):
        self.owm = OWM('246384c9beadbdc4eb18ced4c193e0ae')
        self.reg = self.owm.city_id_registry()
        self.mgr = self.owm.weather_manager()

    def search_city(self, search_word):
        results = self.reg.ids_for(search_word)
        rv_dict = [{'text': str(name + ', ' + country)} for cityid, name, country in results]
        return rv_dict

    def get_weather_status(self, city_details, hour_range):
        city_name = city_details[0]
        country_name = city_details[1]
        location = self.reg.locations_for(city_name, country=country_name)
        if isinstance(location, list):
            location = location[0]
        one_call = self.mgr.one_call(location.lat, location.lon)
        rain_forecast = [one_call.forecast_hourly[i].status for i in range(hour_range)]
        advice = 'No rain today.'
        if 'Rain' in rain_forecast:
            advice = 'You will definitely need an umbrella today.'
            next_rain = rain_forecast.index('Rain')
            if next_rain == 0:
                advice += ' It is probably raining right now.'
            elif next_rain == 1:
                advice += ' It is going to rain in 1 hour'
            else:
                advice += ' It is going to rain in ' + str(next_rain) + ' hours'
        else:
            if 'Clear' in rain_forecast:
                is_sunny = 24 - hour_range + rain_forecast.index('Clear')
                if is_sunny >= 6 and is_sunny <= 18:
                    advice = 'Better get sunglasses than an umbrella.'
        return advice
