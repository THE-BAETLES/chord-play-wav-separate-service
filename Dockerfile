#작성해야함
FROM researchdeezer/spleeter:latest
LABEL maintainer "chobe1<chobe0719@gmail.com>"
LABEL serverType="Music Separate Engine Server"

COPY . /wavSeperateServer
WORKDIR /wavSeperateServer

RUN pip install fastapi && pip install "uvicorn[standard]" && pip install yt-dlp==2022.8.19 && pip install python-dotenv

ENV INPUT_WAV_SAVE_PATH /input
ENV OUTPUT_WAV_SAVE_PATH /output
ENV SERVER_PORT 3000

EXPOSE 3000

ENTRYPOINT ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000"]
