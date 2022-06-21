from typing_extensions import assert_type
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
import os

class SeparateService:
    def __init__(self, path: str, model: Separator, audio_loader: AudioAdapter, sample_rate:int, video_id: str, output_path: str) -> None:
        self.sample_rate = sample_rate
        self.model = model
        self.audio_loader = audio_loader
        self.path = path
        self.video_id = video_id
        self.output_path = output_path


    def separate(self) -> str:
        # default bit rate is 128k
        # save path is base_save_folder/filename/instrument.wav
        self.model.separate_to_file(audio_descriptor=self.path, destination=self.output_path)

        result_path = os.path.join(self.output_path, self.video_id, "accompaniment.wav")
        assert os.path.exists(result_path)
        return result_path