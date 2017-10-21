import pafy

url="" #Enter the youtube URL
#Initializing the video object using pafy.new() method
video=pafy.new(url)

#Retrieving video properties
title=video.title
rating=video.rating
duration=video.duration
likes=video.likes
dislikes=video.dislikes
category=video.category
date_published=video.published
uploader=video.username
best_getVideo=video.getbestvideo
max_resolution_video=best_getVideo.resolution
file_format_video=best_getVideo.extension
file_size_video=best_getVideo.filesize()
best_getAudio=video.getbestaudio
file_format_audio=best_getAudio.extension
file_size_audio=best_getAudio.filesize()

#Downloading the video with the best quality
best_getVideo.download(filepath="/Movies",quiet=False,callback=None,meta=False,remux_audio=False)

#Download the audio with best quality
best_getAudio.download(filepath="/Audio",quiet=False,callback=None,meta=False,remux_audio=False)
