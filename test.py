from utils.request import get_youtube_url
from services.VideoService import VideoService
import pafy
import os
import time

if __name__ == "__main__":
    
    video_id = "saN__9XA7yg"
    
    st = time.time()
    
    video_download_start_time = time.time()
    os.system(f"yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 128K --output '{video_id}.mp3' {get_youtube_url(video_id)}")
    print(f"Video convert end in {time.time() - video_download_start_time}")
    
    ffmpeg_start_time = time.time()
    print(video_id)
    os.system(f"ffmpeg -i {video_id}.mp3 -vn -ar 16000 -ac 2 -ab 192k -f mp3 {video_id}after.mp3")
    print(f"FFmpeg convert end in {time.time() - ffmpeg_start_time}")
    
    spleeter_start_time = time.time()
    os.system(f"spleeter separate -o {video_id} {video_id}after.mp3")
    print("Spleeter done", time.time() - spleeter_start_time)
    
    print("whole time = ",time.time() - st)
    