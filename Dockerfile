FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    python3-pip \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6

WORKDIR /amazon_service

COPY requirements.txt requirements.txt

RUN pip --no-cache-dir install -r  requirements.txt

COPY . /amazon_service/

EXPOSE 1043

CMD make run_app
