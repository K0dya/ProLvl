import kivy

from kivy.app import App

kivy.require('1.9.0')

from kivy.uix.gridlayout import GridLayout

from kivy.config import Config

Config.set('graphics', 'resizable', 1)

class CalcGridLayout(GridLayout):

    def pushbutton(self, pushing):
        if pushing:
            try:
                self.ids.lbl.text = "full"
                print(1)
            except Exception:
                pass

class My01labelApp(App):

    def build(self):
        return CalcGridLayout()

myApp = My01labelApp()
myApp.run()
