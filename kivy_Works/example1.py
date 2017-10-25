#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:10:34 2017

@author: bharath
"""


import example2
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Example(GridLayout):
    
    def __init__(self, **kwargs):
        def callback(instance):
            example2.Example2().showOutput(instance.text)

        super(Example, self).__init__(*kwargs)
        mode_info=Button(text="Choose a mode", font_size=20,size_hint_x=None, width=380, background_color=[1,2,3,4], border=[20,20,20,20], size_hint_y=None, height=40)
        
        easy_info=Button(text='Easy',size_hint_x=None, width=380, background_color=[1,2,3,4], size_hint_y=None, height=100)
        medium_info=Button(text='Medium',size_hint_x=None, background_color=[1,2,3,4], width=380, size_hint_y=None, height=100)
        hard_info=Button(text='Hard',size_hint_x=None, background_color=[1,2,3,4], width=380, size_hint_y=None, height=100)
#        normal_info=Button(text='', border=[20,20,20,20], background_color=[0,0,0,0], size_hint_y=None, height=100)
        
        self.cols=1
#        self.add_widget(Button(text='', border=[20,20,20,20], background_color=[0,0,0,0], size_hint_y=None, height=40))
        self.add_widget(mode_info)
#        self.add_widget(Button(text='', border=[20,20,20,20], background_color=[0,0,0,0], size_hint_y=None, height=40))
#        self.add_widget(normal_info)
        self.add_widget(easy_info)
        easy_info.bind(on_press=callback)
#        self.add_widget(normal_info)
#        self.add_widget(Button(text='', border=[20,20,20,20], background_color=[0,0,0,0], size_hint_y=None, height=100))
        self.add_widget(medium_info)
        medium_info.bind(on_press=callback)
#        self.add_widget(normal_info)
#        self.add_widget(normal_info)
        self.add_widget(hard_info)
        hard_info.bind(on_press=callback)
#        self.add_widget(normal_info)

class example(App):
    def build(self):
        return Example()
    
if __name__=="__main__":
    example().run()