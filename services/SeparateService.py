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

    def __enter__(self):
        return self
        pass

    def __exit__(self, *args):
        if os.path.exists(self.path):
            os.remove(self.path)

    def separate(self) -> str:
        """
        Returns:
            result: A path like self.output_path/self.video_id/accompaniment.wav [str]
        """

        result = os.path.join(self.output_path, self.video_id, "accompaniment.wav")

        if os.path.exists(result):
            return result

        print(f"Spleeter separate start input path: {self.path}")
        # development version
        # os.system(f"spleeter separate  -o {self.output_path} {self.path}")

        # research docker container version
        os.system(f"spleeter separate -i {self.path} -o {self.output_path}")


        print(f"Spleeter separate done output path: {result}")
        return result