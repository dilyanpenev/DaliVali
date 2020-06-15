from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from weather_forcaster import CitySearch, get_remaining_hours
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
        weather_status = cs.get_weather_status(self.text.split(', '), get_remaining_hours())
        App.get_running_app().root.current = 'info'
        App.get_running_app().root.screens[2].ids.city.text = self.text
        App.get_running_app().root.screens[2].ids.status.text = weather_status


class RVPage(Screen):
    pass


class InfoPage(Screen):
    pass


class PageManager(ScreenManager):
    pass


class WeatherApp(App):
    def build(self):
        root = PageManager()
        root.add_widget(StartPage(name='start'))
        root.add_widget(RVPage(name='rvpage'))
        root.add_widget(InfoPage(name='info'))
        return root


if __name__ == '__main__':
    WeatherApp().run()
