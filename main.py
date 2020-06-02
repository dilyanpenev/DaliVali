from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from weather_forcaster import CitySearch


class StartPage(Screen):
    city = ObjectProperty(None)

    def submit_city(self):
        cs = CitySearch(self.city.text)
        print(cs.list_of_results)

    def delete_prompt(self):
        if self.city.text == 'Enter city name':
            self.city.text = ''


class CitySearchPage(Screen):
    pass


class PageManager(ScreenManager):
    pass


class WeatherApp(App):
    def build(self):
        return PageManager()


if __name__ == '__main__':
    WeatherApp().run()
