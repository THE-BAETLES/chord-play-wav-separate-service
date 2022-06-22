import time
import pafy
import os

class VideoService:
    def __init__(self, video_url, save_folder, save_extension) -> None:
        self.save_extension = save_extension

        self.save_folder = save_folder
        self.save_path = os.path.join(save_folder, video_url + f".{save_extension}")
        self.video_url = video_url

    def convertVideo(self):
        video = pafy.new(self.video_url)

        audio: pafy.Stream = video.getbestaudio(preftype=self.save_extension)

        audio.download(filepath=self.save_path)

    def ffmpegConvert(self):
        os.system(f"ffmpeg -i {os.path.basename(self.save_path)} -vn -ar 16000 -ac 2 -ab 192k -f mp3 {os.path.join(self.save_folder, self.video_url)}.mp3")

    def saveToVolume(self) -> str:
        
        self.convertVideo()

        assert os.path.exists(self.save_path) == True

        self.ffmpegConvert()

        return os.path.join(self.save_folder, self.video_url + ".mp3")

    
        