import pafy

playlist_url="" #Enter YouTube playlist url

playList=pafy.get_playlist(playlist_url)

title=playList.title
author=playList.author
description=playList.description
total_Videos=len(playList['items'])

for video in range(total_Videos):
  #import the download.py file and send the item as a parameter to the function downloadVideo(url)
