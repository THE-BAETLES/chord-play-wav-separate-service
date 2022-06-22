import os

class SeparateService:
    def __init__(self, path: str, sample_rate:int, video_id: str, output_path: str) -> None:
        self.sample_rate = sample_rate
        self.path = path
        self.video_id = video_id
        self.output_path = output_path


    def separate(self) -> str:
        os.system(f"spleeter separate -i {self.path} -o {self.output_path}")
        return os.path.join(self.output_path, self.video_id, "accompaniment.wav")