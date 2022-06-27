from flask import app, Flask, request,  jsonify
from services.SeparateService import SeparateService
from services.VideoService import VideoService
from dotenv import load_dotenv
from utils.request import get_youtube_url
import os

load_dotenv()
global model, audio_loader

input_wav_save_path = os.environ.get("INPUT_WAV_SAVE_PATH")
output_wav_save_path= os.environ.get("OUTPUT_WAV_SAVE_PATH")
listen_port = os.environ.get("SERVER_PORT")

app = Flask(__name__)

@app.route('/separate', methods=["GET"])
def separate() -> str:

    request_params = request.args.to_dict()
    video_id: str = request_params["videoId"]
    video_url = get_youtube_url(video_id)

    print('Video url =',video_url)

    #should modify later
    video_service = VideoService(get_youtube_url(video_id),video_id, input_wav_save_path , "webm")
    wav_path = video_service.save_to_volume()
    
    print("wav_path =", wav_path)
    separate_service = SeparateService(wav_path, 16000, video_id, output_path=output_wav_save_path)
    accompaniment_path = separate_service.separate()

    response = {
        "accompanimentPath": accompaniment_path,
        "videoId": video_id
    }

    return jsonify(response)


if __name__ == "__main__":
    print(f"[Music Separate Engine Server] start listen on {listen_port}")
    app.run(host='0.0.0.0',port=listen_port)
