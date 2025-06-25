import yt_dlp
import os 

def download_video_or_playlist(url, download_path):
    ydl_opts = {
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    'retries': 10,
    'ratelimit': 500000,  
    'nocheckcertificate': True,
    'ignoreerrors': True,  
}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_path = "C:/Users/Alawakey/Desktop/download songs/videos/Data Structures and Algorithms in Python"
url = input("Enter the YouTube video or playlist URL: ")
download_video_or_playlist(url, download_path)
