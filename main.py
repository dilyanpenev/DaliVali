from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


class StartPage(Screen):
    city = ObjectProperty(None)

    def submit_city(self):
        print(self.city.text)

    def delete_prompt(self):
        if self.city.text == 'Enter city name':
            self.city.text = ''


class SecondPage(Screen):
    pass


class PageManager(ScreenManager):
    pass


class WeatherApp(App):
    def build(self):
        return PageManager()


if __name__ == '__main__':
    WeatherApp().run()
