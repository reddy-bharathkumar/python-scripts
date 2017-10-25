#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:52:15 2017

@author: bharath
"""

from kivy.uix.textinput import TextInput

class Example2(TextInput):
    
    def __init__(self, **kwargs):
        super(Example2, self).__init__(*kwargs)
        self.add_widget(TextInput())
    @staticmethod
    def showOutput(inputValue):
            print inputValue