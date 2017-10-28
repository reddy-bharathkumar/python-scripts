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

import typingTest
import paragraphs

class BoxLayouts(BoxLayout):
    app=ObjectProperty(None)
    
class HomeScreen(Screen):
    pass
    
class InputScreen(Screen):
    def buttonPressed(self, instance):
        mode=self.get_id(instance)
        print(mode)
        para_key=str(randint(1,11))
        print(para_key)
        text=paragraphs.paradict(mode,para_key)
        print(text)
        
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
