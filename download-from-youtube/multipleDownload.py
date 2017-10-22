#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 09:02:45 2017

@author: bharath
"""

import urllib
import download
from bs4 import BeautifulSoup

def multipleDownload(query, file_count, audio_video):
    search_query=urllib.urlencode({"query":query})
    main_url="http://www.youtube.com/results?search_"+search_query
    
    data=urllib.urlopen(main_url).read()
    soup=BeautifulSoup(data,"lxml")
    
    urls=soup.find_all('a', href=True)
    
    count=0
    
    for url in urls:
        if url.get_text(strip=True):
            if "/watch?v" in url['href']:
                count=count+1
                if count%2==0:
                    youTubeURL="https://www.youtube.com"+url['href']
                    download.download(youTubeURL, audio_video)
                if count==file_count*2:
                    break;