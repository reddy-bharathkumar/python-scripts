#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:27:18 2017

@author: bharath
"""
import datetime
import pafy
import urllib
from bs4 import BeautifulSoup

today = datetime.date.today()

def multipleDownload(file_count):
    search_query=urllib.urlencode({"query":"Mahathalli"})
    main_url="http://www.youtube.com/results?search_"+search_query
    print(main_url)
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
                    download(youTubeURL)
                if count==file_count*2:
                    break;

def download(url):
    try:        
        #Initializing the video object using pafy.new() method
        video=pafy.new(url)
        
        #Retrieving video properties
        title=video.title
        duration=video.duration
        date_published=video.published
        uploader=video.username
        best_getVideo=video.getbest()
        max_resolution_video=best_getVideo.resolution
        file_format_video=best_getVideo.extension
        file_size_video=best_getVideo.get_filesize()/1024/1024
        
        if (uploader=="UCFnLGH9BGpJLJMMlRMr-f5Q") & (str(today)==date_published[0:10]):
            print("-------------------------------------------------------------------")
            print("URL: "+url)
            print("Name: "+title)
            print("duration: "+duration)
            print("Uploaded On: "+date_published)
            print("Uploaded by: "+uploader)
            print("Resolution: "+max_resolution_video)
            #Downloading the video with the best quality
            print("Downloading video "+title+" with "+max_resolution_video+" resolution in "+file_format_video+" format")
            print("Size: "+str(file_size_video)+"MB")
            best_getVideo.download(filepath=title+".mp4",quiet=False,callback=None,meta=False,remux_audio=False)
    except:
        print("Sorry this video can't be downloaded")
        
multipleDownload(1)
#download("https://www.youtube.com/watch?v=EijuJw54r_0")

