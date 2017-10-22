#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:06:48 2017

@author: bharath
"""

import download
import multipleDownload
import playlistURLsRetrieve

def check_int():
    try:
        num= int(input())
    except ValueError:
        print "This is not a number"
    return num

def singleVideoAudio_Download_URL(audio_video):
    print("Enter YouTube URL to download")
    single_url=raw_input()
    download.download(single_url,audio_video)
def multipleVideoAudio_Download_NoURL(audio_video):
    print("Enter your query: ")
    query=str(raw_input())
    print("No of files to download: ")
    file_count=check_int()
    multipleDownload.multipleDownload(query, file_count, audio_video)
def singlePlayList_Download_URL(audio_video):
    print("Enter your query to search for a Playlist: ")
    playListURL=raw_input()
    playlistURLsRetrieve.retrieveURLfromPlayList(playListURL, audio_video)
def searchPlayList_Download_NoURL(audio_video):
    print("Enter your query: ")
    playList_query=raw_input()
    playlistURLsRetrieve.retrievePlayListURL(playList_query, audio_video)

def video_mode():
    print("You've chosen Video Download mode")
    print("Enter your choice: ")
    print("1 : Download video from a known youtube URL")
    print("2: To download multiple videos from a search")
    print("3: To download all videos from a playlist")
    print("4: To search for a playlist and download all videos from top resulted playlist")
    print("5: If you want to switch to Audio mode")
    
    input_choice=input()

    if input_choice==1:
        singleVideoAudio_Download_URL("video")
    elif input_choice==2:
        multipleVideoAudio_Download_NoURL("video")
    elif input_choice==3:
        singlePlayList_Download_URL("video")
    elif input_choice==4:
        searchPlayList_Download_NoURL("video")
    elif input_choice==5:
        audio_mode()
    else:
        print("Sorry, you've Entered wrong input!")
        print("Please try again.")
        exit
        
def audio_mode():
    print("You've chosen Audio Download mode")
    print("Enter your choice: ")
    print("1 : Download audio from a known youtube URL")
    print("2: To download 4 audio's from search")
    print("3: To download all audio's from a playlist")
    print("4: To search for a playlist and download all audios from top resulted playlist")
    print("5: If you want to switch to Video mode")
    
    input_choice=input()

    if input_choice==1:
        singleVideoAudio_Download_URL("audio")
    elif input_choice==2:
        multipleVideoAudio_Download_NoURL("audio")
    elif input_choice==3:
        singlePlayList_Download_URL("audio")
    elif input_choice==4:
        searchPlayList_Download_NoURL("audio")
    elif input_choice==5:
        video_mode()
    else:
        print("Sorry, you've Entered wrong input!")
        print("Please try again.")
        exit
print("Enter your choice: ")
print("1: To download Video/Video's")
print("2: To download Audio/Audio's")

audio_video_choice=input()

if audio_video_choice==1:
    video_mode()
elif audio_video_choice==2:
    audio_mode()
else:
    print("Sorry, you've Entered wrong input!")
    print("Please try again.")
    exit