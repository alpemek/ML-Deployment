FROM nvidia/cuda:10.2-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip

RUN mkdir /app
WORKDIR /app

COPY . ./


RUN pip3 install -r requirements.txt

ENV PYTHONPATH .
