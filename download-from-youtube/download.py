import pafy

url="" #Enter the youtube URL
#Initializing the video object using pafy.new() method
video=pafy.new(url)

#Retrieving video properties
title=video.title
duration=video.duration
date_published=video.published
uploader=video.username
best_getVideo=video.getbestvideo
max_resolution_video=best_getVideo.resolution
file_format_video=best_getVideo.extension
file_size_video=best_getVideo.filesize()
best_getAudio=video.getbestaudio
file_format_audio=best_getAudio.extension
file_size_audio=best_getAudio.filesize()

print("Name: "+title)
print("duration: "+duration)
print("Uploaded On: "+date_published)
print("Uploaded by: "+uploader)

#Downloading the video with the best quality
print("Downloading "+title+" with "+max_resolution_video+" resolution in "+file_format_video+" format")
best_getVideo.download(filepath="/Movies/"+title+file_format_video,quiet=False,callback=None,meta=False,remux_audio=False)

#Download the audio with best quality
print("Downloading audio "+title+" in "+file_format_audio+" format"
best_getAudio.download(filepath="/Audio"+title+file_format_audio,quiet=False,callback=None,meta=False,remux_audio=False)
