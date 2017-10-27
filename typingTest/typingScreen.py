#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:58:23 2017

@author: bharath
"""
#import paragraphs
from kivy.app import App
from kivy.uix.label import Label
#from random import randint
#from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TypingScreen(Label):
#    @staticmethod
#    def retrieveParagraph(self,mode):
#        print(mode)
#        para_key=str(randint(1,11))
#        paragraph=paragraphs.paradict(self,mode,para_key)
#        print paragraph

    def __init__(self, **kwargs):
        super(TypingScreen, self).__init__(**kwargs)
        print("Press Enter once your typing is completed!")
    
        self.cols=1
        self.add_widget(Label(text="Just Checking", font_size='20sp'))
        self.add_widget(TextInput(multiline=True, font_size='20sp', focus=True))

class typingScreen(App):
  def build(self):
    return TypingScreen()

if __name__=="__main__":
    typingScreen().run()