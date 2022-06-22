import os

class SeparateService:
    def __init__(self, path: str, sample_rate:int, video_id: str, output_path: str) -> None:
        """
        params:
            path: Wav file path [str]
            sample_rate: audio sample rate default: 16000 [int]
            video_id: youtube videurl videoId [str]
            output_path: Base output path [str]
        """
        self.sample_rate = sample_rate
        
        
        self.path = path
        self.video_id = video_id
        self.output_path = output_path


    def separate(self) -> str:
        """
        Returns:
            result: A path like self.output_path/self.video_id/accompaniment.wav [str]
        """
        print(f"Spleeter separate start input path: {self.path}")
        os.system(f"spleeter separate -i {self.path} -o {self.output_path}")

        result = os.path.join(self.output_path, self.video_id, "accompaniment.wav")
        print(f"Spleeter separate done output path: {result}")
        return result