import os
import time
class VideoService:
    def __init__(self, video_url,video_id, save_folder, save_extension) -> None:
        self.save_extension = save_extension

        self.video_id = video_id
        self.save_folder = save_folder
        self.save_path = os.path.join(save_folder, video_id + f".{save_extension}")
        self.video_url = video_url
        self.ffmpeg_save_path =  f"{os.path.join(self.save_folder, self.video_id)}after.mp3"

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):

        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def convert_video(self):
        video_download_start_time = time.time()
        print("Webm to Audio convert start")
        
        if not os.path.exists(self.save_path): 
            os.system(f"yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 128K --output '{self.save_path}' {self.video_url}")
            # video = pafy.new(self.video_url)
            # print("video = ", video)
            # audio: pafy.Stream = video.getbestaudio(preftype=self.save_extension)
            # audio.download(filepath=self.save_path)

        print(f"Webm to Audio convert end in {time.time() - video_download_start_time}s save on {self.save_path}")


    def ffmpeg_convert(self):
        print("FFmpeg convert start")

        if  not os.path.exists(self.ffmpeg_save_path):
            ffmpeg_start_time = time.time()
            os.system(f"ffmpeg -i {self.save_path} -vn -ar 16000 -ac 2 -ab 192k -f mp3 {self.ffmpeg_save_path}")
            print(f"FFmpeg convert end in {time.time() - ffmpeg_start_time}")
        
    def save_to_volume(self) -> str:
        
        self.convert_video()

        assert os.path.exists(self.save_path) == True
        self.ffmpeg_convert()
        return self.save_path

    
        