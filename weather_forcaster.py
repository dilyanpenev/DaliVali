from pyowm.owm import OWM
from datetime import datetime


def get_remaining_hours(timezone='EEST'):
    hour_now = datetime.now().hour
    return 24 - hour_now


def calculate_rain_chance(status_list, rain_list, hour_range):
    advice = 0
    if 'Rain' in status_list:
        next_rain = None
        for no, status in enumerate(status_list):
            if status == 'Rain':
                if rain_list[no].get('1h') <= 0.5 and advice < 2:
                    advice = 1
                elif rain_list[no].get('1h') <= 2.5 and advice < 3:
                    advice = 2
                else:
                    advice = 3
                if next_rain is None:
                    next_rain = no
        if advice == 1:
            advice = 'Nothing more than a drizzle today.'
        elif advice == 2:
            advice = 'You\'ll definitely need an umbrella today.'
        else:
            advice = 'It\'s not a good idea to go out. Heavy rain is coming.'
        if next_rain == 0:
            advice += ' It\'s probably raining right now.'
        elif next_rain == 1:
            advice += ' It\'s going to rain in 1 hour'
        else:
            advice += ' It\'s going to rain in ' + str(next_rain) + ' hours'
    elif 'Clear' in status_list:
        is_sunny = 24 - hour_range + status_list.index('Clear')
        if 6 <= is_sunny <= 18:
            advice = 'Sunglasses will be more useful than an umbrella today.'
        else:
            advice = 'Fortunately, no rain today.'
    else:
        advice = 'Fortunately, no rain today.'
    return advice


class CitySearch:
    def __init__(self):
        self.owm = OWM('246384c9beadbdc4eb18ced4c193e0ae')
        self.reg = self.owm.city_id_registry()
        self.mgr = self.owm.weather_manager()

    def search_city(self, search_word):
        results = self.reg.ids_for(search_word)
        rv_dict = [{'text': str(name + ', ' + country)} for cityid, name, country in results]
        return rv_dict

    def get_weather_advice(self, city_details, hour_range):
        city_name = city_details[0]
        country_name = city_details[1]
        location = self.reg.locations_for(city_name, country=country_name)
        if isinstance(location, list):
            location = location[0]
        one_call = self.mgr.one_call(location.lat, location.lon)
        status_forecast = [one_call.forecast_hourly[i].status for i in range(hour_range)]
        rain_forecast = [one_call.forecast_hourly[i].rain for i in range(hour_range)]
        advice = calculate_rain_chance(status_forecast, rain_forecast, hour_range)
        return advice
