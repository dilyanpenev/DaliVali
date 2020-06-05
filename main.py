from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, ListProperty
from weather_forcaster import CitySearch
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button


class StartPage(Screen):
    city = ObjectProperty(None)

    def submit_city(self):
        cs = CitySearch()
        rv_list = cs.search_city(self.city.text)
        self.manager.screens[1].ids.search_res.data = rv_list

    def delete_prompt(self):
        if self.city.text == 'Enter city name':
            self.city.text = ''


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)


class CityButton(Button):
    def __init__(self, **kwargs):
        super(CityButton, self).__init__(**kwargs)

    def on_release(self):
        cs = CitySearch()
        print(cs.get_weather_status(self.text.split(', ')))


class RVPage(Screen):
    pass


class PageManager(ScreenManager):
    pass


class WeatherApp(App):
    def build(self):
        root = PageManager()
        root.add_widget(StartPage(name='start'))
        root.add_widget(RVPage(name='rvpage'))
        return root


if __name__ == '__main__':
    WeatherApp().run()
