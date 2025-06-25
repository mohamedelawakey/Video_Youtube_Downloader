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

# put your path to download in here
download_path = "C:\Users\Downloads"
url = input("Enter the YouTube video or playlist URL: ")
download_video_or_playlist(url, download_path)
