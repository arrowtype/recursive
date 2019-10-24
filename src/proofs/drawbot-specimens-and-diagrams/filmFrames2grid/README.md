# Making a set of gridded frames from a video with ffmpeg and DrawBot

crop into a square:

    ffmpeg -i "VIDEO_PATH.MOV" -filter:v "crop=1080:1080" -c:a copy "VIDEO_PATH.square.MOV"


extract frames to jpg

     ffmpeg -i "VIDEO_PATH.square.MOV" -vf fps=16 VIDEO_PATH-still-%04d.jpg -hide_banner

Adapted from https://www.bugcodemaster.com/article/extract-images-frame-frame-video-file-using-ffmpeg
