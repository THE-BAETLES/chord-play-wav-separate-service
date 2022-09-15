from services.SeparateService import SeparateService
from services.VideoService import VideoService
from dotenv import load_dotenv
from utils.request import get_youtube_url
from fastapi import FastAPI
import os

load_dotenv()
global model, audio_loader

input_wav_save_path = os.environ.get("INPUT_WAV_SAVE_PATH")
output_wav_save_path= os.environ.get("OUTPUT_WAV_SAVE_PATH")
listen_port = os.environ.get("SERVER_PORT")
app = FastAPI()
@app.get('/separate')
def separate(videoId: str) -> str:
    with VideoService(get_youtube_url(videoId),videoId, input_wav_save_path , "mp3") as v:
        wav_path = v.save_to_volume()
    with SeparateService(wav_path, 16000, videoId, output_path=output_wav_save_path) as s:
        accompaniment_path = s.separate()

    response = {
        "accompanimentPath": accompaniment_path,
        "videoId": videoId
    }
    
    return response
def test():
    
    pass

if __name__ == "__main__":
    print(f"[Music Separate Engine Server] start listen on {1201}")
    app.run(host='0.0.0.0',port=1201)
