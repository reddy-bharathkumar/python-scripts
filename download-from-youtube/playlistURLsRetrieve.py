#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:14:04 2017

@author: bharath
"""

import pafy
import download
import urllib
from bs4 import BeautifulSoup

def retrieveURLfromPlayList(playListURL, audio_video):

    playlist=pafy.get_playlist(playListURL)
    
    print("-------------------------------------------------------------------")
    print(playListURL)
    print playlist['title']
    print playlist['author']
    print len(playlist['items'])

    data=urllib.urlopen(playListURL).read()
    soup=BeautifulSoup(data,"lxml")
    urls=soup.find_all('a', href=True)
    try:
        for url in urls:
            if url.get_text(strip=True):
                if "/watch?v" in url['href']:
                        youTubeURL="https://www.youtube.com"+url['href']
                        download.downloadVideo(youTubeURL,audio_video)
    except:
        pass

def retrievePlayListURL(query, audio_video):
    search_query=urllib.urlencode({"query":query})
    main_url="http://www.youtube.com/results?search_"+search_query
    data=urllib.urlopen(main_url).read()
    soup=BeautifulSoup(data,"lxml")
    
    urls=soup.find_all('a', href=True)
    count=0   
    for url in urls:
        if url.get_text(strip=True):
            if "/playlist?list=" in url['href']:
                count=1
                playListURL="https://www.youtube.com"+url['href']
                retrieveURLfromPlayList(playListURL, audio_video)
            if count==1:
                break