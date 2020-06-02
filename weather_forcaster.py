from pyowm.owm import OWM


class CitySearch:

    def __init__(self, search_word):
        self.search_word = search_word
        owm = OWM('246384c9beadbdc4eb18ced4c193e0ae')
        reg = owm.city_id_registry()
        self.list_of_results = reg.ids_for(self.search_word)
