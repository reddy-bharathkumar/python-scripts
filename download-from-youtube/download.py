#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:40:47 2017

@author: bharath
"""
import pafy

url="https://www.youtube.com/watch?v=k9DMXBFHEH4" #Enter the youtube URL

def downloadVideo(url):
    
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
    best_getAudio=video.getbestaudio()
    file_format_audio=best_getAudio.extension
    file_size_audio=best_getAudio.get_filesize()/1024/1024
    
    print("Name: "+title)
    print("duration: "+duration)
    print("Uploaded On: "+date_published)
    print("Uploaded by: "+uploader)
    print("Resolution: "+max_resolution_video)
    
    #Downloading the video with the best quality
    print("Downloading video"+title+" with "+max_resolution_video+" resolution in "+file_format_video+" format")
    print("Format: "+file_format_video)
    print("Size: "+str(file_size_video)+"MB")
    best_getVideo.download(filepath=title+".mp4",quiet=False,callback=None,meta=False,remux_audio=False)
    
    #Download the audio with best quality
    print("Downloading audio "+title+" in "+file_format_audio+" format"+best_getAudio.bitrate)
    print("Size: "+str(file_size_audio)+"MB")
    best_getAudio.download(filepath=title+"."+file_format_audio,quiet=False,callback=None,meta=False,remux_audio=False)
    
#try:    
downloadVideo(url)
#except:
#    print("Sorry, this video can't be downloaded")
