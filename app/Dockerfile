FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y supervisor

# # about opencv
# RUN apt-get -y install libgl1-mesa-glx &&\
#     apt-get install libglib2.0-0 -y &&\
#     apt-get install ffmpeg x264 libx264-dev -y &&\
#     apt-get install watch -y

# RUN apt update && \
#     apt install -y postgresql-client

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

COPY . .