from flask import app, Flask, request,  jsonify
from services.SeparateService import SeparateService
from services.VideoService import VideoService
from spleeter.audio.adapter import AudioAdapter
from dotenv import load_dotenv
import os

load_dotenv()
global model, audio_loader

input_wav_save_path = os.environ.get("INPUT_WAV_SAVE_PATH")
output_wav_save_path= os.environ.get("OUTPUT_WAV_SAVE_PATH")

app = Flask(__name__)


@app.route('/separate', method='GET')
def separate() -> str:

    request_params = request.args.to_dict()
    video_id: str = request_params["videoId"]
    #should modify later
    video_service = VideoService(video_id, input_wav_save_path , "webm")
    wav_path = video_service.convertVideo()

    separate_service = SeparateService(wav_path, model, audio_loader, 16000, video_id, output_path=output_wav_save_path)

    accompaniment_path = separate_service.separate()

    
    response: str = {
        "accompaniment_path": accompaniment_path,
        "videoId": video_id
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=1111)