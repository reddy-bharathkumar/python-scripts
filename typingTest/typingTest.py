#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:39:33 2017

@author: bharath
"""

import time
import paragraphs
from random import randint

print("Select the mode")
print("1: Easy")
print("2: Medium")
print("3: Hard")

input_choice=input()

text=""

if input_choice==1:
    pass
elif input_choice==2:
    para_key=str(randint(1,11))
    print(para_key)
    text=paragraphs.paradict("easy",para_key)
    print(text)
elif input_choice==3:
    pass
else:
    print("Please choose a level between 1-3")
    exit()

#
#initial_time=time.time()  
#test=raw_input()
#after_time=time.time()
#
#sample_split=text.split()
#test_compare=test.split()
#boolean=True
#
#while boolean:
#  if len(test_compare)<len(sample_split):
#    print("Please enter all the words with proper format.")
#    exit()
#  else:
#    boolean=False
#
#count=0
#mistakes=[]
#
#for i in range(len(sample_split)):
#  if test_compare[i]==sample_split[i]:
#    pass
#  else:
#    count=count+1
#    mistakes.append(test_compare[i])
#
#print("Total words: "+str(sample_split))
#print("Total misspells: "+str(count))
#print(mistakes)
#
#print("Correctly typed words: "+str(sample_split-count))
#
#time_taken=(after_time-initial_time)/60
#
#words=len(test)/5
#wpm=round(words/time_taken)
#accuracy=round((len(sample_split)-count)/len(sample_split),2)*100
#
#print("Your wpm: "+str(wpm))
#print("Accuracy: "+str(accuracy)+"%")