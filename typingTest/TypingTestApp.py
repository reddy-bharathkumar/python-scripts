#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:46:14 2017

@author: bharath
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout

class BoxLayouts(BoxLayout):
    pass
class HomeScreen(Screen):
    pass
class InputScreen(Screen):
    pass
class ResultScreen(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass

guiPart=Builder.load_file("GUI.kv")

class typingTestApp(App):
    def build(self):
        return guiPart
        
if __name__=='__main__':
    typingTestApp().run()
