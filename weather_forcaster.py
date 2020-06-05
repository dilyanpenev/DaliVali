from pyowm.owm import OWM


class CitySearch:
    def __init__(self):
        self.owm = OWM('246384c9beadbdc4eb18ced4c193e0ae')
        self.reg = self.owm.city_id_registry()
        self.mgr = self.owm.weather_manager()

    def search_city(self, search_word):
        results = self.reg.ids_for(search_word)
        rv_dict = [{'text': str(name + ', ' + country)} for cityid, name, country in results]
        return rv_dict

    def get_weather_status(self, city_details):
        city_name = city_details[0]
        country_name = city_details[1]
        print(city_name, country_name)
        location = self.reg.locations_for(city_name, country=country_name)
        if isinstance(location, list):
            location = location[0]
        one_call = self.mgr.one_call(location.lat, location.lon)
        # return [one_call.forecast_hourly[i].status for i in range(10)]
        return one_call.forecast_hourly[0].status
